# Verifying and updating a skill

A skill is only as good as its last check. Update a skill whenever an agent
finds a claim that no longer matches a core's website, an IU directory, or a
cited policy. [MAINTAINING.md](MAINTAINING.md) is the runbook for reviewing
the whole set.

## Let the live source answer

Cores change faster than any document about them. Check these against the
live source, not a memory of it:

| Fact | Check with |
| --- | --- |
| Which cores exist and what they are called | `iu-research-cores-map/scripts/core_directories.py check`, then the core's own page |
| A core's instruments and services | The core's own page |
| A core's rates, cancellation rules, and data windows | The core's policy, pricing, or fees page |
| An instrument a department owns | `core_directories.py equipment <words>` |
| A core's RRID, and whether it is retired | `core_directories.py rrid <SCR_id>` |
| CTSI award numbers | The Indiana CTSI Citations and Acknowledgments page |

Record such a fact as **Observed**, with the date and the page or command,
as in `Observed 2026-10-04 on the LMIC Policies page`. The checker fails any
**Observed** statement without a date.

When directories disagree with a core's own page, the core's page wins.
Record the other name in
`iu-research-cores-map/references/renamed-and-retired.md`.

## Cite each claim

Every claim carries one of the markers in the README, or cites its source
inline:

- **Required** names the IU policy, federal regulation, sponsor term, or the
  core's own policy page that binds. The checker fails a **Required**
  statement with no source.
- **Recommended** gives the reason.
- **Observed** gives the date and the page or command.
- **External** names the non-IU source, such as an NIH or NSF page.
- **Practice** says how to check the lesson where a check exists.
- **Open item** names the sources that disagree, or says none answers.

Each skill keeps its citations in a Sources list at the end. Quote a policy
when its exact words matter, such as a cancellation rule or an
acknowledgment text.

## Rates and quotes

This repository holds no rates, not even as examples. Agents copy
examples into estimates. A cost estimate needs the core's current rate
page or iLab listing, read at the time, and a written quote. A skill may
describe how rates are structured, such as tiers, units, and extra fees,
and where to read them now.

## Write a lesson as Practice

A Practice lesson saves the next person a mistake. Write it so anyone at IU
can use it:

- State the lesson and the reason.
- Give a check where one exists.
- Leave out the incident: no people, labs, projects, tickets, or dates of
  failures.
- Prefer a citation when a core page backs the lesson. Then it is not
  Practice.

## What stays out

- **People.** No staff names or personal email addresses. Link to the
  core's contact page. Role addresses, such as a core's shared mailbox or
  iLab support, are allowed only after they are added to `allowed_emails` in
  `tools/check-skills.toml`.
- **Internal systems.** No hostnames, server names, or operations details
  for the systems that deliver core data. Name the service, such as "a web
  data portal," and send readers to the core's own help page. Do not name the
  software behind a portal or who operates it.
- **One lab's work.** No project names, fund numbers, or quotes.

## Record what is unknown

Write an open item when no source answers a question, or when sources
disagree. Name the sources and quote the words that differ. Do not resolve a
conflict by picking the more plausible value. Add each open item to
[docs/open-items.md](docs/open-items.md) under the office or core that can
answer it.

Record a closed or renamed core as such. An agent that does not see a core
listed may assume it still exists.

## Update the verified date

Each skill carries a `Verified <date>` line near the top. Change it only
after re-reading every source in that skill's Sources list. A partial
re-read names what it covered, in this form: `Verified 2026-10-04 (CMG and
LMIC pages only). Other sources were verified 2026-07-01.`

## Format and style

- Follow the [Agent Skills specification](https://agentskills.io/specification).
  Keep `name` equal to the directory name, in kebab-case. Keep `description`
  under 1024 characters, and say what the skill does and "Use when."
- Use only `name` and `description` in frontmatter unless a spec field is
  needed.
- Keep `SKILL.md` under 500 lines. Move detail to `references/`.
- Put runnable helpers in `scripts/`. Use the Python standard library.
- Keep skills harness-neutral. Do not name a harness's tools.
- Refer to another skill by its name in backticks. Do not link across skill
  directories, because a skill may be installed alone. Name a companion
  repository's skill with the repository, as in "`storing-and-moving-research-data`
  in `research-technologies`."
- One idea per sentence, under 25 words, with the serial comma.
- Lead each section with its claim, then support it.
- End every skill with a "Keep this file current" section, then Sources.

Run `tools/check-skills.py` before committing. It must print `OK`.

`tools/check-skills.py` is the same file in every repository of this
family. Do not edit it here. Change this repository's settings in
`tools/check-skills.toml`: allowed emails, the Required-source pattern,
the STALE age, link skip lists, and the weekly checks. The first line it
prints carries its version and hash, so copies can be compared.

## Commits

Make one focused commit per skill change. Say in the message which pages
were re-read and which directories were checked.
