---
name: matching-research-to-cores
description: Turn a research question into a measurement, a technique, an instrument, and an Indiana University core facility that can do it. Walks question to measurement to technique to instrument to core, collects sample type, biosafety, human or animal approvals, throughput, turnaround, data size, campus, and budget, and decides between full service and self-operated instrument time. Includes worked examples for sequencing and single-cell genomics, light microscopy, phosphoproteomics, cryo-EM and crystallography, nanoscale materials characterization, and human fMRI and rodent behavior. Use when someone describes what they want to learn or measure and asks which IU core or instrument fits, or compares two cores for the same job.
---

# Matching research to cores

Verified 2026-10-04 against IU core websites. Sources are listed at the end.

Work from the question, not the instrument. People often ask for an
instrument they have heard of. The right core depends on what must be
measured, in what samples, at what scale.

## The chain

Walk each step in order, and write the answer down:

1. **Question.** What does the researcher want to learn?
2. **Measurement.** What quantity answers it? For example, transcript
   abundance, protein localization, a binding constant, or a BOLD signal.
3. **Technique.** Which methods measure that quantity? Name more than one
   when they trade off resolution, throughput, or cost.
4. **Instrument.** Which instrument class runs the technique?
5. **Core.** Which IU core runs that instrument, on which campus?

[references/technique-map.md](references/technique-map.md) maps common
techniques to IU cores. The `iu-research-cores-map` skill and its catalog
confirm each core exists and what it is called now.

**Recommended.** Stop at step 3 and talk to a core before buying reagents or
collecting samples. Most cores offer a consultation, and several require one
for new projects. The IUSM Center for Electron Microscopy charges a
refundable consultation fee for new projects (its page, **Observed
2026-10-04**).

## Collect the facts

Ask for what the description leaves out. Each answer can change the core.

| Ask | Why it matters |
| --- | --- |
| What samples, from what organism, and how many? | Sample type and count pick the technique and the batch size |
| Human subjects, vertebrate animals, or biohazards involved? | Approvals must exist before the core can run anything; see `using-iu-research-cores` |
| Is any data identifiable or clinical? | Sets where data may go afterward; see `handling-core-instrument-data` |
| Full service, or will the lab run the instrument? | Full service costs more per sample; self-use needs training first |
| How soon are results needed? | Queues are first come, first served at several cores |
| How large will the data be? | Sequencing and imaging can produce terabytes |
| Which campus is the lab on? | Shipping samples is possible, but live cells and animals travel badly |
| What budget and funding source? | Internal and external rates differ; see `budgeting-core-services-in-proposals` |

## Full service or self-use

Cores work in one of two ways, and many offer both.

- **Full service.** Staff run the samples and return data. Examples are
  sequencing at CMG and proteomics at the Center for Proteome Analysis
  (their pages, **Observed 2026-10-04**).
- **Self-use.** Trained users book instrument time and run it themselves.
  LMIC is "a fee for use facility" where trained users reserve time in iLab
  (LMIC Policies, **Observed 2026-10-04**).

**Recommended.** Choose full service for a one-time experiment or a
technique the lab will not repeat. Choose self-use when the lab will run the
instrument often and can spend time on training.

## When two cores could do it

IU often has a core on each campus for the same technique. Compare them on:

- **The exact capability.** CMG lists single-cell and spatial
  transcriptomics, including Xenium. CGB lists library preparation on
  Illumina and Nanopore platforms, with sample forms for small genomes,
  amplicons, ChIP-seq, and methylation (their pages, **Observed
  2026-10-04**).
- **Campus and sample logistics.** Fresh tissue and live cells favor the
  nearer core.
- **Rate tier and access.** Some cancer center cores give cancer center
  members "first priority" and reduced rates (cancer center Shared
  Facilities page, **Observed 2026-10-04**).
- **Turnaround.** Ask the core. No directory lists queue times.

**Practice.** Ask both cores for a quote and a turnaround estimate. Core
staff will often say plainly when the other core is the better fit.

## Things a core cannot fix later

- **Replicates.** The Center for Proteome Analysis says "Biological
  triplicate necessary for statistics" for quantitative services (its page,
  **Observed 2026-10-04**). Plan replicates with the core before the
  experiment.
- **Sample quality.** CMG expects full payment if data is obtained and
  intercepts projects that fail quality control (CMG Payment policy,
  **Observed 2026-10-04**). Follow each core's sample guidelines.
- **Approvals.** A missing IACUC, IRB, or IBC approval stops the work. See
  `using-iu-research-cores`.

## Worked examples

[references/worked-examples.md](references/worked-examples.md) walks the
chain for six kinds of research:

1. Gene expression in mouse liver, bulk and single-cell.
2. Protein localization in live cells.
3. Phosphorylation changes after a stimulus.
4. The structure of a protein complex.
5. A thin film's topography and surface chemistry.
6. Brain activity in people, and memory in a knockout mouse.

Each example is illustrative. Confirm capabilities with the core before
planning around them.

## When IU has no core for it

1. Run `core_directories.py equipment <word>` from `iu-research-cores-map`.
   A department may own the instrument without running a core.
2. Check Purdue and Notre Dame cores listed by the Indiana CTSI. Run
   `core_directories.py ctsi --all`. CTSI designated cores serve its partner
   institutions.
3. Ask whether an IU core can arrange the work with an outside vendor. The
   IUSM Collaborative Metabolome Core works this way. The cancer center has a
   Virtual Core for Novel Technologies that connects researchers with
   external vendors (their pages, **Observed 2026-10-04**).
4. If the need is shared by several NIH-funded labs, consider an S10
   instrument grant. See `budgeting-core-services-in-proposals`.

## Keep this file current

- Re-read the core pages in Sources each review. Update
  `references/technique-map.md` when a core adds or retires a technique.
- Add a worked example when a common kind of request does not fit the six.
- **Open item.** No IU directory lists turnaround times or queue lengths.
  Ask cores whether they publish them.

## Sources

Checked 2026-10-04.

- CMG: https://medicine.iu.edu/service-cores/facilities/medical-genomics
- CMG Payment policy:
  https://medicine.iu.edu/service-cores/facilities/medical-genomics/policies/payment
- CGB: https://cgb.indiana.edu/ and https://cgb.indiana.edu/sequencing/index.html
- Center for Proteome Analysis:
  https://medicine.iu.edu/service-cores/facilities/proteomics
- IUSM Center for Electron Microscopy:
  https://medicine.iu.edu/service-cores/facilities/electron-microscopy
- LMIC Policies: https://lmic.indiana.edu/equipment/policies/index.html
- IU Simon Comprehensive Cancer Center Shared Facilities:
  https://cancer.iu.edu/research/shared-facilities/index.html
- Collaborative Metabolome Core:
  https://medicine.iu.edu/service-cores/facilities/metabolome
- Indiana CTSI Service Cores: https://indianactsi.org/servicecores/
- Other core pages, listed in `references/technique-map.md`.
