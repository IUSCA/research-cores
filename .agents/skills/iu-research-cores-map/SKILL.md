---
name: iu-research-cores-map
description: Orientation to Indiana University research core facilities - which cores exist on IU Bloomington, IU Indianapolis, and IU School of Medicine campuses, what each offers (genomics, proteomics, mass spectrometry, light and electron microscopy, cryo-EM, flow cytometry, NMR, crystallography, nanoscale characterization, histology, animal models, human MRI, biostatistics), where IU lists them (IUSM Find a Core, Indiana CTSI service cores, iLab, IU Research, Research Equipment and Tools), and what a core is called now after renames. Includes a script that reads every directory. Use when someone asks what cores or instruments IU has, whether a core still exists, what it is called now, or where to start looking for a core.
---

# IU research cores map

Verified 2026-10-04 against IU core directories and core websites. Sources
are listed at the end.

Start here. Find candidate cores in the catalog, then confirm each one on
its own website before advising anyone. Cores rename, merge, and close. A
name in this skill is a lead, not an answer.

## What a core is at IU

A research core sells instrument time, services, training, and expertise to
many labs. IU School of Medicine describes its cores as offering
"consultations and training, sample testing and processing, data analysis,
access to specialized equipment and instrumentation, and production of
preclinical models" (IUSM About the Service Cores, **Observed 2026-10-04**).

Most cores charge for their work. At IU a core that bills other IU units is a
recharge or service center. **Required.** It may charge only approved rates
that recover no more than allowable cost, under FIN-ACC-400. The
`budgeting-core-services-in-proposals` skill explains what that means for a
grant budget.

## Where IU lists its cores

No single list is complete. Each directory covers part of IU, and each lags
reorganizations differently. **Observed 2026-10-04:**

| Directory | Covers | Size |
| --- | --- | --- |
| IUSM [Find a Core](https://medicine.iu.edu/service-cores/search) | IU School of Medicine, its centers, and some IU Bloomington and South Bend cores | 50 cores |
| Indiana CTSI [Service Cores](https://indianactsi.org/servicecores/) | IU Indianapolis, IU Bloomington, IUSM South Bend, Purdue, and Notre Dame. Marks each as a Designated Service Core or Non-Designated Service Resource | 92 entries, 60 at IU |
| IU [iLab landing page](https://iu.ilab.agilent.com/landing/321) | Every core that books or bills through IU's iLab | 46 cores |
| IU Research [CIMS page](https://research.iu.edu/about/centers-institutes/index.html) | Cores administered centrally by IU Research | 10 core services and facilities |
| College of Arts and Sciences [Facilities](https://facilities.college.indiana.edu/facilities/index.html) | College facilities at IU Bloomington | 5 facilities |
| [Research Equipment and Tools](https://equipment-tools.research.iu.edu/) | Individual instruments, software, and datasets, by unit and campus | 204 items |
| IU Simon Comprehensive Cancer Center [Shared Facilities](https://cancer.iu.edu/research/shared-facilities/index.html) | Cancer center cores | 14 entries |

Read them all at once with the script. It needs only Python:

```bash
s=.agents/skills/iu-research-cores-map/scripts/core_directories.py
$s iusm                    # IUSM Find a Core
$s ctsi                    # Indiana CTSI service cores at IU (--all adds Purdue and Notre Dame)
$s ilab                    # core names on IU's iLab
$s iuresearch              # IU Research core services
$s equipment cryo          # instruments whose name, function, model, or unit matches
$s rrid SCR_025533         # a core's RRID and proper citation
```

The Research Equipment and Tools data was last modified 2026-02-16, per its
server header (**Observed 2026-10-04**). It still names some units by older
names. Trust a core's own website over it.

## The cores by capability

[references/catalog.md](references/catalog.md) lists each core with its
campus, what it offers, its website, how it books, and which directories list
it. This table is the short form.

| Capability | IU Bloomington | IU Indianapolis and IUSM |
| --- | --- | --- |
| Sequencing and genomics | Center for Genomics and Bioinformatics (CGB) | Center for Medical Genomics (CMG) |
| Proteomics and biological mass spectrometry | Laboratory for Biological Mass Spectrometry (LBMS) | Center for Proteome Analysis |
| Small-molecule mass spectrometry | Mass Spectrometry Facility (MSF), Chemistry | Clinical Pharmacology Analytical Core; Chemical Genomics Core Facility |
| Metabolomics | LBMS has "additional interest" | Collaborative Metabolome Core, through external vendors |
| Light microscopy | Light Microscopy Imaging Center (LMIC) | Indiana Center for Biological Microscopy (ICBM); Stark Flow Cytometry and Microscopy |
| Flow cytometry and sorting | Flow Cytometry Core Facility (FCCF) | Cancer center Flow Cytometry Core; Stark Flow Cytometry and Microscopy |
| Electron microscopy and cryo-EM | Electron Microscopy Center (IUB-EMC) | IUSM Center for Electron Microscopy (iCEM) |
| NMR | NMR Facility, Chemistry | Chemical Genomics Core Facility (NMR with cryoprobe) |
| Crystallography and biophysics | Macromolecular Crystallography Facility (MCF/CAF); Physical Biochemistry Instrumentation Facility (PBIF) | |
| Nanoscale fabrication and materials | Nanoscience Core Facility (NCF) | Integrated Nanosystems Development Institute (INDI) |
| Histology and pathology | | Histology Core; Immunohistochemistry Research Core |
| Animal models and phenotyping | Laboratory Animal Resources; CISAB Mechanisms of Behavior Lab | Behavioral Phenotyping Core; Transgenic Animal Core; Laboratory Animal Resource Center; musculoskeletal and ultrasound phenotyping |
| Human brain and body imaging | Imaging Research Facility (IRF), 3T MRI | Office for Research Imaging and Research Imaging Core |
| Biospecimens | | Biospecimen Collection and Banking Core; Biospecimen Management Core; Indiana Biobank |
| Statistics, surveys, and evaluation | Indiana Statistical Consulting Center; Biostatistics Consulting Center; Center for Survey Research; CEPR | Biostatistics and Health Data Science |

South Bend has the IUSM Imaging and Flow Cytometry Core, open to IU, Purdue,
and Notre Dame investigators (its IUSM page, **Observed 2026-10-04**).

Data cores, such as Regenstrief Data Services and the Indiana Biobank, sell
data access rather than instrument time. The companion `research-data`
repository covers them.

## Names change; check before you cite

These changes were **Observed 2026-10-04**. The full list is in
[references/renamed-and-retired.md](references/renamed-and-retired.md).

- The Nanoscale Characterization Facility is now the Nanoscience Core
  Facility. The Research Equipment and Tools database still uses the old
  name.
- The IUSM Medical Imaging Research Institute was "Established in May 2025."
  The IUSM Find a Core page still lists the Indiana Institute for Biomedical
  Imaging Sciences as an affiliation.
- The Neuroscience Core Lab at IU Bloomington appears in Research Equipment
  and Tools. Its iLab page title reads "xArchive Neuroscience Core."
- Directories disagree on names. The Transgenic Animal Core is the
  "Indiana University Transgenic and Animal Core (IUTAC)" on the CTSI site.

**Recommended.** Use the name on the core's own website in a proposal or
paper. Check its RRID too; see `acknowledging-research-cores`.

## Booking and billing systems

Most IU cores book and bill through Agilent iLab. IUSM calls iLab its
"enterprise-wide core facility management system for all research service
cores and shared resources" (IUSM iLab page, **Observed 2026-10-04**). IU
Bloomington cores also use it, such as LMIC, IUB-EMC, NCF, and the Chemistry
MSF. They appear on IU's iLab landing page.

Some cores use other tools. **Observed 2026-10-04:**

- The IRF books MRI time through 25Live in One.IU. New users must first
  contact the MRI technician.
- CGB reserves equipment through its own scheduler.
- PBIF uses its own training and reservation pages.
- The NMR Facility posts its own sign-up rules.

The `using-iu-research-cores` skill covers iLab registration and fund
numbers.

## Keep this file current

- Run `scripts/core_directories.py check`. It compares every directory with
  `references/directory-snapshot.tsv` and prints NEW and GONE names.
  Investigate each one on the core's own website. Update
  `references/catalog.md` and `references/renamed-and-retired.md`. Then
  regenerate the snapshot with `scripts/core_directories.py snapshot`.
- The IUSM search page pages its results with a `CurrentPage` parameter. If
  `iusm` returns only 12 cores, the page changed; fix the script.
- **Open item.** Three hosts serve Research Equipment and Tools with
  identical data: `equipment-tools.research.iu.edu`, `corefacilities.iu.edu`,
  and `corefacilities.indiana.edu`. IU Research links the first. Ask IU
  Research which is canonical.
- **Open item.** IU has no single directory of cores across campuses. Ask IU
  Research whether one is planned.

## Sources

Checked 2026-10-04.

- IUSM Find a Core: https://medicine.iu.edu/service-cores/search
- IUSM About the Service Cores: https://medicine.iu.edu/service-cores/about
- IUSM iLab: https://medicine.iu.edu/service-cores/ilab
- IU iLab landing page: https://iu.ilab.agilent.com/landing/321
- Indiana CTSI Service Cores: https://indianactsi.org/servicecores/
- IU Research CIMS page:
  https://research.iu.edu/about/centers-institutes/index.html
- College of Arts and Sciences Facilities:
  https://facilities.college.indiana.edu/facilities/index.html
- Research Equipment and Tools and its data:
  https://equipment-tools.research.iu.edu/,
  https://equipment-tools.research.iu.edu/resources/01equipment.json
- IU Simon Comprehensive Cancer Center Shared Facilities:
  https://cancer.iu.edu/research/shared-facilities/index.html
- Medical Imaging Research Institute:
  https://medicine.iu.edu/research-centers/medical-imaging
- IRF: https://irf.indiana.edu/
- FIN-ACC-400, Recharge and Service Center Activity:
  https://policies.iu.edu/policies/fin-acc-400-recharge-service-center-activity/index.html
- Each core website, listed in `references/catalog.md`.
