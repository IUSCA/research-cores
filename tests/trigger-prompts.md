# Trigger prompts

Use these in a fresh session to check that each skill loads when it should.
Each prompt names the skill that should load first. Others may load too.
Step 6 of `MAINTAINING.md` explains the test.

| Prompt | Expected skill |
| --- | --- |
| What core facilities does IU have for microscopy? | `iu-research-cores-map` |
| Is the Nanoscale Characterization Facility still around? | `iu-research-cores-map` (renamed) |
| Does any IU lab have an XPS instrument I could use? | `iu-research-cores-map` (run `core_directories.py equipment`) |
| I want to know which genes change in mouse liver after a drug. Which IU core should I use? | `matching-research-to-cores` |
| Should I use cryo-EM or crystallography for my protein complex, and where at IU? | `matching-research-to-cores` |
| I need fMRI for a decision-making study at IU Bloomington. | `matching-research-to-cores` |
| How do I get an iLab account and add my PI's fund number? | `using-iu-research-cores` |
| Can a collaborator at another university use the LMIC confocals, and what will it cost? | `using-iu-research-cores` |
| What happens if I miss my microscope reservation? | `using-iu-research-cores` |
| How do I budget sequencing from the Center for Medical Genomics in an R01? | `budgeting-core-services-in-proposals` |
| Can I include a letter of support from a core director in my NSF proposal? | `budgeting-core-services-in-proposals` |
| Three of us need a new mass spectrometer. How could we fund it? | `budgeting-core-services-in-proposals` (S10) |
| The CMG says my sequencing data is ready. Where should I put it? | `handling-core-instrument-data` |
| I lost the files the core sent me two months ago. | `handling-core-instrument-data` |
| How do I acknowledge the LMIC in my paper? | `acknowledging-research-cores` |
| What is the RRID for the IU School of Medicine Center for Electron Microscopy? | `acknowledging-research-cores` |
| Should the core manager be a coauthor on my paper? | `acknowledging-research-cores` |
| Who do I ask about a wrong charge from a core? | `getting-help-with-research-cores` |
| The core needs an IBC protocol number. Who handles that? | `getting-help-with-research-cores` |
