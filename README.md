# research-cores

Agent skills for research core facilities at Indiana University. They help a
researcher or a coding agent find the core and instrument that fit a research
question. They also cover getting access, paying for core work in a grant,
acknowledging cores in papers, and handling the data an instrument produces.

## Companion repositories

Four repositories cover research at IU. Skills name a companion's skill by
its repository and skill name, as in "`sharing-research-data` in
research-data," and link the first mention to the skill on GitHub.

- [research-technologies](https://github.com/IUSCA/research-technologies) covers clusters, storage, data transfer, and
  allocations.
- [research-data](https://github.com/IUSCA/research-data) covers finding, classifying, managing, and sharing research
  data.
- [research-funding](https://github.com/IUSCA/research-funding) covers planning and preparing grant proposals.
- **research-cores** (this repository) covers core facilities, their instruments, and the data
  they deliver.

research-funding covers proposal drafting as a whole. This repository covers
only the core-specific parts of a proposal: quotes, rates, letters, and
facilities text.

## Quickstart

1. Clone this repository.
2. Start your agent in the clone. Claude Code, Codex, OpenCode, and pi all
   find the skills there with no install step.
3. Ask: "I want to measure protein phosphorylation changes in mouse liver.
   Which IU core should I talk to?"

## What the skills trust

Cores rename, merge, move, and close. An agent must not trust its own memory
of IU cores. Each skill says where every claim came from.

Every claim carries one of these markers, or cites its source inline:

| Marker | Meaning | Must cite |
| --- | --- | --- |
| **Required** | A binding rule: an IU policy, a federal regulation, a sponsor term, or a core's own written policy | The policy, regulation, notice, or core policy page |
| **Recommended** | A practice this repository advises where no rule applies | The reason |
| **Observed** | Read from a live page or directory, such as a core's rate table | The date and the URL or command |
| **External** | From a non-IU source, such as an NIH or NSF page | The source |
| **Practice** | A lesson from experience that no source states | How to check it, where possible |
| **Open item** | No source answers it, or sources conflict | The sources that disagree |

Sources rank this way:

1. **IU policy, federal rules, and sponsor terms** bind. A core's written
   policy binds its own users.
2. **A core's own website** is the source of truth for what it offers, its
   rates, and how to request service.
3. **IU's core directories** say which cores exist. No single directory is
   complete. The `iu-research-cores-map` skill reads all of them with a
   script.

Rates, instruments, and contacts change every year. A rate in this
repository shows the shape of a rate table, not a quote. Get a current quote
from the core.

## What stays out

The skills hold what is true for anyone at IU. They leave out:

- People's names and personal email addresses. Core pages list their own
  staff. Link to the page, not the person.
- Internal hostnames, operations details, and ticket references for the
  systems that deliver core data.
- A researcher's own projects, fund numbers, and quotes. Keep those with the
  project.

## Skills

| Skill | Use it when |
| --- | --- |
| [iu-research-cores-map](.agents/skills/iu-research-cores-map/SKILL.md) | Asking which cores IU has, where they are, or what a core is called now. Start here. |
| [matching-research-to-cores](.agents/skills/matching-research-to-cores/SKILL.md) | Turning a research question into a measurement, a technique, an instrument, and a core. |
| [using-iu-research-cores](.agents/skills/using-iu-research-cores/SKILL.md) | Getting started with a core: iLab, consultation, training, scheduling, rates, samples, and external users. |
| [budgeting-core-services-in-proposals](.agents/skills/budgeting-core-services-in-proposals/SKILL.md) | Putting core work in a grant budget, getting a quote or letter, or writing facilities text. |
| [handling-core-instrument-data](.agents/skills/handling-core-instrument-data/SKILL.md) | Receiving data from a core, keeping it safe, and moving it to IU storage. |
| [acknowledging-research-cores](.agents/skills/acknowledging-research-cores/SKILL.md) | Writing the acknowledgment for a paper, citing a core RRID or S10 instrument grant, or deciding on core authorship. |
| [getting-help-with-research-cores](.agents/skills/getting-help-with-research-cores/SKILL.md) | Deciding whom to ask about a core, iLab, billing, or a missing capability. |

## Use the skills

Each skill is a directory in the open
[Agent Skills](https://agentskills.io/specification) format. A `SKILL.md`
file carries `name` and `description` frontmatter. Scripts use only Python's
standard library, so any harness that can run a shell can use them.

The skills live in `.agents/skills/`. Codex, pi, and OpenCode read that
directory. Claude Code reads only `.claude/skills/`, so `.claude/skills` is a
symbolic link to it.

### As a Claude plugin

This repository is also a Claude plugin marketplace. Installing the plugin
makes every skill available in all your projects, with no clone and no
copying.

In Claude Code:

```text
/plugin marketplace add IUSCA/research-cores
/plugin install research-cores@iusca-research-cores
```

Plugin skills are namespaced, so `matching-research-to-cores` appears as
`research-cores:matching-research-to-cores`. The agent still picks a skill
from its description, so you rarely type the name.

To update, run `/plugin marketplace update iusca-research-cores`.

The plugin reads the skills from `.agents/skills/`, the directory the other
harnesses use, so no skill is duplicated. The manifests are
`.claude-plugin/plugin.json` and `.claude-plugin/marketplace.json`.

### In another project

To use the skills in another project, copy the skill directories you need
into that project's `.agents/skills/`. Or use the
[`skills` CLI](https://github.com/vercel-labs/skills):

```bash
npx skills add <this repository> --list
npx skills add <this repository> --skill matching-research-to-cores --copy
```

Claude Code users can install the
[plugin](#as-a-claude-plugin). For one session only, run
`claude --add-dir ~/repos/research-cores`.

## Maintaining

- [CONTRIBUTING.md](CONTRIBUTING.md) explains how to verify and write a
  single claim.
- [MAINTAINING.md](MAINTAINING.md) is the runbook for reviewing the whole
  set.
- [docs/open-items.md](docs/open-items.md) collects every open question, by
  the office or core that can answer it.
- `tools/check-skills.py` runs the offline checks: format, markers, sources,
  age, and what stays out. `--kb` and `--links` add the network checks, and
  `--freshness` runs every check this repository's weekly workflow runs.
  `tools/check-skills.toml` holds this repository's settings.
- The directory helper,
  `.agents/skills/iu-research-cores-map/scripts/core_directories.py check`,
  reports cores that appeared in or vanished from IU's directories.
  `--freshness` runs it too.
- [tests/trigger-prompts.md](tests/trigger-prompts.md) checks that agents
  load the right skill.

## License

Code, meaning scripts and tools, is under the Educational Community License,
Version 2.0; see [LICENSE](LICENSE). Written content, including every
`SKILL.md` and reference file, is under CC BY 4.0; see
[LICENSE-docs](LICENSE-docs). Copyright the Trustees of Indiana University.
