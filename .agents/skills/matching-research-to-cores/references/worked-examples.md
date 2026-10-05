# Worked examples

These examples walk the chain from `SKILL.md`: question, measurement,
technique, instrument, core. They are illustrative. Capabilities were
**Observed 2026-10-04** on each core's page. Confirm with the core before
planning around them, and get a current quote.

Each example ends with what to settle before the first sample.

## 1. Gene expression in mouse liver

**Question.** Which genes change in mouse liver after a drug treatment? Are
the changes in hepatocytes or in immune cells?

| Step | Answer |
| --- | --- |
| Measurement | Transcript abundance, first across the tissue, then per cell type |
| Technique | Bulk RNA-seq for the whole tissue; single-cell or single-nucleus RNA-seq for cell types; spatial transcriptomics to keep tissue position |
| Instrument | Illumina sequencers; 10x Genomics single-cell and Visium or Xenium platforms |
| Core | Center for Medical Genomics (CMG), Indianapolis, for all three. CGB, Bloomington, for bulk libraries and sequencing |
| Analysis | Bioinformatics Core, Indianapolis, fee for service; CGB bioinformatics, Bloomington |

Settle first:

- The CMG holds monthly single-cell and spatial office hours with 10x
  Genomics staff. It also books virtual consultations for planning and
  estimates (CMG page). Use one before collecting tissue.
- The animal protocol must cover the treatment and the tissue collection.
- Plan where the data goes. CMG says it "is not responsible for the
  potential data loss after a month from the date the data is shared" (CMG
  Data Storage policy). See `handling-core-instrument-data`.

## 2. Protein localization in live cells

**Question.** Where does a tagged protein go in a cell over an hour after a
stimulus?

| Step | Answer |
| --- | --- |
| Measurement | Position of a fluorescent signal over time |
| Technique | Live-cell spinning-disk confocal for speed and low phototoxicity; laser-scanning confocal for fixed endpoints; structured illumination when structures sit below about 200 nm |
| Instrument | Spinning-disk confocal; laser-scanning confocal; OMX super-resolution |
| Core | LMIC, Bloomington, has all three. ICBM, Indianapolis, has confocal and multiphoton systems |

Settle first:

- LMIC is self-use. Book training first. Reservations are "up to two weeks
  in advance" and missed time not cancelled by 5pm the day before is charged
  (LMIC Policies).
- Data acquired on the OMX must acknowledge its S10 grant. See
  `acknowledging-research-cores`.

## 3. Phosphorylation after a stimulus

**Question.** Which proteins change phosphorylation within 15 minutes of a
growth factor?

| Step | Answer |
| --- | --- |
| Measurement | Abundance of phosphopeptides relative to total protein |
| Technique | Phosphopeptide enrichment, tandem mass tag labeling, fractionation, LC-MS/MS |
| Instrument | High-resolution Orbitrap-class mass spectrometer |
| Core | Center for Proteome Analysis, Indianapolis, offers phosphorylation quantification. LBMS, Bloomington, specializes in PTMs including phosphorylation |

Settle first:

- The Center for Proteome Analysis says "Biological triplicate necessary for
  statistics" for this service. Design replicates before the experiment.
- Contact the core "by email or through iLab prior to submitting samples"
  (Center for Proteome Analysis page).
- Ask whether the core will deposit data to a public repository at
  publication. The center lists upload of project data as a publication
  support service.

## 4. Structure of a protein complex

**Question.** What is the three-dimensional structure of a purified
complex, and how tightly do its parts bind?

| Step | Answer |
| --- | --- |
| Measurement | Atomic or near-atomic coordinates; binding affinity |
| Technique | Single-particle cryo-EM for large or flexible complexes; X-ray crystallography if it crystallizes; solution NMR for small, dynamic proteins; ITC or microscale thermophoresis for affinity |
| Instrument | Cryo-TEM; crystallization robots and a synchrotron beamline; 600 to 800 MHz NMR; ITC and MST instruments |
| Core | IUSM Center for Electron Microscopy, Indianapolis: grid preparation, screening, and collection on a Glacios, with grids shipped for collection on a Krios G4 at Purdue. IUB-EMC, Bloomington: Talos Arctica cryo-EM. MCF/CAF, Bloomington: crystallization, with remote synchrotron access through the Molecular Biology Consortium. NMR Facility, Bloomington. PBIF, Bloomington, for affinity |

Settle first:

- The IUSM Center for Electron Microscopy requires a consultation, with a
  fee refunded at project completion.
- Sample purity and homogeneity decide which method works. Screen with
  negative stain or small-scale crystallization before committing.
- PBIF users "must have clearance from the facility manager" and the MCB
  department office before using the facility (PBIF page).

## 5. A thin film's topography and surface chemistry

**Question.** Is a deposited film uniform, how rough is it, and what is its
surface composition?

| Step | Answer |
| --- | --- |
| Measurement | Surface height map; elemental and chemical state at the surface; cross-section thickness |
| Technique | Atomic force microscopy; X-ray photoelectron spectroscopy; SEM; focused ion beam cross-sections; profilometry |
| Instrument | Asylum AFMs; PHI Versaprobe II XPS; FEI Quanta 600 SEM; Zeiss Auriga FIB; KLA Tencor profiler |
| Core | Nanoscience Core Facility (NCF), Bloomington. INDI, Indianapolis, has FESEM, AFM-IR, XRD, and a profilometer. IUB-EMC for atomic-resolution TEM |

Settle first:

- NCF asks users to contact it for instrument training (NCF Instruments
  page).
- Fabrication happens in the NCF cleanroom, which has its own resources
  page. Read it before planning fabrication.

## 6. Brain activity in people, and memory in a knockout mouse

**Question A.** Which brain regions respond during a decision task, and do
they differ in older adults?

| Step | Answer |
| --- | --- |
| Measurement | BOLD signal during the task; brain structure as a covariate |
| Technique | Task fMRI, structural MRI, and diffusion imaging |
| Instrument | 3 Tesla MRI scanner with stimulus delivery, eye tracking, and response devices |
| Core | Imaging Research Facility (IRF), Bloomington: Siemens 3T Prisma. Office for Research Imaging, Indianapolis, for studies that use IU Health and IUSM imaging resources |

Settle first:

- The study needs IRB approval before scanning anyone.
- At the IRF, book through 25Live in One.IU. New users contact the MRI
  technician for 25Live access (IRF page).
- In Indianapolis, "All studies utilizing radiologic imaging resources for
  research purposes must register their studies with the Office for Research
  Imaging" (IUSM Research Imaging page).
- Human MRI data is identifiable. Classify it before it leaves the scanner.
  See `handling-core-instrument-data`.

**Question B.** Does knocking out a gene impair memory in mice, and why?

| Step | Answer |
| --- | --- |
| Measurement | Behavior in memory tasks; synaptic plasticity |
| Technique | Rodent cognitive assays; brain slice electrophysiology for long-term potentiation |
| Instrument | Behavioral apparatus; slice electrophysiology rigs |
| Core | Transgenic Animal Core to make the mouse; Behavioral Phenotyping Core for testing; Electrophysiology Core for slices. All in Indianapolis |

Settle first:

- The animal protocol must cover breeding, testing, and tissue collection.
  Knockout animals also need an IBC protocol (IU Research Institutional
  Biosafety Committee page).
- The Behavioral Phenotyping Core "validates all assays" and advises on
  analysis. Agree on group sizes with it before breeding (its page).

## Sources

Checked 2026-10-04.

- CMG and its Data Storage policy:
  https://medicine.iu.edu/service-cores/facilities/medical-genomics,
  https://medicine.iu.edu/service-cores/facilities/medical-genomics/policies/data-storage
- CGB: https://cgb.indiana.edu/sequencing/index.html
- LMIC Policies: https://lmic.indiana.edu/equipment/policies/index.html
- ICBM: https://medicine.iu.edu/internal-medicine/research/centers/biological-microscopy
- Center for Proteome Analysis:
  https://medicine.iu.edu/service-cores/facilities/proteomics
- LBMS: https://bms.lab.iu.edu/
- IUSM Center for Electron Microscopy:
  https://medicine.iu.edu/service-cores/facilities/electron-microscopy
- IUB-EMC: https://iubemcenter.indiana.edu/
- MCF/CAF: https://facilities.college.indiana.edu/facilities/mcf/index.html
- PBIF: https://facilities.college.indiana.edu/facilities/pbif/index.html
- NMR Facility: http://nmr.chem.indiana.edu/nmrblog/
- NCF Instruments: https://nano.indiana.edu/instruments/index.html
- INDI instruments, in Research Equipment and Tools:
  https://equipment-tools.research.iu.edu/resources/index.html
- IRF and its MRI page: https://irf.indiana.edu/,
  https://irf.indiana.edu/our-facility/mri.html
- IUSM Research Imaging:
  https://medicine.iu.edu/service-cores/facilities/research-imaging
- Behavioral Phenotyping Core:
  https://medicine.iu.edu/service-cores/facilities/behavioral-phenotype
- Transgenic Animal Core: https://medicine.iu.edu/service-cores/facilities/transgenic
- IU Research Institutional Biosafety Committee:
  https://research.iu.edu/compliance/biosafety/index.html
- Electrophysiology Core:
  https://medicine.iu.edu/research-centers/neurosciences/Core-Services/Electrophysiology-Core
