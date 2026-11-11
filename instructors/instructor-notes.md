---
title: 'Instructor Notes'
---

## About this course

- Six weeks, **hard cap of 6 hours per week** (about 30 hours in total). Weeks 3 and 5 come in under 6 hours on purpose, and so do the others; the spare time is a buffer.
- This is Part 2 of a two-part course. Learners have finished Part 1. They are still beginners, mostly working adults who want to move into data work or cyber security. Part 2 serves both paths, and every week uses synthetic data made for the course.
- Security content is defensive and analytical only: checking, detecting, hashing and reporting. There are no attack tools or exploit code. The Caesar cipher is taught as a weak teaching cipher, and the notes say so.
- Videos are not chosen yet. Every Watch table lists the planned topics and lengths, marked "To be sourced and checked". Choose and check the videos before the first intake.
- Editor: **PyCharm only** for Part 1 and Part 2 (free core).
- The weeks of this course are numbered 1 to 6. A week from Part 1 is always written "Part 1 Week N".

## Weekly structure

Each week is one episode. Inside it are the week overview, the core sections, a 30-minute **Concepts Bridge** and a **practice task**, each a level-2 heading so they show as sub-items in the menu. The overview's time plan is the source of truth for timings; the `teaching` and `exercises` minutes on each episode are estimates based on it.

| Week | Watch | Read & practise | Bridge | Build | Quiz | Total |
|---|---|---|---|---|---|---|
| 1 | 30 m | 2 h | 30 m | 2 h | 15 m | 5 h 15 m |
| 2 | 30 m | 1 h 45 m | 30 m | 2 h | 15 m | 5 h |
| 3 | 20 m | 1 h 30 m | 30 m | 2 h | 15 m | 4 h 35 m |
| 4 | 30 m | 1 h 45 m | 30 m | 2 h | 15 m | 5 h |
| 5 | 20 m | 1 h 45 m | 30 m | 2 h | 15 m | 4 h 50 m |
| 6 | 20 m | 1 h 30 m | 30 m | 3 h | 15 m | 5 h 35 m |

## Practice tasks

- The tasks are **practice only on this site**. Assessment has not been designed yet. Do not add graded tasks, weightings or deadlines until it is.
- Every task has starter code, a model solution and pytest tests. Learners work inside the unzipped course folder (see the Setup page), because the programs find the data files by their place in it.
- Week 2 changes the learner's own `library.py` and `main.py` from Part 1 Week 6. The Part 1 interface (`Book`, `Library`, `add_book`, `lend`, `return_book`, `available_books`, `search`) must stay the same.
- Week 3 has an optional integrity checker. Its three tests fail until the learner writes it. That is expected.
- Week 6 offers two capstone datasets. The task gives questions to investigate. It does not give the findings.

## The data

- Every dataset is synthetic and was made by a script in the course repository, with a fixed seed. The internet addresses are from ranges reserved for examples.
- The datasets hold planted patterns for the lessons to find. `203.0.113.45` makes 22 failed logins at about 2 am, and `203.0.113.77` asks for 10 pages that do not exist (Weeks 2 and 5). Two login counts are unusual in Week 4. Capstone option A has a burst of failed logins on one night, and option B has revenue that rises in September.
- A pattern in a log or a dataset is a reason to look closer, not proof of an attack. The notes say this each time, so keep to it when you teach.

## Teaching tips

- Course code only uses ideas already taught. Where a later idea is unavoidable, the notes tell learners to leave it as is and say which week explains it.
- On Windows, a plain terminal may not show characters such as `é` correctly. The Week 1 page says PyCharm's Python Console uses UTF-8. This has not been confirmed in PyCharm yet.
- The Week 5 output comes from Pandas 3.1.1. Older versions print some details differently, for example `object` instead of `str` for text columns. The lesson says so.
- Timing figures in the Week 4 bridge are typical values. Learners' numbers will differ.
- The Week 5 bridge gives a general introduction to the Australian Privacy Principles and points to the OAIC website. It is not legal advice. Have someone with privacy knowledge read it before release.

## Before publishing outside ADCI

- The licence is not confirmed. The lesson text was written for this course, but ADCI has not chosen a licence. Confirm it, then update `license` in `config.yaml` and `LICENSE.md`.
- The lesson uses The Carpentries Workbench for layout only; it is not a Carpentries lesson. The `carpentry: 'adci'` setting avoids Carpentries branding, and the ADCI logo comes from ADCI's fork of the theme (`varnish: 'ADCI-Perth/varnish'` in `config.yaml`; see `branding/`).
- Replace the placeholder `contact` email in `config.yaml`, and add the links in `CODE_OF_CONDUCT.md`.
- Source the videos, and check every link before each intake.
- Set up the Canvas quizzes. The question pools are in the course repository, in `curriculum/quizzes/`.
