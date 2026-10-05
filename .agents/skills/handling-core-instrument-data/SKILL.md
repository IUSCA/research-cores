---
name: handling-core-instrument-data
description: Handle the data an Indiana University core facility or instrument produces - how cores deliver data (web data portals, OneDrive, drives, cloud buckets), how long a core keeps its copy, what to check on receipt, copying to IU storage such as Slate-Project and the Scholarly Data Archive with Globus, classifying instrument data before it moves (including identifiable human MRI data), recording provenance such as core, RRID, and instrument settings, and depositing to public repositories. Points to the research-technologies and research-data companion repositories for storage, transfer, classification, and sharing. Use when someone is about to receive or download data from an IU core, asks how long a core keeps data, lost a core's delivery, or needs to plan storage for sequencing, imaging, or mass spectrometry output.
---

# Handling core instrument data

Verified 2026-10-04 against IU core data policies. Sources are listed at the
end.

The core's copy is not your copy. Most cores keep data only for a short
window. Plan where the data goes before the first run.

This skill covers the hand-off from the core. Two companion repositories
cover the rest:

- `research-technologies` covers IU storage and transfer. Its
  [`storing-and-moving-research-data`](https://github.com/IUSCA/research-technologies/tree/main/.agents/skills/storing-and-moving-research-data) skill covers Slate-Project, the
  Scholarly Data Archive (SDA), and Globus.
- `research-data` covers classification, management plans, and sharing.
  Its [`classifying-research-data`](https://github.com/IUSCA/research-data/tree/main/.agents/skills/classifying-research-data) and [`sharing-research-data`](https://github.com/IUSCA/research-data/tree/main/.agents/skills/sharing-research-data) skills apply
  here.

## How long a core keeps data

Ask each core. Two examples, **Observed 2026-10-04**:

- **CMG.** Raw sequencing data "is automatically pushed into" the SDA. "The
  user is responsible for maintaining the data once backup is complete." CMG
  "is not responsible for the potential data loss after a month from the
  date the data is shared." Retrieval after a loss carries a fee (CMG Data
  Transfer and Data Storage policies).
- **LMIC.** Image data is delivered through a web data portal. "Download
  your files within 15 days. After this period, the files will be moved to
  the SDA archive." Archived files can be staged again for download (LMIC
  data portal page).

**Recommended.** Treat the delivery window as the deadline for your own
copy. Do not rely on a core's archive as your backup.

## How cores deliver data

CMG lists four routes (CMG Data Transfer policy, **Observed 2026-10-04**):

| Route | When |
| --- | --- |
| A web data portal | "the preferred platform for sharing large datasets with IU investigators" |
| OneDrive | "Most of the data analysis results" |
| A portable hard drive | The user provides or buys the drive |
| An AWS S3 bucket | External users who set one up and grant access |

Some IU cores offer a web data portal as a delivery option. Choose it when
it helps the next step, such as keeping a run's files and metadata together
for processing. The portals seen at CMG and LMIC share a pattern:

- Log in with IU credentials.
- Download a dataset within the delivery window.
- After the window, data moves to archive. Ask for it to be staged before
  downloading again.

Each portal has its own help page on the core's site. Ask the core for its
portal's address and window. **Open item.** No IU page lists which cores
deliver through a portal.

## Before data moves: classify it

Classify the data before it leaves the instrument or the portal. The
classification decides where it may be stored and computed on.

- Most cell, tissue, and materials data is not sensitive.
- Human imaging, human genomic, and clinical data may be Restricted or
  Critical, or may be PHI. Ask SecureMyResearch or the Human Subjects
  Office when unsure.
- **Practice.** Treat head MRI as identifiable even without names. A face
  can be rebuilt from a structural scan. Deface images before sharing when
  the protocol allows.
- **Required.** The NMR Facility assumes submitted samples and metadata are
  anonymized, with Critical data removed (NMR Policies, **Observed
  2026-10-04**). Other cores may expect the same. Do not send identifiers
  to a core unless the core and the IRB protocol allow it.

The `classifying-research-data` skill in `research-data` explains IU's
classifications. The [`iu-research-computing-map`](https://github.com/IUSCA/research-technologies/tree/main/.agents/skills/iu-research-computing-map) skill in
`research-technologies` says which IU systems may hold PHI.

## On receipt

**Recommended.** Do these the day the data arrives:

1. Check file counts and sizes against the core's report.
2. Verify checksums if the core supplies them. Compute your own if it does
   not.
3. Copy the data to project storage, not a laptop. For working data,
   Slate-Project. For a long-term copy, the SDA. Move large data with
   Globus. See `storing-and-moving-research-data` in `research-technologies`.
4. Keep the core's quality control reports with the data.
5. Tell the core you have a verified copy, if it asks.

Bundle many small files, such as image tiles, before they reach the SDA.
The IU Knowledge Base says to bundle collections of 100 or more files
(KB0025237). The `storing-and-moving-research-data` skill in
`research-technologies` explains how.

## Record where the data came from

**Recommended.** Keep a short provenance record with each dataset:

- The core's name as written on its site, and its RRID if it has one. See
  `acknowledging-research-cores`.
- The instrument model, settings, run or order number, and date.
- The core's protocol or kit, and software versions for any processing the
  core did.
- The iLab request number, for matching data to charges later.

Methods sections and repository deposits ask for these. They are hard to
recover after the core's window closes.

## Sharing and depositing

Journals and sponsors often require deposit in a public repository. Ask the
core early whether it will help. The Center for Proteome Analysis lists
"upload of all project data to a publicly available source for publication
submission" as a service (its page, **Observed 2026-10-04**).

The `sharing-research-data` and [`planning-data-management-and-sharing`](https://github.com/IUSCA/research-data/tree/main/.agents/skills/planning-data-management-and-sharing)
skills in `research-data` cover repositories, sponsor rules, and
data management and sharing plans.

## Keep this file current

- Re-read each core data policy in Sources each review. Delivery windows
  change.
- Add a core to "How long a core keeps data" when its page states a window.
- **Open item.** No IU policy sets a minimum time a core must keep raw
  instrument data. Ask the cores and the University Data Management Council.

## Sources

Checked 2026-10-04.

- CMG Data Transfer and Data Storage policies:
  https://medicine.iu.edu/service-cores/facilities/medical-genomics/policies/data-transfer,
  https://medicine.iu.edu/service-cores/facilities/medical-genomics/policies/data-storage
- LMIC data portal page: https://lmic.indiana.edu/data-portal/index.html
- NMR Facility Policies: http://nmr.chem.indiana.edu/nmrblog/?page_id=2513
- Center for Proteome Analysis:
  https://medicine.iu.edu/service-cores/facilities/proteomics
- [KB0025237](https://servicenow.iu.edu/kb?id=kb_article_view&sysparm_article=KB0025237)
  Best uses for an IU SDA account, as cited by `research-technologies`
  (verified there 2026-10-03)
