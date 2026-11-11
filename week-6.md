---
title: 'Week 6: Charts and capstone'
teaching: 94
exercises: 226
---

:::::::::::::::::::::::::::::::::::::: questions

- What will I learn in Week 6, and how should I spend my 6 hours?
- How do I draw a chart that shows change over time?
- Which chart suits which question?
- How do I go from a question to a chart and a finding?
- How can a chart mislead without a wrong number?
- Can I take a dataset from a question to two honest charts and a finding?

::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::: objectives

- Plan your study time for the week using the time plan.
- Make a figure and axes with plt.subplots.
- Add a title, axis labels with units and a legend.
- Save a chart as a PNG file.
- Draw bar charts and histograms.
- Choose between a line chart, a bar chart and a histogram.
- Follow the steps from question to chart to written finding.
- Write one sentence that says what a chart shows, with a real number.
- Spot the common ways a chart misleads.
- Use a checklist to make a chart honest.
- Choose a dataset, draw two charts and write a short finding.

::::::::::::::::::::::::::::::::::::::::::::::::

## Week 6 overview {#week-6-overview}

**Theme:** draw line charts, bar charts and histograms with Matplotlib, choose the chart that suits a question, make sure a chart is honest, and finish the course with a capstone of two charts and a written finding.

This is the last week of Part 2.

**What you need from earlier weeks:** Pandas from Week 5 (`read_csv`, filtering, `groupby`, missing values), your project's virtual environment and pip from Week 4, and Python basics from Part 1 (functions, dictionaries, loops, tests with pytest).

### Learning goals

By the end of this week you can:

1. Draw a line chart, a bar chart and a histogram with Matplotlib, with a title, axis labels with units and readable tick labels, and save the chart as a PNG file.
2. Choose the chart type and the method that suit a question, and explain why (LO 4).
3. Spot a misleading chart, and make your own charts honest.
4. Take a dataset from a question to two charts and a short written finding, using Pandas and Matplotlib together (LO 1 and LO 3).

### Time plan (under 6 hours)

| Block | Time | What you do |
|---|---|---|
| Watch | 20 min | Two videos (below) |
| Read & practise | 1 h 30 m | Sections 6.1 (35 min), 6.2 (30 min) and 6.3 (25 min), with Level 1 exercises |
| Concepts Bridge | 30 min | [Honest charts](#week-6-bridge) |
| Build | 3 h | [Capstone: two charts and a written finding](#week-6-practice), your portfolio item for this week |
| Quiz | 15 min | Canvas quiz, 6 questions |
| **Total** | **5 h 35 min** | Under the 6 h cap |

### Watch (20 min)

Watch in this order. Pause and try things in PyCharm as you go.

| # | Video | Length | Look out for | Link |
|---|---|---|---|---|
| 1 | Line and bar charts with Matplotlib | 12 min (planned) | How `plt.subplots()` makes the figure and axes. How to add a title and labels. | To be sourced and checked |
| 2 | Honest and misleading charts | 8 min (planned) | How an axis that does not start at zero changes the impression. | To be sourced and checked |

### Read & practise (1 h 30 m)

Open the lesson, read it, type out the examples and run them. Do not just copy and paste. The saved code for each section is in its `_code` folder. The saved files write a PNG next to the script. In your own code, `plt.show()` opens a window in PyCharm.

#### Section 6.1: Line charts with Matplotlib (35 min)

Lesson: [Section 6.1](#section-6-1). Code: [lessons/6.1_code/](files/code/6.1/).

- Read all of it. Install Matplotlib in your project's virtual environment first.
- Do the **Level 1** exercises (1 to 6).

#### Section 6.2: Bar charts and histograms (30 min)

Lesson: [Section 6.2](#section-6-2). Code: [lessons/6.2_code/](files/code/6.2/).

- Read all of it. Keep the decision table (which chart for which question) open for the Build.
- Do the **Level 1** exercises (1 to 6).

#### Section 6.3: Building a chart that answers a question (25 min)

Lesson: [Section 6.3](#section-6-3). Code: [lessons/6.3_code/](files/code/6.3/).

- Read all of it. This is the method you will use in the Build.
- Do the **Level 1** exercises (1 to 6).

**PyCharm note:** if a chart window opens and the program seems stuck, close the window. The program waits for you.

### Concepts Bridge (30 min)

Go to [bridge.md](#week-6-bridge). It shows how a chart can mislead without any wrong number, gives you a checklist for an honest chart, and explains why the person who makes a chart is responsible for the impression it gives. Code for the bridge is in [bridge_code/](files/code/bridge-6/).

### Build (3 h)

Go to [practice/README.md](#week-6-practice). You choose one of two datasets (login attempts, or sales), answer a question with Pandas, draw two charts, and write a short finding. Install pandas, matplotlib and pytest in your project's virtual environment before you start. This is your portfolio item for Week 6.

### Quiz (15 min)

Take the Canvas quiz for Week 6 after you finish the Build. It has 6 questions, drawn from a pool. It is marked automatically.

### Portfolio this week

Submit at the end of the week, in your portfolio folder:

- `starter.py` (completed for the one option you chose)
- `chart1.png`
- `chart2.png`
- `finding.txt` (150 to 250 words)

Your tutor marks the portfolio. The quiz is marked automatically.

### Optional

Only if you have time and are curious.

- Sections 6.1, 6.2 and 6.3 Level 2 exercises.
- Try the other capstone option. Make two charts for it as well.
- Matplotlib Development Team (2026) *Matplotlib documentation*. Available at: https://matplotlib.org/stable/ (Accessed: 11 November 2026).
- The Pandas Development Team (2026) *pandas documentation*. Available at: https://pandas.pydata.org/docs/ (Accessed: 11 November 2026).

---

### Finishing the course

You have now finished both parts of the course. In Part 1 you learned to write Python programs with variables, decisions, loops, functions, classes and modules, and to test them. In Part 2 you learned to work with text, files and logs, to check data and to hash it, and to use NumPy and Pandas to summarise it. This week you added Matplotlib, so you can turn a table into a chart that answers a question, judge whether a chart is honest, and write a short, careful finding with its limits.

## 6.1 Line charts with Matplotlib {#section-6-1}

1. Why draw a chart?
2. Install Matplotlib
3. Your first line chart
4. Figure and axes
5. Title, labels and units
6. Show it, or save it
7. Plot a Pandas Series from `groupby`
8. Dates, tilted labels and a legend
9. Common mistakes
10. Exercises

---

### 1. Why draw a chart?

A table of 563 login attempts is hard to read. A chart can show in a second that one day is very different from the rest. Analysts in data and security roles use charts to **find** a pattern and to **show** it to other people.

A **line chart** joins points with a line. Use it when the horizontal axis is time, or any ordered scale, and you want to see how a number **changes**.

**Matplotlib** is the Python library that draws charts. It works well with the Pandas you used in Week 5.

### 2. Install Matplotlib

Open the **Terminal** tab in PyCharm. Check that the name of your project's virtual environment shows in brackets at the start of the line. This is the environment you made in Week 4. Then type:

```output
python -m pip install matplotlib
```

When it finishes, check it with:

```output
python -c "import matplotlib; print(matplotlib.__version__)"
```

You should see a version number such as `3.11.2`. Yours may be different, and that is fine.

### 3. Your first line chart

Every Matplotlib program starts with the same import. The name `plt` is a short nickname that almost everyone uses.

**Example: Help desk tickets**

```python
import matplotlib.pyplot as plt

days = ["Mon", "Tue", "Wed", "Thu", "Fri"]
tickets = [12, 15, 9, 20, 14]

fig, ax = plt.subplots()
ax.plot(days, tickets, marker="o")
ax.set_title("Help desk tickets this week")
ax.set_xlabel("Day of the week")
ax.set_ylabel("Tickets opened (count)")
plt.show()
```

Run it in PyCharm. `plt.show()` **opens a window** with the chart. Close the window to let the program end.

📷 Image placeholder: episodes/fig/first_line_chart.png — a line chart with five round dots joined by a line. The title is "Help desk tickets this week". The line rises from 12 to 15, falls to 9, climbs to 20 on Thursday, then falls to 14.

The saved code for this section, in [6.1_code](files/code/6.1/), uses a different last step. It saves the chart to a PNG file instead of opening a window. That way it also runs on a computer with no screen. You will see how below.

### 4. Figure and axes

The line `fig, ax = plt.subplots()` makes two things:

| Name | What it is | Think of it as |
|---|---|---|
| `fig` | The **figure**: the whole picture, including its size and its margins. | The sheet of paper |
| `ax` | The **axes**: the area where the data is drawn, with its two number lines. | The graph drawn on the paper |

Almost every command you use starts with `ax.` (draw or label something on the graph) or `fig.` (change the whole sheet, or save it).

`plt.subplots()` gives back two values in one go. Python assigns them to `fig` and `ax`, in that order. This works the same way as `a, b = 1, 2`.

To make the sheet bigger, give a size in inches:

```python
fig, ax = plt.subplots(figsize=(9, 5))
```

The first number is the width and the second is the height.

### 5. Title, labels and units

A chart without labels is a puzzle. Always add three things:

| Command | What it adds |
|---|---|
| `ax.set_title("...")` | A title that says what the chart is about |
| `ax.set_xlabel("...")` | A label under the horizontal axis |
| `ax.set_ylabel("...")` | A label beside the vertical axis |

Put the **unit** in the label. "Tickets opened (count)" is better than "Tickets". "Revenue ($)" is better than "Revenue". "Response size (bytes)" is better than "Size". Week 6's bridge explains why this matters.

Two other options you will use:

- `marker="o"` puts a round dot on every data point, so readers can see where the real values are.
- `ax.set_ylim(bottom=0)` makes the vertical axis start at zero. You will use it on the capstone.

### 6. Show it, or save it

| Command | What it does |
|---|---|
| `plt.show()` | Opens a window with the chart. In PyCharm, close the window to continue. |
| `fig.savefig("name.png", dpi=150)` | Writes the chart to a PNG image file. `dpi=150` makes it sharp enough for a report. |
| `plt.close(fig)` | Frees the memory used by the chart when you have finished with it. |

Matplotlib saves the file in the **current working folder** unless you give a full path. The saved code uses `Path(__file__)` to put the PNG next to the script:

```python
from pathlib import Path

HERE = Path(__file__).resolve().parent   # the folder this file is in
fig.savefig(HERE / "first_line_chart.png", dpi=150)
```

`pathlib.Path` is a tool for file paths. Week 2 explained it. The `/` joins a folder and a file name.

Call `savefig` **before** `plt.show()`. When you close the window, `show` clears the chart, and a later `savefig` would save a blank picture.

At the top of the saved code files you will also see two lines:

```python
import matplotlib
matplotlib.use("Agg")
```

This tells Matplotlib to draw into files only. Do not add it to programs where you want `plt.show()` to open a window.

Now run `first_line_chart.py` in the `6.1_code` folder. It prints:

```output
Saved first_line_chart.png
```

A file called `first_line_chart.png` appears next to the script. Open it in PyCharm to look at it. You can delete it afterwards.

### 7. Plot a Pandas Series from `groupby`

In Week 5 you learned that `groupby` followed by `.size()` gives a **Series**: a column of values with a label (the **index**) for each one. A Series is ready to plot. Use `.index` for the x values and `.values` for the y values.

**Example: Web requests per hour**

```python
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("assets/data/web_log.csv")
df["hour"] = df["time"].str[:2].astype(int)    # "07:13:45" gives 7

per_hour = df.groupby("hour").size()
print(per_hour.head())

fig, ax = plt.subplots(figsize=(9, 5))
ax.plot(per_hour.index, per_hour.values, marker="o")
ax.set_title("Web requests per hour of the day")
ax.set_xlabel("Hour of the day (24-hour clock)")
ax.set_ylabel("Requests (count)")
ax.set_ylim(bottom=0)
fig.tight_layout()
fig.savefig("requests_per_hour.png", dpi=150)
plt.close(fig)
```

The first lines of output are:

```output
hour
2     22
7      6
8     15
9     14
10     8
dtype: int64
```

Hour 2 (2 am) has 22 requests. That is a lot for the middle of the night. It is the burst of failed logins in the web log that you looked at in Week 5.

`str[:2]` takes the first two characters of the time text. `fig.tight_layout()` adjusts the margins so that labels are not cut off. The file is `line_from_groupby.py`.

📷 Image placeholder: episodes/fig/requests_per_hour.png — a line chart with a high point at hour 2 (22 requests), a long straight stretch to hour 7 (6 requests), then a line that rises and falls with peaks of 23 requests at hours 11 and 15, and ends at hour 23 with 10.

**Check the picture against the numbers.** A chart is only as good as the code that made it. Here the table says hour 2 has 22, and the chart shows a high point at hour 2. They match.

Notice that hours 3 to 6 are missing from the Series, because there were no requests. Matplotlib joins hour 2 straight to hour 7 with a line, which can look like a steady change when nothing was recorded in between. This is one small way a chart can mislead. In the capstone you will fill in missing days with 0.

### 8. Dates, tilted labels and a legend

When the x values are dates, the labels are long and run into each other. Two fixes:

- `fig.autofmt_xdate()` tilts the labels so they fit.
- `ax.set_xticks(...)` chooses which labels to show.

If you draw more than one line, give each line a `label=` and call `ax.legend()`. The **legend** is the small box that says which line is which.

**Example: Two users**

```python
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("assets/data/login_counts.csv")
print(df[["date", "user01", "user04"]].head(3))

fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(df["date"], df["user01"], label="user01")
ax.plot(df["date"], df["user04"], label="user04")
ax.set_title("Daily logins for two users")
ax.set_xlabel("Date")
ax.set_ylabel("Logins (count)")
ax.legend()
ax.set_xticks(df["date"][::3])      # show every third date only
fig.autofmt_xdate()
fig.tight_layout()
fig.savefig("two_users.png", dpi=150)
plt.close(fig)
```

```output
         date  user01  user04
0  2026-10-05       4       6
1  2026-10-06       5       9
2  2026-10-07       5       7
```

`df["date"][::3]` takes every third item (a slice with a step of 3, as in Week 1). The file is `line_with_dates.py`.

📷 Image placeholder: episodes/fig/two_users.png — two lines. user01 stays between 2 and 6. user04 stays between 6 and 10 except for one tall spike to 41 on 2026-10-21. A legend in the corner names the two lines. The date labels are tilted.

Here the dates are plain text such as `"2026-10-05"`, and Matplotlib treats each as a separate category in order. That works because the rows are already in date order and there are no gaps. If a day were missing, the spacing would be wrong. Always check that every day is present.

### 9. Common mistakes

- **Forgetting `plt.close(fig)`.** In a program that draws many charts, the memory fills up and Matplotlib warns you.
- **Calling `savefig` after `plt.show()`.** The file is blank. Save first.
- **No units in the labels.** A reader cannot tell whether "50" means dollars, bytes or people.
- **Overlapping date labels.** Use `fig.autofmt_xdate()`.
- **Plotting a whole DataFrame by accident.** Choose the two columns or the Series you mean.
- **A line across a gap.** A line suggests the values in between. If days are missing, add them with the value 0, or use a different chart.
- **Running a saved code file and expecting a window.** Those files use `Agg` and only write a PNG.

---

::::::::::::::::::::::::::::::::::::: challenge

### Exercises: Level 1

1. Install Matplotlib in your project's virtual environment and print its version.
2. Type out the help desk chart from section 3 and run it with `plt.show()`. Change the numbers in `tickets` and run it again.
3. Add `ax.set_ylim(bottom=0)` to your chart. What changes?
4. Change `plt.show()` to `fig.savefig("tickets.png", dpi=150)`. Run it, find the file, and open it.
5. In the web log example, change the last line of the chart so the title says "Web requests per hour, 9 and 10 November 2026". Add the unit "(count)" if it is not there.
6. Draw `user02` and `user03` from `login_counts.csv` on one chart with a legend. Which user has the bigger spike, and on which date? (Hint: look at the highest point and use `df["user02"].max()` to check.)

::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::: challenge

### Exercises: Level 2

1. Use `groupby("date").size()` on `web_log.csv` to count requests per day. Draw it as a line chart. Why is a line not a good choice for only two points?
2. Add `ax.grid(True)` to a chart. Does it help the reader, or does it add clutter?
3. Make the line for `user04` red with `color="red"` and the line for `user01` dashed with `linestyle="--"`. Why might you not want to rely on colour alone?

::::::::::::::::::::::::::::::::::::::::::::::::

## 6.2 Bar charts and histograms {#section-6-2}

1. Why different charts?
2. Bar charts with `ax.bar`
3. Horizontal bars with `ax.barh`
4. Sort your bars
5. Histograms with `ax.hist`
6. What are bins?
7. Which chart should I use?
8. Common mistakes
9. Exercises

---

### 1. Why different charts?

A line chart answers "how did it change?". Two other questions come up all the time in data and security work:

- "Which one is biggest?" Which user, which IP address, which page, which region? That needs a **bar chart**.
- "How are the values spread out?" Are most responses small, with a few huge ones? That needs a **histogram**.

Choosing the chart that suits the question is part of the job. The wrong chart can hide the answer, or give a wrong impression.

### 2. Bar charts with `ax.bar`

A **bar chart** draws one bar for each **category** (a named group, such as a status code). The height of the bar is the value. You use it to **compare** categories.

**Example: Requests by status code**

```python
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("assets/data/web_log.csv")

by_status = df.groupby("status").size()
print(by_status)

fig, ax = plt.subplots()
ax.bar(by_status.index.astype(str), by_status.values)
ax.set_title("Web requests by status code")
ax.set_xlabel("Status code")
ax.set_ylabel("Requests (count)")
fig.tight_layout()
plt.show()
```

`plt.show()` opens a window in PyCharm. The saved version, `bar_charts.py` in [6.2_code](files/code/6.2/), saves a PNG instead. The numbers printed are:

```output
status
200    143
304     12
401     27
404     16
500      2
dtype: int64
```

The status codes are numbers, but here they are names of groups, so `.astype(str)` turns them into text. Without it, Matplotlib may place the bars as if the codes were on a number line.

📷 Image placeholder: episodes/fig/status_bars.png — five vertical bars labelled 200, 304, 401, 404 and 500. The 200 bar is by far the tallest at 143. The 401 bar is 27, the 404 bar is 16, the 304 bar is 12 and the 500 bar is 2.

**Bars must start at zero.** The height of a bar is how much there is. If the axis starts at 100, a bar of 143 looks as if it were only a little bigger than nothing, and it is hard to compare. `ax.bar` starts at zero by default. Do not change that. The bridge this week explains why.

### 3. Horizontal bars with `ax.barh`

Long labels, such as page names, do not fit under vertical bars. They overlap or have to be tilted. Turn the chart on its side with `ax.barh` (the "h" is for horizontal). The labels then sit on the left, where there is room.

**Example: The five most requested pages**

```python
top_paths = df.groupby("path").size().sort_values(ascending=False).head(5)
print(top_paths)
```

```output
path
/login              34
/courses.html       25
/css/site.css       24
/about.html         22
/images/logo.png    21
dtype: int64
```

`sort_values(ascending=False)` puts the largest first, and `.head(5)` keeps the first five (Week 5).

`barh` draws the **first** item at the **bottom**. To get the largest at the top, sort the other way before you draw:

```python
top_paths = top_paths.sort_values()      # smallest first

fig, ax = plt.subplots(figsize=(8, 4))
ax.barh(top_paths.index, top_paths.values)
ax.set_title("Five most requested pages")
ax.set_xlabel("Requests (count)")        # note: the NUMBER axis is now x
ax.set_ylabel("Page")
fig.tight_layout()
```

With `barh`, the number axis is the **horizontal** one. So the unit goes in `set_xlabel`, and the category name goes in `set_ylabel`.

📷 Image placeholder: episodes/fig/top_pages.png — five horizontal bars. The longest, "/login" at 34, is at the top. Below it are "/courses.html" (25), "/css/site.css" (24), "/about.html" (22) and "/images/logo.png" (21).

### 4. Sort your bars

Bars in a random order make the reader work. Sort them by size, biggest first, unless the categories have a natural order. Months and days of the week have one, so keep it: January, February, March.

Status codes also have a natural order, so the bars in section 2 are in code order. The pages are not ordered, so they are sorted by size.

A sorted bar chart answers "which is biggest?" at a glance.

### 5. Histograms with `ax.hist`

A **histogram** shows the **distribution** of one numeric column: how the values are spread out. It does not compare named categories. It answers questions such as "Are most responses small?" and "Is there a long tail of huge ones?"

**Example: How big are the responses?**

```python
sizes = df["size"].dropna()          # 12 rows have no size
print("Sizes with a value:", len(sizes))
print("Smallest:", sizes.min(), "Largest:", sizes.max())

fig, ax = plt.subplots()
ax.hist(sizes, bins=5)
ax.set_title("Size of web responses")
ax.set_xlabel("Response size (bytes)")
ax.set_ylabel("Requests (count)")
plt.show()
```

```output
Sizes with a value: 188
Smallest: 318.0 Largest: 18240.0
```

`dropna()` removes the missing values (Week 5). A histogram cannot draw an empty cell.

### 6. What are bins?

A histogram works in three steps:

1. It finds the smallest and largest value (here 318 and 18240).
2. It cuts that range into equal-width slices called **bins**.
3. It counts how many values fall in each bin and draws a bar for each.

`bins=5` makes five bins. Each is about 3,584 bytes wide. The counts for five bins are:

```output
87, 81, 0, 0, 20
```

With `bins=20` the bins are narrower, and more detail shows:

```output
45, 7, 17, 18, 24, 34, 0, 23, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 20
```

Both are correct. They show the same data at different levels of detail.

- **Too few bins** hide the shape. Everything is lumped together.
- **Too many bins** make the chart jagged and noisy.

Try several values and choose the one that shows the shape honestly. The file `histograms.py` draws both next to each other.

📷 Image placeholder: episodes/fig/size_histograms.png — two histograms side by side. The left one has 5 bars: two tall bars (87 and 81) on the left, an empty gap, and a short bar (20) at the far right. The right one has 20 narrower bars, with a cluster on the left, many empty bins in the middle and right, and one bar of 20 at the far right.

Notice that the bars of a histogram touch. That is because the x axis is a continuous number line, not separate categories. The gap in the middle means no response had a size in that range. The group at the far right is the 20 responses of the largest size.

A histogram has a bar for each **range**, so its y axis should say what is counted, such as "Requests (count)". The x axis says what was measured, with its unit.

### 7. Which chart should I use?

Start with the question, then choose.

| Your question sounds like | Chart | Matplotlib | Example |
|---|---|---|---|
| How does a number **change** over time? | Line chart | `ax.plot` | Failed logins per day |
| How do named **categories compare**? | Bar chart | `ax.bar` | Requests by status code |
| Same, but the labels are long? | Horizontal bar chart | `ax.barh` | Most requested pages |
| How is **one numeric column spread** out? | Histogram | `ax.hist` | Size of each response |

Three quick tests:

- Is the horizontal axis **time** (an ordered scale)? Think line.
- Is the horizontal axis a **list of names**? Think bar.
- Is there **one list of numbers** with no names or dates? Think histogram.

### 8. Common mistakes

- **A bar chart that does not start at zero.** It exaggerates the differences.
- **A line chart for categories.** A line between "Perth" and "Fremantle" suggests something in between. There is nothing between them.
- **A histogram of a column with missing values.** Use `dropna()` first.
- **Only one bin count.** Try two or three and compare.
- **Unsorted bars.** Sort by value unless the categories have a natural order.
- **`barh` with the largest at the bottom.** Sort smallest first.
- **Forgetting that `barh` swaps the axes.** The unit goes on the x label.
- **Using a histogram when you meant a bar chart.** A histogram counts how many values fall in each range. A bar chart compares values you have already added up.

---

::::::::::::::::::::::::::::::::::::: challenge

### Exercises: Level 1

1. Draw the status code bar chart from section 2. Change the title to include the dates covered (9 and 10 November 2026).
2. Count requests by `method` (use `groupby("method").size()`). Which chart do you choose, and why? Draw it.
3. Draw the five most requested pages as `barh`, largest at the top. Check that your top bar is `/login`.
4. Draw the histogram of `size` with `bins=5`, then `bins=20`. Write one sentence on what the 20-bin version shows that the 5-bin one hides.
5. Add `bins=10` as a third try. Which of the three bin counts would you show to a manager, and why?
6. In your own words, complete this sentence: "I would use a bar chart when ... and a histogram when ..."

::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::: challenge

### Exercises: Level 2

1. Count the failed logins in `web_log.csv` (status 401) by `ip`. Draw the top five as a horizontal bar chart. Which address stands out?
2. Draw the histogram for only the responses with status 200. Does the shape change?
3. Find out what `ax.hist(sizes, bins=[0, 2000, 4000, 20000])` does. Why might unequal bins be hard for a reader to interpret?

::::::::::::::::::::::::::::::::::::::::::::::::

## 6.3 Building a chart that answers a question {#section-6-3}

1. Start with a question
2. The six steps
3. A worked example
4. The sentence that finishes the chart
5. A second question, a second chart
6. Common mistakes
7. Exercises

---

### 1. Start with a question

Beginners often open a file and draw a chart of whatever is easy. The result may look nice and say nothing. Analysts do it the other way round. They start with a **question**, and the chart is the answer.

- A security analyst asks: "Did failed logins change on any day?"
- A data analyst asks: "Which region sells the most?"

A good question names what you want to know and is small enough for one chart. "What is in the data?" is too big. "Which month had the most closed tickets?" is just right.

### 2. The six steps

| Step | What you do | Tool you already know |
|---|---|---|
| 1. Question | Write it as a sentence. | Your own words |
| 2. Data and chart type | Choose the columns, then the chart from the table in Section 6.2. | Decision table |
| 3. Clean | Deal with missing values and wrong types. Note what you did. | `dropna`, `astype` |
| 4. Summarise | Turn many rows into a few numbers. | `groupby`, `.sum()`, `.size()` |
| 5. Plot and label | Draw it. Add a title, axis labels with units, readable ticks. | Matplotlib |
| 6. Say it | Write one sentence about what the chart shows, with a number. | Plain English |

Keep the steps in this order. Writing the sentence last is important: you read it off the finished chart, not the other way round.

### 3. A worked example

The data below is a tiny help desk table made by hand. It is **not** the data for your capstone. The capstone is your own work.

**Step 1: Question.** "Which month had the most tickets closed, and which team closed the most?"

**Step 2: Data and chart type.** The columns `month` and `closed` give the first answer. "How do months compare?" suggests a bar chart. Months have a natural order, so we keep it (January, February, March).

**Steps 3 to 5: Clean, summarise, plot.**

```python
import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame({
    "month":  ["Jan", "Jan", "Feb", "Feb", "Mar", "Mar", "Mar", "Feb"],
    "team":   ["Network", "Desk", "Network", "Desk", "Network", "Desk", "Desk", "Desk"],
    "closed": [20, 35, 25, 30, None, 50, 20, 5],
})
print("Rows:", len(df))
print("Missing closed:", df["closed"].isna().sum())

# Clean: drop the row with no number, and say so.
clean = df.dropna(subset=["closed"]).copy()
print("Rows after cleaning:", len(clean))

# Summarise.
by_month = clean.groupby("month")["closed"].sum()
by_month = by_month.reindex(["Jan", "Feb", "Mar"])     # calendar order
print(by_month)

# Plot.
fig, ax = plt.subplots()
ax.bar(by_month.index, by_month.values)
ax.set_title("Tickets closed per month")
ax.set_xlabel("Month (2026)")
ax.set_ylabel("Tickets closed (count)")
fig.tight_layout()
plt.show()
```

The output is:

```output
Rows: 8
Missing closed: 1
Rows after cleaning: 7
month
Jan    55.0
Feb    60.0
Mar    70.0
Name: closed, dtype: float64
```

Go through what each part does.

- **Clean.** One row has `None` in `closed`. We do not know how many tickets that team closed, so we drop the row. This is a choice. We write it down, because it changes the answer. `.copy()` makes a separate DataFrame so we do not change `df`.
- **Summarise.** `groupby("month")` followed by `["closed"].sum()` adds up the tickets for each month. `groupby` puts the months in alphabetical order (Feb, Jan, Mar), which is wrong for time. `reindex(["Jan", "Feb", "Mar"])` puts them back in calendar order.
- **Plot.** A bar chart, with a title, labels and units. The bars start at zero because we did not change the axis.

The numbers are floats (`55.0`) because the missing value made Pandas store the column as decimals. The saved code in [6.3_code](files/code/6.3/) is `worked_example.py`. It saves a PNG instead of calling `plt.show()`.

📷 Image placeholder: episodes/fig/tickets_per_month.png — three bars labelled Jan, Feb and Mar, with heights 55, 60 and 70. The bars rise a little each month. The y axis starts at 0. The title is "Tickets closed per month".

### 4. The sentence that finishes the chart

**Step 6.** Read the chart and write one sentence with a real number in it:

> March had the most closed tickets, with 70, up from 55 in January.

You can ask Python for the winner instead of reading it by eye, so you do not make a mistake:

```python
best = by_month.idxmax()      # the label of the biggest value
print(f"{best} had the most closed tickets, with {int(by_month[best])}.")
```

```output
Mar had the most closed tickets, with 70.
```

A good sentence:

- says what the chart shows, not what you hoped,
- includes at least one actual number,
- does not say more than the data can support. "Tickets closed rose from January to March" is fine. "The team is getting better" is not, because the chart cannot show that. The numbers might rise because more tickets arrived.

### 5. A second question, a second chart

The second part of the question was "which team closed the most?". Now the categories are teams and the question is a comparison, so a bar chart again. Teams have no natural order, so we sort by size.

```python
by_team = clean.groupby("team")["closed"].sum().sort_values(ascending=False)
print(by_team)

fig, ax = plt.subplots()
ax.bar(by_team.index, by_team.values)
ax.set_title("Tickets closed per team, January to March")
ax.set_xlabel("Team")
ax.set_ylabel("Tickets closed (count)")
fig.tight_layout()
```

```output
team
Desk       140.0
Network     45.0
Name: closed, dtype: float64
```

The sentence: "The Desk team closed 140 tickets and the Network team closed 45."

**A limit worth noting.** Does this mean the Desk team works harder? We cannot tell. The Desk team has five of the seven rows left. It may simply be a bigger team, or handle a different type of ticket. Comparing totals can be unfair when the groups differ in size. The bridge this week returns to this idea. A good analyst states the limit next to the finding.

This file is `team_chart.py`.

📷 Image placeholder: episodes/fig/tickets_per_team.png — two bars. "Desk" is much taller (140) than "Network" (45). The y axis starts at 0.

### 6. Common mistakes

- **Drawing before asking.** Write the question first.
- **Cleaning without noting it.** If you drop six rows, say so. The reader needs to know.
- **Wrong order.** `groupby` sorts text alphabetically. Months and days need `reindex`.
- **A sentence with no number.** "Sales went up" is weak. "Sales went up from $2,100 to $3,400" is strong.
- **A sentence that claims too much.** Say what the chart shows. Do not claim a cause.
- **Checking the chart but not the numbers.** Print the summary before you plot it. Check that the chart agrees with it.
- **Forgetting the unit or title** on a chart that is "just for you". Charts get shared.

---

::::::::::::::::::::::::::::::::::::: challenge

### Exercises: Level 1

1. Run `worked_example.py` in PyCharm (change the last chart step to `plt.show()` if you want to see the window). Does the output match the lesson?
2. Change the `None` to `15` in the `closed` list and run it again. What are the new month totals? What does that tell you about how much one missing row can matter?
3. Write the six steps from the table in your own words, one short line each.
4. For each question, name the chart type you would choose: (a) "How did failed logins change over two weeks?" (b) "Which user has the most logins?" (c) "How are login counts spread across all users?"
5. Using `login_counts.csv`, ask the question "Which user had the most logins in total?" Summarise with `df.drop(columns="date").sum()`, sort the result, draw it as a bar chart with labels and units, and write the one-sentence answer with a number.
6. A classmate's chart sentence says: "Sales are improving because customers like us." Rewrite it so that it only says what a chart of monthly sales could show.

::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::: challenge

### Exercises: Level 2

1. Plot the total logins per day (add up the six user columns) as a line chart. Write one sentence.
2. In the worked example, fill the missing value with the average of the other `closed` values instead of dropping the row. Does the answer to the question change? Which choice would you defend, and why?

::::::::::::::::::::::::::::::::::::::::::::::::

## Concepts Bridge: Honest Charts {#week-6-bridge}

**Time: 30 minutes.** Reading 12 minutes, running the code 5 minutes, activities 8 minutes, checking the model answer 5 minutes.

### Why this matters

A chart can mislead without a single wrong number. Every bar can be the right height and the picture can still tell the wrong story. The person who makes a chart is responsible for the **impression** it gives, not only for the numbers behind it.

This is about ethics and professional responsibility. Analysts in data and security roles are trusted to report what the data shows. Managers, clients and customers cannot check every row, so they rely on the chart and on the person who drew it. That includes the times when the data does **not** support what someone hoped to hear. A chart that was drawn to please is a betrayal of that trust, even if no number was changed.

This also links to Week 5's bridge. Data about people deserves care, and so does the way you present it.

### Six ways a chart misleads

| Problem | What happens | The fix |
|---|---|---|
| **Bars that do not start at zero** | A small difference looks huge. The bar heights no longer match the sizes. | Start bar charts at zero. |
| **A stretched or squashed axis** | A tall, narrow chart makes a rise look steep. A wide, flat one makes it look like nothing. | Use a normal shape and a sensible range. Show the full data. |
| **Cherry-picked dates** | Starting a line chart at the lowest point makes a "rise". Stopping before a drop hides it. | Show the whole period you have. Say why if you cut it. |
| **Missing labels or units** | The reader guesses: dollars or thousands of dollars? Count or per cent? | Title, axis labels with units, a legend if there is more than one line. |
| **Too many colours or 3-D effects** | Decoration pulls the eye away from the data. 3-D bars distort the heights. | Use one colour unless colour carries meaning. Keep it flat. |
| **Totals when rates are fairer** | A big group has bigger totals just because it is big. | Compare per person, per computer or per cent when group sizes differ. |

**Example: Totals against rates.** Team A has 1,000 computers and reported 30 incidents. Team B has 200 computers and reported 20 incidents. A bar chart of totals says Team A has more trouble (30 against 20). The rates say something different: Team A had 3 incidents per 100 computers, and Team B had 10 per 100. Team B has more trouble for its size. Neither chart is "wrong", but they give opposite impressions. Choose the one that answers the real question, and say which you used.

### See it in code

The same three values, drawn twice. The only difference is `ax.set_ylim(bottom=...)`, which sets where the vertical axis starts. The code is in [bridge_code/axis_pair.py](files/code/bridge-6/axis_pair.py).

```python
import matplotlib.pyplot as plt

teams = ["Team A", "Team B", "Team C"]
patched = [96, 97, 98]      # per cent of computers patched

fig, (left, right) = plt.subplots(1, 2, figsize=(10, 4))

left.bar(teams, patched)
left.set_ylim(bottom=95)
left.set_title("Axis starts at 95")
left.set_ylabel("Computers patched (%)")

right.bar(teams, patched)
right.set_ylim(bottom=0)
right.set_title("Axis starts at 0")
right.set_ylabel("Computers patched (%)")

fig.tight_layout()
plt.show()
```

`plt.subplots(1, 2)` makes one figure with two sets of axes side by side. Run it in PyCharm (the saved file writes a PNG instead).

📷 Image placeholder: episodes/fig/axis_pair.png — two bar charts side by side with the same three values (96, 97, 98). On the left, the axis starts at 95, so Team A's bar is tiny, Team B's is about twice as tall, and Team C's is three times as tall. On the right, the axis starts at 0, and the three bars look almost the same height.

Look at both. What impression does each give?

- **Left (axis from 95):** Team C looks three times better than Team A. It looks like a big gap.
- **Right (axis from 0):** the three teams are nearly the same. This matches the numbers, which differ by only two percentage points.

The truncated chart is not "lying" about any value. It lies about how **big the difference matters**.

A fair exception: a **line chart** may start above zero when the change is what matters and the story is clearly labelled. A line shows position, not the size of a bar. Even so, the axis range should be shown and fair, and never chosen to make the difference look bigger.

### A checklist for an honest chart

Before you share a chart, ask:

- [ ] Does it have a title that says what it shows?
- [ ] Are both axes labelled, with units?
- [ ] Do bars start at zero?
- [ ] Is the shape normal, not stretched or squashed?
- [ ] Does it show the whole period, not just a favourable part?
- [ ] Are group sizes fair, or should I show a rate?
- [ ] Is there only as much colour as is needed, and no 3-D?
- [ ] Can every label be read?
- [ ] Does my caption say what the chart shows, and nothing more?
- [ ] Would I be comfortable if the reader saw the data behind it?

::::::::::::::::::::::::::::::::::::: challenge

### Activity 1: three problems in a described chart (4 minutes)

A report has a bar chart titled "Our security training works!". It has two bars, "Before training" and "After training". The vertical axis has no label and runs from 40 to 44. The "Before" bar is at 41 and the "After" bar is at 43. The bars are bright red and green and drawn in 3-D.

Find **three** problems. For each, name the fix.

### Activity 2: rewrite a misleading caption (4 minutes)

Here is the caption under a line chart of failed logins per day for one week:

> "Failed logins are skyrocketing, proving we are under attack."

The chart starts on the quietest day of the month and the y axis runs from 0 to 8. The numbers are 1, 2, 3, 5, 4, 6, 7. Rewrite the caption so that it says only what the data shows, and add one limit.

:::::::::::::::: solution

### Model answer

**Activity 1.** Any three of these:

1. The axis starts at 40, not zero. The bars exaggerate a small difference. Fix: start at zero.
2. The y axis has no label or unit, so a reader does not know what is measured (a score? per cent?). Fix: label it with the unit.
3. 3-D effects distort bar heights. Fix: flat bars.
4. Bright red and green add meaning ("bad" and "good") that the data does not prove, and are hard to read for people with colour blindness. Fix: one calm colour.
5. The title claims the training works, but two bars cannot show a cause. Fix: a neutral title such as "Average quiz score before and after training", and a note about the limit.

**Activity 2.** For example: "Failed logins rose from 1 on the first day to 7 on the last day of this week. Because the chart starts on the quietest day of the month, one week cannot show whether this is unusual. A rise is a reason to look closer, not proof of an attack." This uses real numbers, shows the period, avoids the claim about a cause, and states a limit.

:::::::::::::::::::::::::
::::::::::::::::::::::::::::::::::::::::::::::::

### Further reading

- Matplotlib Development Team (2026) *Matplotlib documentation*. Available at: https://matplotlib.org/stable/ (Accessed: 11 November 2026).

## Practice task: Capstone, Two Charts and a Written Finding {#week-6-practice}

:::::::::::::::::::::::::::::::::::::::: callout

### Files for this task

The easiest way to get every file is the [course zip file](data/course-data.zip) from the Setup page. Unzip it and open the folder in PyCharm. The programs find the data files by their place in that folder, so keep the folder layout. You can also download single files here:

- [starter.py](files/week-6/starter.py)
- [solution.py](files/week-6/solution.py)
- [test_solution.py](files/week-6/test_solution.py)

:::::::::::::::::::::::::::::::::::::::::::::::::::

**Time: 3 hours.** This is your portfolio item for Week 6, and the last one in the course. Your tutor marks it at the end of the week.

### Goal

Choose **one** dataset. Ask a question about it. Use Pandas to summarise the data, draw **two charts** with Matplotlib, and write a short **finding** saying what you learned.

This is your own work. The lessons did not use these datasets, and this page does not tell you what the data shows. Finding that out is the task.

### Install first

Open the **Terminal** tab in PyCharm. Check that your project's virtual environment is active (its name shows in brackets at the start of the line). Then install the three libraries you need:

```output
python -m pip install pandas matplotlib pytest
```

If you already installed some in earlier weeks, pip tells you they are already there. That is fine.

### Choose one dataset

Both files are in `assets/data/`. Open both in PyCharm and look at them before you choose.

| Option | File | Columns | The kind of question |
|---|---|---|---|
| **A: Security** | `login_attempts.csv` | `date,hour,user,ip,result` | Is anything unusual in a fortnight of login attempts? `result` is `success` or `fail`. |
| **B: Data** | `sales.csv` | `date,region,product,units,unit_price` | How is a small stationery shop doing over three months? Some rows are incomplete. |

Both are synthetic. No real people or real systems are involved. The IP addresses come from ranges reserved for examples.

**Questions to investigate**

- **A:** "How do failed logins change from day to day, and where do they come from?"
- **B:** "How does revenue change over time, and how do the regions compare?"

You may add a question of your own.

### Files

| File | What it is |
|---|---|
| `starter.py` | Functions for **both** options, with TODOs. You complete the set for your option only. |
| `test_solution.py` | Tests. Tests named `test_a_...` are for option A. Tests named `test_b_...` are for option B. |
| `solution.py` | A model answer for both options. Try the task yourself before you look. |

Work in this folder (`weeks/week-6/practice`). The starter finds the datasets from where it sits, so it will not work if you move it somewhere else.

### Which functions do I write?

| Shared | `load_data(path)` returns a DataFrame |
|---|---|
| **Option A** | `fails_per_day(df)`, `fails_per_hour(df, date)`, `fails_per_ip(df, n=5)`, `chart_fails_per_day(df, path)`, `chart_fails_per_ip(df, path)` |
| **Option B** | `clean_sales(df)`, `revenue_per_month(df)`, `revenue_per_region(df)`, `chart_revenue_per_month(df, path)`, `chart_revenue_per_region(df, path)` |

The docstring of each function in `starter.py` says exactly what it must return. Leave the other option's functions as they are, with `pass`.

**Every chart function** takes the DataFrame and a `path`, saves a PNG to that path, and **returns the Figure** (`fig`). The code that calls it closes the figure with `plt.close(fig)`. The tests use the returned figure to check your title and labels.

### Steps

1. **Install and choose (15 min).** Install the libraries. Open both CSV files. Choose your option. In `starter.py`, change `OPTION = "A"` to your choice. Write your question as a sentence at the top of a new file `finding.txt`.
2. **Explore (20 min).** In a scratch file (or in the PyCharm Python console), load your file with `pd.read_csv`. Look at `df.head()`, `df.shape` and `df.dtypes`. Group the data and print what you see before you write any chart code. For option B, find out how many rows have a missing `units`. For option A, count the failed attempts for each day. Do you see anything that stands out? Write down what you notice.
3. **Data functions (40 min).** Write `load_data`, then the three data functions for your option. Option A: `fails_per_day`, `fails_per_hour`, `fails_per_ip`. Option B: `clean_sales`, `revenue_per_month`, `revenue_per_region`. Run the tests for your option after each function (see "Check your work" below).
4. **Chart 1 (25 min).** Write your first chart function: `chart_fails_per_day` (A) or `chart_revenue_per_month` (B). Both are about change over time, so a line chart suits. For B you may use a bar chart instead if you can explain why. Add a title, axis labels with units, and readable date labels. Start the vertical axis at zero.
5. **Chart 2 (20 min).** Write the second chart function: `chart_fails_per_ip` (A) or `chart_revenue_per_region` (B). These compare categories, so use a bar chart. Sort the bars and start them at zero.
6. **Written finding (30 min).** Write `finding.txt` (see below).
7. **Test and tidy (30 min).** Complete `main()`. Run the program to make `chart1.png` and `chart2.png`. Look at both pictures. Run the tests for your option. Check every item in the honest chart checklist. Remove stray TODO comments and unused code, and re-read `finding.txt`.

Times add up to 15 + 20 + 40 + 25 + 20 + 30 + 30 = **180 minutes (3 hours)**.

### What the output could look like

Your wording will differ.

```output
Rows: 563
Fails per day: {'2026-10-19': 2, '2026-10-20': 3, ...}
Busiest addresses: [('...', ...), ...]
Saved chart1.png and chart2.png in <your folder>
```

(The numbers shown are just the start of the real output. Run your code to see the rest.)

### Hints

- `df[df["result"] == "fail"]` keeps only the failed rows. Then `.groupby("date").size()` counts them (Week 5).
- A date with no fails does not appear after a `groupby`. For `fails_per_day`, build a list of **every** date with `sorted(df["date"].unique())`, then use `counts.get(date, 0)` for each one.
- `fails_per_hour` must give a plain dictionary. Use `{int(hour): int(count) for hour, count in counts.items()}`. `int(...)` turns Pandas numbers into ordinary integers.
- `fails_per_ip` returns a list of `(ip, count)` tuples. Sort with `pairs.sort(key=lambda pair: (-pair[1], pair[0]))`: biggest count first, then alphabetical order.
- `df.dropna(subset=["units"])` drops the rows where `units` is missing. Use `.copy()` so you do not change the original. Then `clean["revenue"] = clean["units"] * clean["unit_price"]`.
- The month is the first seven characters of the date: `df["date"].str[:7]` gives `"2026-07"` style text.
- Round dollar values with `round(float(total), 2)`.
- `ax.barh` draws the first item at the **bottom**. Reverse the list if you want the biggest at the top.
- `fig.autofmt_xdate()` tilts long date labels. `fig.tight_layout()` stops labels being cut off.
- `ax.set_ylim(bottom=0)` makes the vertical axis start at zero.
- Keep `print()` and file writing inside `main()`. The data functions only take values in and return values.
- If a test fails, read its message. It often says what was expected.

### Option B: your cleaning choice

Option B has six rows with a missing `units`. The model solution **drops** those rows. You may instead fill the gap with a sensible value, such as the average units for that product. Choose **one**, write what you chose in the docstring of `clean_sales`, and say why in your finding.

If you fill instead of dropping, the tests for `clean_sales` and the revenue numbers will not match the model solution, because the totals will differ. That is not a mistake. Check that your numbers follow from your rule, and mention in your finding that your totals depend on your choice.

### Your written finding

Write `finding.txt`, **150 to 250 words**, in your own words. Include:

1. **The question** you asked.
2. **What each chart shows**, with at least **two actual numbers** taken from your data.
3. **The finding in one clear sentence.**
4. **What you did to clean or prepare the data.** For option B, say how you handled the missing units. For option A, say how you made sure days with no fails still appear.
5. **One limit** of your analysis. For example: a pattern is a reason to look closer, not proof of a cause. The data is synthetic. A short period is not a trend.
6. **Which chart types you chose and why** (LO 4). Say why a line or bar suited your question better than another chart.
7. **How you made the charts honest.** Refer to the checklist in the bridge.

To count your words, type `len(open("finding.txt").read().split())` in the PyCharm Python console, or paste your text into any word counter.

### Check your work

Run only the group of tests for your option. From the top folder of the course:

```output
python -m pytest weeks/week-6/practice -k "test_a"
python -m pytest weeks/week-6/practice -k "test_b"
```

Run `test_a` if you chose option A and `test_b` if you chose option B.

To test your own file, open `test_solution.py` and change `import solution as cap` to `import starter as cap`. **The tests for the option you did not choose will fail in your copy. That is expected.** Ignore them.

In PyCharm, you can also right-click `test_solution.py` and choose **Run pytest**, then look only at the tests for your option. The tests set Matplotlib to `Agg` mode, so no chart windows open.

- [ ] All the tests for my option pass with `import starter as cap`.
- [ ] `python starter.py` runs without errors and makes `chart1.png` and `chart2.png`.
- [ ] I opened both pictures and looked at them.
- [ ] Each chart has a title, axis labels with units and readable tick labels.
- [ ] My bar chart starts at zero. My line chart's axis range is fair.
- [ ] Days with no fails (A), or missing units (B), are handled and I said how.
- [ ] `finding.txt` is 150 to 250 words and covers all seven points above.
- [ ] I wrote the finding in my own words, from my own charts.
- [ ] `OPTION` at the top of `starter.py` matches my choice.

### Portfolio files

Submit these four files:

- `starter.py` (completed for your one option)
- `chart1.png`
- `chart2.png`
- `finding.txt`

:::::::::::::::::::::::::::::::::::::: keypoints

- Each week has four blocks: Watch, Read & practise, Concepts Bridge and Build.
- Every chart needs a title and labelled axes with units.
- savefig saves the chart; show opens a window.
- Use a line chart for change over time, a bar chart to compare groups and a histogram for the spread of one measure.
- Bars should start at zero.
- Start from the question, not from the chart.
- Finish with one sentence that says what the chart shows.
- The person who makes a chart is responsible for the impression it gives.
- Start bars at zero, label axes with units and compare rates when totals would mislead.
- Choose the chart that suits the question, and make it honest.

::::::::::::::::::::::::::::::::::::::::::::::::
