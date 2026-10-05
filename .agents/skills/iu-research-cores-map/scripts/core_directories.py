#!/usr/bin/env python3
"""Read Indiana University's public core facility directories from a terminal.

Usage:
    core_directories.py iusm                 # IU School of Medicine "Find a Core" list
    core_directories.py ctsi [--all]         # Indiana CTSI service cores (IU only unless --all)
    core_directories.py ilab                 # core names on IU's iLab landing page
    core_directories.py iuresearch           # IU Research core services and facilities
    core_directories.py college              # College of Arts and Sciences facilities
    core_directories.py units                # Research Equipment and Tools, items per unit
    core_directories.py equipment <words>    # Research Equipment and Tools, matching items
    core_directories.py rrid <SCR_id> ...    # resolve core RRIDs to their proper citation
    core_directories.py snapshot             # every directory as "source<TAB>name" lines, with a dated header
    core_directories.py check                # live directories versus the recorded snapshot

IU has no single list of cores. Each directory covers part of IU and lags
reorganizations differently, so this script reads them all. `check` compares
the live directories with references/directory-snapshot.tsv. It prints NEW for
a name that appeared and GONE for one that disappeared. It exits 1 when
anything changed or a directory could not be read.

The iLab landing page also lists contact names and emails. This script prints
core names only. Standard library only.
"""

import html
import json
import pathlib
import re
import sys
import time
import urllib.error
import urllib.request

HERE = pathlib.Path(__file__).resolve().parent
SNAPSHOT = HERE.parent / "references" / "directory-snapshot.tsv"
UA = {"User-Agent": "Mozilla/5.0 research-cores-skills/1.0"}

IUSM_SEARCH = "https://medicine.iu.edu/service-cores/search?CurrentPage={page}"
CTSI_LIST = "https://indianactsi.org/servicecores/"
ILAB_LANDING = "https://iu.ilab.agilent.com/landing/321"
IU_RESEARCH = "https://research.iu.edu/about/centers-institutes/index.html"
COLLEGE = "https://facilities.college.indiana.edu/facilities/index.html"
EQUIPMENT = "https://equipment-tools.research.iu.edu/resources/01equipment.json"
RRID = "https://scicrunch.org/resolver/RRID:{id}.json"


class Unreachable(Exception):
    pass


def get(url, tries=3):
    req = urllib.request.Request(url, headers=UA)
    for attempt in range(tries):
        try:
            with urllib.request.urlopen(req, timeout=40) as resp:
                return resp.read().decode("utf-8", "replace")
        except urllib.error.HTTPError as e:
            if e.code not in (429, 500, 502, 503, 504):
                raise Unreachable(f"HTTP {e.code} from {url}")
        except (urllib.error.URLError, TimeoutError, ConnectionError):
            pass
        time.sleep(4 * 2 ** attempt)
    raise Unreachable(f"no reply from {url} after {tries} tries")


def clean(fragment):
    text = html.unescape(re.sub(r"<[^>]+>", " ", fragment))
    return re.sub(r"\s+", " ", text).strip()


def iusm():
    """Cards on the IUSM core search page, 12 per page, paged by CurrentPage."""
    rows, seen = [], set()
    for page in range(1, 20):
        s = get(IUSM_SEARCH.format(page=page))
        cards = re.findall(r'(?s)<div class="rvt-card__body">(.*?)</li>', s)
        new = 0
        for card in cards:
            link = re.search(r'href="([^"]*)"[^>]*>(.*?)</a>', card)
            if not link:
                continue
            name = clean(link.group(2))
            eyebrow = re.search(r'eyebrow">(.*?)</div>', card)
            url = link.group(1).strip()
            if url.startswith("/"):
                url = "https://medicine.iu.edu" + url
            if name == "Service Cores" or (name, url) in seen:
                continue
            rows.append((name, clean(eyebrow.group(1)) if eyebrow else "", url))
            seen.add((name, url))
            new += 1
        if not new:
            break
        time.sleep(1)
    return rows


def ctsi(include_all=False):
    """Indiana CTSI service cores: institution, designation, name, detail link."""
    s = re.sub(r"(?is)<(script|style)[^>]*>.*?</\1>", "", get(CTSI_LIST))
    s = re.sub(r'(?is)<a [^>]*href="(/servicecores/core/\d+)/?"[^>]*>.*?</a>', r"\nLINK:\1\n", s)
    lines = [ln.strip() for ln in html.unescape(re.sub(r"(?s)<[^>]+>", "\n", s)).split("\n") if ln.strip()]
    designations = ("Designated Service Core", "Non-Designated Service Resource")
    rows, k = [], 0
    while k < len(lines) - 2:
        if lines[k + 1] in designations:
            inst, des, name = lines[k], lines[k + 1], re.sub(r"\s+", " ", lines[k + 2])
            j = k + 3
            while j < len(lines) and not lines[j].startswith("LINK:"):
                j += 1
            link = "https://indianactsi.org" + lines[j][5:] + "/" if j < len(lines) else ""
            if include_all or inst.startswith("IU"):
                rows.append((name, f"{inst}; {des}", link))
            k = j + 1
        else:
            k += 1
    return rows


def ilab():
    """First column of the 'iLab Cores at Indiana University' table. Names only."""
    s = get(ILAB_LANDING)
    rows = []
    for tr in re.findall(r"(?s)<tr[^>]*>(.*?)</tr>", s):
        cells = re.findall(r"(?s)<td[^>]*>(.*?)</td>", tr)
        if cells:
            rows.append((clean(cells[0]), "iLab", ""))
    return rows


def iuresearch():
    """The 'Core services/facilities' list on the IU Research CIMS page."""
    s = get(IU_RESEARCH)
    block = re.search(r"(?s)Core services/facilities:(.*?)<h3", s)
    if not block:
        raise Unreachable("IU Research page no longer has a 'Core services/facilities' heading")
    return [(clean(n), "IU Research", u) for u, n in re.findall(r'href="([^"]+)"[^>]*>(.*?)</a>', block.group(1))]


def college():
    s = get(COLLEGE)
    rows = []
    for href, abbr, name in re.findall(r'(?s)<a href="(/facilities/[^"]+)"><h3[^>]*>(.*?)</h3><p>(.*?)</p>', s):
        rows.append((clean(name), clean(abbr), "https://facilities.college.indiana.edu" + href))
    return rows


def equipment_items():
    try:
        data = json.loads(get(EQUIPMENT))
    except json.JSONDecodeError:
        raise Unreachable("Research Equipment and Tools returned something other than JSON")
    return [v[0] for v in data.values() if v]


def units():
    counts = {}
    for item in equipment_items():
        key = (item.get("Unit") or "(no unit)", item.get("Campus Location") or "")
        counts[key] = counts.get(key, 0) + 1
    return [(u, c, str(n)) for (u, c), n in sorted(counts.items())]


def equipment(words):
    words = [w.lower() for w in words]
    out = []
    for item in equipment_items():
        name = item.get("Equipment Name") or item.get("Software Name") or ""
        hay = " ".join(str(item.get(k) or "") for k in ("Equipment Name", "Software Name", "Function", "Model", "Unit")).lower()
        if all(w in hay for w in words):
            out.append((name, f"{item.get('Unit') or ''}; {item.get('Campus Location') or ''}", item.get("URL") or ""))
    return sorted(out)


def rrid(ids):
    out = []
    for rid in ids:
        rid = rid.upper().replace("RRID:", "")
        try:
            data = json.loads(get(RRID.format(id=rid)))
            hits = data["hits"]["hits"]
        except (Unreachable, json.JSONDecodeError, KeyError) as e:
            out.append((rid, f"could not resolve: {e}", ""))
            continue
        if not hits:
            out.append((rid, "no such RRID", ""))
            continue
        src = hits[0]["_source"]
        name = src["item"].get("name", "")
        desc = src["item"].get("description", "")
        # The registry spells it "NO LONGER IN SERVCE" in some records.
        retired = "NO LONGER IN SERV" in (name + " " + desc).upper()
        citation = src.get("rrid", {}).get("properCitation", "")
        out.append((rid, citation or name, "RETIRED" if retired else ""))
        time.sleep(1)
    return out


SOURCES = {"iusm": iusm, "ctsi": ctsi, "ilab": ilab, "iuresearch": iuresearch, "college": college}


def snapshot_rows():
    rows, failed = [], []
    for source, fn in SOURCES.items():
        try:
            rows += [(source, r[0] if source != "iusm" else f"{r[0]} ({r[1]})") for r in fn()]
        except Unreachable as e:
            failed.append(f"{source}: {e}")
    try:
        rows += [("equipment-unit", u) for u, _, _ in units()]
    except Unreachable as e:
        failed.append(f"equipment: {e}")
    return sorted(set(rows)), failed


def show(rows):
    for row in rows:
        print("  |  ".join(x for x in row if x))
    print(f"{len(rows)} rows.", file=sys.stderr)


def main(argv):
    if len(argv) < 2:
        print(__doc__.strip())
        return 2
    cmd, args = argv[1], argv[2:]
    try:
        if cmd in SOURCES and cmd != "ctsi":
            show(SOURCES[cmd]())
        elif cmd == "ctsi":
            show(ctsi("--all" in args))
        elif cmd == "units":
            show(units())
        elif cmd == "equipment" and args:
            show(equipment(args))
        elif cmd == "rrid" and args:
            show(rrid(args))
        elif cmd == "snapshot":
            rows, failed = snapshot_rows()
            print(f"# Directory snapshot. Observed {time.strftime('%Y-%m-%d')} with scripts/core_directories.py snapshot.")
            print("# One line per directory listing: source<TAB>name. Regenerate after review; see SKILL.md.")
            for source, name in rows:
                print(f"{source}\t{name}")
            for f in failed:
                print(f"ERROR {f}", file=sys.stderr)
            return 1 if failed else 0
        elif cmd == "check":
            recorded = set()
            for line in SNAPSHOT.read_text().splitlines():
                if line and not line.startswith("#") and "\t" in line:
                    recorded.add(tuple(line.split("\t", 1)))
            live, failed = snapshot_rows()
            live = set(live)
            failed_sources = {f.split(":")[0] for f in failed}
            for source, name in sorted(live - recorded):
                print(f"NEW   {source}: {name}")
            for source, name in sorted(recorded - live):
                if source.split("-")[0] not in failed_sources:
                    print(f"GONE  {source}: {name}")
            for f in failed:
                print(f"ERROR {f}")
            changed = len(live - recorded) + len([r for r in recorded - live if r[0].split("-")[0] not in failed_sources])
            print(f"{changed} directory names changed; {len(failed)} directories unreadable.")
            return 1 if changed or failed else 0
        else:
            print(__doc__.strip())
            return 2
    except Unreachable as e:
        print(f"ERROR {e}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
