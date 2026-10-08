# Runbook: reviewing and updating the skill set

This runbook keeps the skills true to IU's cores as they are now. It covers
a full review, the checks that drive it, and when to run it.
`CONTRIBUTING.md` covers how to write and verify a single claim.

## Who decides what is true

- **A core's own website** wins for what the core offers, what it charges,
  and its own policies.
- **IU policy, federal regulations, and sponsor instructions** win for rules
  that bind everyone, such as recharge rates and acknowledgment of federal
  funding.
- **IU's directories** show which cores exist. They lag. When a directory
  and a core's page disagree, keep the core's page and record the other
  name in `references/renamed-and-retired.md`.
- **The core or office itself** settles what no page answers. Record its
  answer with the date and the email or ticket it came from, without naming
  the person.

## When to review

| Trigger | Scope |
| --- | --- |
| Any agent finds a wrong claim during real work | That claim, right away, in its own commit |
| An open issue labeled `freshness` | [Working a freshness issue](#working-a-freshness-issue) |
| Every quarter (January, April, July, October) | The full review below |
| Each July, after new fiscal-year rates take effect | The rate examples in `using-iu-research-cores` |
| A new CTSA award or S10 cycle | `acknowledging-research-cores` and `budgeting-core-services-in-proposals` |
| NIH or NSF issues a new forms version or PAPPG | `budgeting-core-services-in-proposals` |

GitHub Actions runs two checks. On every pull request and push to `main`,
`check-skills.yml` runs `tools/check-skills.py` and fails on any `ERROR`.
Every Monday, `freshness.yml` runs `tools/check-skills.py --freshness`. Here
that means the KB check, the link check, and `core_directories.py check`.
When it finds NEW or GONE names, or `STALE`, `BROKEN`, or `ERROR` lines, it
opens an issue labeled `freshness`, or comments on the one already open.

## Working a freshness issue

A person or their agent works each `freshness` issue by hand. Nothing
edits a skill on its own, because every fixed claim needs someone to read
its source. An agent can do all of this; give it this section and the
issue. A person reviews and merges the pull request.

1. Make a branch from `main`. Run `tools/check-skills.py --freshness`
   again. The issue may be days old, and some lines may have cleared.
2. Work each line by kind:
   - **STALE, KB article changed.** Read the whole article with
     `iukb.py read KB0123456` (in research-technologies'
     `searching-the-iu-knowledge-base` skill). Find every claim citing it,
     in each skill the line names and in that skill's `references/`.
     Fix what changed. Then record the reading with
     `tools/check-skills.py --kb-snapshot KB0123456`.
   - **INFO, text unchanged.** The article was touched but its text was
     not. Record it with `--kb-snapshot KB0123456`. No skill changes.
   - **STALE, not found by KB search.** The article was retired or
     renumbered. Search for its replacement. If there is none, name the
     article without a link, with the date it went missing.
   - **STALE, Verified date too old.** Re-read every source the skill
     cites, then update its Verified line.
   - **BROKEN.** Run `--links` again; a single failure is often transient.
     If it still fails, find the page's new address. If the page is gone,
     find another source or make the claim an open item.
   - **CHANGED.** Run the snapshot script named in the line. Update the
     catalog or directory file it compares against, and every skill that
     names what changed.
3. A claim the new source no longer supports is fixed, cut, or turned into
   an open item in `docs/open-items.md`. A question the source now settles
   leaves the open items.
4. Update the Verified line of each skill you edited. For an article with
   a snapshot entry, `--kb-snapshot` is the record, so the Verified line
   does not need to list it as a partial re-read.
5. Run `tools/check-skills.py --freshness` until no STALE, BROKEN, or
   CHANGED line remains. Commit one skill per commit, with the snapshot
   change in the same commit as the skill it supports.
6. Open a pull request that says `Closes #<issue>`. List each line and
   what you did with it: fixed, unchanged, or opened as an item.

## Full review

Work on a branch. Make one commit per skill, as `CONTRIBUTING.md` asks.

### 1. Lint

```bash
tools/check-skills.py
```

`ERROR` lines must be fixed before merging. They include a **Required**
statement with no source, an **Observed** statement with no date, a
personal email address, an internal hostname, and a skill with no README
row or trigger prompt. `STALE` lines name a skill whose Verified date is
over 120 days old. Re-read its Sources in step 3.

### 2. Check the directories

```bash
s=.agents/skills/iu-research-cores-map/scripts/core_directories.py
$s check
```

For each NEW name, find the core's own page. Add it to
`references/catalog.md` if it offers services to other labs. For each GONE
name, check whether the core closed, renamed, or moved. Record the change in
`references/renamed-and-retired.md`. Then regenerate the snapshot. It
carries its own dated header:

```bash
$s snapshot > .agents/skills/iu-research-cores-map/references/directory-snapshot.tsv
```

A directory that cannot be read prints `ERROR`. Check whether its page
changed shape, and fix the script.

### 3. Re-read the core pages

Every core page cited in a skill's Sources list gets re-read each quarter.
Fix what changed. Rates, cancellation rules, data windows, and
acknowledgment texts change most often.

```bash
tools/check-skills.py --links
```

`BROKEN` lines usually mean a core moved its site. Search for the new page
before removing the citation.

### 4. Check RRIDs and award numbers

```bash
$s rrid SCR_025533 SCR_025538 SCR_025587 SCR_025568 SCR_015346 \
  SCR_028155 SCR_025560 SCR_017845 SCR_024398
```

Mark any RRID the registry now calls retired. Re-read the Indiana CTSI
citation page for new award numbers.

### 5. Work the open items

```bash
grep -rn -i "open item" .agents/skills
```

For each item, try in this order:

1. Can a page or directory answer it now? Record the answer as Observed.
2. Otherwise collect it for the core or office that can answer it. Send one
   message per office with every question batched.
   [docs/open-items.md](docs/open-items.md) holds drafts.

Close an item only with its source: a page and date, or a dated reply.

### 6. Test that agents find the right skill

Start a fresh session in this repository in each harness you support. Try
the prompts in [tests/trigger-prompts.md](tests/trigger-prompts.md). Check
that the expected skill loads and that the answer cites it. Fix a
description that fails to trigger.

### 7. Finish

```bash
tools/check-skills.py
```

It must print `OK`. Open a pull request that lists the pages re-read, the
directory changes, and the open items closed or opened.

## Adding a skill

1. Create `.agents/skills/<name>/SKILL.md`. Keep `name` equal to the
   directory name.
2. Follow `CONTRIBUTING.md` for sources, markers, and style.
3. Add a row to the skills table in `README.md`.
4. Add trigger prompts to `tests/trigger-prompts.md`.
5. Run `tools/check-skills.py`.

## Retiring a skill

Delete the directory and its README row in one commit. Say why in the
message.
