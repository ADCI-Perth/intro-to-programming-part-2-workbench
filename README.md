# Intro to Programming, Part 2 (Workbench version)

The website version of Part 2 of ADCI's beginner Python micro-credential: *Data and Security with Python*. It is built with [The Carpentries Workbench](https://carpentries.github.io/sandpaper-docs/). It is a staging step before the course goes into Canvas. Part 1 has its own Workbench site, in the repository `intro-to-programming-part-1-workbench`.

The course content is maintained in the main course repository, `intro-to-programming-part-2`. This repository holds the converted lesson.

## Structure

| Folder | What is in it |
|---|---|
| `episodes/` | One episode per week (`week-1.md` to `week-6.md`). Each holds the week overview, its sections (1.1, 1.2 ...), the Concepts Bridge and the practice task as level-2 headings, which the menu shows as sub-items. |
| `episodes/files/` | Practice-task starter code, solutions and tests (`week-N/`), lesson code (`code/W.S/` and `code/bridge-N/`) and the text data files |
| `episodes/data/` | The CSV data files, plus `course-data.zip` for learners. The zip keeps the course folder layout, so every program finds its data. |
| `learners/` | Setup and reference pages |
| `instructors/` | Instructor notes |
| `profiles/` | Learner profiles |
| `scripts/` | `convert_from_course.py`, which rebuilds the episodes from the course repository |

## Updating from the course repository

With both repositories side by side in the same folder:

```bash
python scripts/convert_from_course.py ../intro-to-programming-part-2 .
```

This rewrites the week episodes and everything in `episodes/files/` and `episodes/data/`, including the zip. Other pages (home, setup, glossary, instructor notes, profiles, `config.yaml`) are edited by hand. If you add, remove or rename a section, update `scripts/wb_meta.py`.

## Building the site locally

You need R, the Workbench packages and pandoc:

```r
install.packages(c("sandpaper", "varnish", "pegboard", "tinkr"),
  repos = c("https://carpentries.r-universe.dev/", getOption("repos")))
sandpaper::build_lesson()        # builds the site into site/docs and opens a preview
sandpaper::validate_lesson()     # checks links, fenced divs and headings
```

## Before publishing

- Confirm the licence (see `LICENSE.md`).
- Replace the placeholder `contact` in `config.yaml`, and add the code of conduct links in `CODE_OF_CONDUCT.md`.
- The ADCI logo files are in `branding/` (made from `adci-logo-source.jpg` with `branding/make_logo.py`). The theme only loads logos from its own package, so they live in a fork of `varnish` (`ADCI-Perth/varnish`): `adci-logo.svg` and `adci-logo-sm.svg` go in `inst/pkgdown/assets/assets/images/`, and `favicons/adci/` goes in `inst/pkgdown/assets/favicons/`. `config.yaml` pins the fork with `varnish: 'ADCI-Perth/varnish'`. In dark mode the theme shows every logo in plain white.
