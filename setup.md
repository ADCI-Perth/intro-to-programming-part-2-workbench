---
title: Setup
---

You need the same two free programs as in Part 1: **Python 3.12 or newer** and **PyCharm**. This page is a short checklist. It also shows how to get the course files and which packages to install, and when.

## Software Setup

::::::::::::::::::::::::::::::::::::::: discussion

### What you need

- **Python 3.12 or newer** from [python.org](https://www.python.org/downloads/). Check with `python --version` (Windows) or `python3 --version` (Mac and Linux).
- **PyCharm** from [jetbrains.com/pycharm](https://www.jetbrains.com/pycharm/download/). The core features are free, and everything in this course works in them.
- Your own **`library.py` and `main.py` from Part 1 Week 6**. You add to them in Week 2.

If you finished Part 1, you already have all of this.

:::::::::::::::::::::::::::::::::::::::::::::::::::

## Get the course files

Download the [course zip file](data/course-data.zip) and unzip it into your Documents folder. It gives you an `IntroToProgrammingPart2` folder with:

- an `assets` folder with the synthetic data files the lessons use (`files` and `data`);
- a `weeks` folder with the lesson code for each section, and each week's practice task (starter file, model solution and tests).

Open the `IntroToProgrammingPart2` folder in PyCharm (**File > Open**). **Keep the folder layout.** The programs find their data files by their place in this folder, so they will not find them if you move them.

## Create a virtual environment

A virtual environment is a private set of packages for one project. Week 4 explains what it is and why you want one. You can create it now, or when you reach Week 4:

1. In PyCharm, open **Settings > Python > All Interpreters**. In older PyCharm versions this is **Settings > Project > Python Interpreter**.
2. Add a new interpreter and choose **Virtualenv** (a new environment in the project folder).
3. Open the **Terminal** tab at the bottom of PyCharm. You should see `(.venv)` at the start of the line.

## Install packages when you need them

Install each package with `python -m pip install`, in the PyCharm Terminal, with the virtual environment active.

| When | Command | What it is for |
|---|---|---|
| Week 1 | `python -m pip install pytest` | Running the practice tests |
| Week 4 | `python -m pip install numpy` | Arrays and statistics |
| Week 5 | `python -m pip install pandas` | Tables of data |
| Week 6 | `python -m pip install matplotlib` | Charts |

Installing only what you need keeps your project small. Check that the name is spelled exactly as shown before you press Enter.

## Data Sets

Every data file in this course is **synthetic**. It was made for the course, and it contains no real logs and no personal information. The internet addresses in the logs come from ranges reserved for examples, so they belong to nobody.

| File | Used in | What it holds |
|---|---|---|
| [sample_text.txt](files/sample_text.txt) | Week 1 | A short passage, "The Quiet Server Room" |
| [web_log.txt](files/web_log.txt) | Week 2 | 200 web-server log lines over two days |
| [common_passwords.txt](files/common_passwords.txt) | Week 3 | 50 common passwords, one on each line |
| [login_counts.csv](data/login_counts.csv) | Week 4 | Daily login counts for six users over 28 days |
| [web_log.csv](data/web_log.csv) | Week 5 | The same 200 log records as a CSV file |
| [login_attempts.csv](data/login_attempts.csv) | Week 6 | Capstone option A: login attempts over two weeks |
| [sales.csv](data/sales.csv) | Week 6 | Capstone option B: three months of sales for an invented shop |
