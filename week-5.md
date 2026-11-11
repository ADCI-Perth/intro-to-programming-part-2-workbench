---
title: 'Week 5: Pandas'
teaching: 103
exercises: 172
---

:::::::::::::::::::::::::::::::::::::: questions

- What will I learn in Week 5, and how should I spend my 6 hours?
- How do I load a table of data into Python?
- How do I pick rows and put them in order?
- How do I summarise data by group?
- What do I do when some values are missing?
- How do I clean data honestly?
- What is personal information, and how do I handle it?
- Can I summarise a log with Pandas?

::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::: objectives

- Plan your study time for the week using the time plan.
- Read a CSV file with pd.read_csv.
- Look at a table with head, shape, dtypes and describe.
- Select columns and add a new column.
- Filter rows with a boolean mask.
- Combine conditions with & and |.
- Sort and count values.
- Group rows and count, sum or average each group.
- Sort the result and turn it back into a table.
- Find missing values with isna.
- Choose between dropping and filling, and say why.
- List common data problems and record each cleaning step.
- Explain the main ideas behind the Australian Privacy Principles in plain words.
- Write functions that answer questions about a web log, and spot two addresses that stand out.

::::::::::::::::::::::::::::::::::::::::::::::::

## Week 5 overview {#week-5-overview}

**Theme:** read a table of data into Pandas, filter and sort it, group it to find patterns, and deal with gaps and personal information in the data.

**What you need from earlier weeks:** the virtual environment from Week 4, with NumPy installed. Boolean masks from Week 4. String slicing from Week 1. Status codes and the web log format from Week 2. You do not need your own Week 2 output. This week reads the course copy, `assets/data/web_log.csv`.

### Learning goals

By the end of this week you can:

1. Read a CSV file into a Pandas DataFrame and describe it with `head`, `shape`, `dtypes`, `info()` and `describe()`.
2. Select columns, filter rows with boolean masks, and sort the result.
3. Use `groupby` to count, add up and average data for each group, and find missing values and decide what to do about them.
4. Describe common data problems and what counts as personal information, and say why you record every cleaning step.

### Time plan (under 6 hours)

| Block | Time | What you do |
|---|---|---|
| Watch | 20 min | Two videos (below) |
| Read & practise | 1 h 45 m | Sections 5.1 to 5.4, with Level 1 exercises |
| Concepts Bridge | 30 min | [Cleaning data, and handling personal information](#week-5-bridge) |
| Build | 2 h | [Web-log summary](#week-5-practice), your portfolio item for this week |
| Quiz | 15 min | Canvas quiz, 6 questions |
| **Total** | **4 h 50 min** | Under the 6 h cap |

### Watch (20 min)

Watch in this order. Pause and try things in PyCharm as you go.

| # | Video | Length | Look out for | Link |
|---|---|---|---|---|
| 1 | DataFrames and `read_csv` | 10 min (planned) | What a DataFrame and a Series are, and how a CSV file becomes a table. | To be sourced and checked |
| 2 | Filtering, sorting and `groupby` | 10 min (planned) | How a condition picks rows, and how rows are split into groups. | To be sourced and checked |

### Read & practise (1 h 45 m)

Open each lesson, read it, type out the examples and run them. Do not just copy and paste. Install Pandas in your virtual environment first: `python -m pip install pandas`.

#### Section 5.1: DataFrames and `read_csv` (35 min)

Lesson: [Section 5.1](#section-5-1). Code: [lessons/5.1_code/](files/code/5.1/).

- Read: what a DataFrame and a Series are, `read_csv`, the first-look methods, selecting columns, and making a new column.
- Do the **Level 1** exercises (1 to 6).

#### Section 5.2: Filtering and sorting (30 min)

Lesson: [Section 5.2](#section-5-2). Code: [lessons/5.2_code/](files/code/5.2/).

- Read: masks, combining conditions with `&` and `|`, `isin`, `sort_values`, `value_counts` and the `str` helper.
- Do the **Level 1** exercises (1 to 6).

#### Section 5.3: Grouping with `groupby` (25 min)

Lesson: [Section 5.3](#section-5-3). Code: [lessons/5.3_code/](files/code/5.3/).

- Read: split, apply, combine; `size` and `count`; `agg`; and `reset_index`.
- Do the **Level 1** exercises (1 to 6).

#### Section 5.4: Missing values (15 min)

Lesson: [Section 5.4](#section-5-4). Code: [lessons/5.4_code/](files/code/5.4/).

- Read: `NaN`, `isna`, `dropna`, `fillna`, and why a mean skips gaps.
- Do the **Level 1** exercises (1 to 6). They are short, so go quickly.

**PyCharm note:** keep your exercise files in the project that has your virtual environment. If PyCharm underlines `import pandas` in red, check the interpreter in the project settings is the `.venv` one.

### Concepts Bridge (30 min)

Go to [bridge.md](#week-5-bridge). Part 1 lists the common data problems and the habit of recording every cleaning step. Part 2 introduces personal information and the Australian Privacy Principles, and explains why this course uses only made-up data. There are two short activities.

### Build (2 h)

Go to [practice/README.md](#week-5-practice). You finish a Pandas web-log summary and write a short note about what it shows. This is your portfolio item for Week 5.

### Quiz (15 min)

Take the Canvas quiz for Week 5 after you finish the Build. It has 6 questions, drawn from a pool. It is marked automatically.

### Portfolio this week

Submit at the end of the week, in your portfolio folder:

- `starter.py` (your completed web-log summary)
- `log_summary.txt` (five or six sentences, see the practice task)

Your tutor marks the portfolio. The quiz is marked automatically.

### Optional

Only if you have time and are curious.

- The Level 2 exercises in each section.
- Pandas development team (2026) *pandas documentation*. Available at: https://pandas.pydata.org/docs/ (Accessed: 11 November 2026).
- Office of the Australian Information Commissioner (n.d.) *Australian Privacy Principles*. Available at: https://www.oaic.gov.au/privacy/australian-privacy-principles (Accessed: 11 November 2026).

---

## 5.1 DataFrames and read_csv {#section-5-1}

### Why Pandas

In Week 2 you read a web log with the `csv` module and loops. It worked, but every question needed a new loop. In Week 4 you used NumPy for columns of numbers. A web log has numbers and text mixed together, so NumPy is not a good fit.

**Pandas** is a library for tables of mixed data. You can ask "how many rows have status 404?" in one line. Analysts use it for sales, surveys and logs. Security teams use it to look through logs for odd patterns.

Two words to learn first:

- A **DataFrame** is a table. It has rows and named columns, like a spreadsheet.
- A **Series** is one column of a DataFrame. It has a name and a list of values.

### Install Pandas

Use the virtual environment you made in Week 4. In the PyCharm Terminal, check that you see `(.venv)` at the start of the line. Then type:

```output
python -m pip install pandas
```

Pandas needs NumPy, so pip installs NumPy too if it is missing. By convention, everyone imports Pandas with the short name `pd`:

```python
import pandas as pd
```

### A first DataFrame

We start with a tiny table made by hand. The dictionary keys become the column names. Each list becomes a column. Code: `5.1_code/first_dataframe.py`.

```python
import pandas as pd

data = {
    "user": ["user01", "user02", "user03"],
    "logins": [12, 7, 30],
    "failed": [0, 2, 9],
}
df = pd.DataFrame(data)

print(df)
print(df.shape)

logins = df["logins"]
print(logins)
print(type(logins))
print(logins.sum())
```

```output
     user  logins  failed
0  user01      12       0
1  user02       7       2
2  user03      30       9
(3, 3)
0    12
1     7
2    30
Name: logins, dtype: int64
<class 'pandas.Series'>
49
```

Look at what you see:

- The numbers on the left (0, 1, 2) are the **index**. Pandas numbers the rows for you.
- `shape` is a pair: rows first, then columns. This table has 3 rows and 3 columns.
- `df["logins"]` is a Series. It remembers its name, `logins`, and its type, `int64` (a whole number stored in 64 bits).
- A Series has methods such as `sum()`, like a NumPy array.

### Read the web log

Real tables come from files. `pd.read_csv` reads a CSV file into a DataFrame in one line. It also works out the column names from the first row.

The course keeps a copy of the web log from Week 2 at `assets/data/web_log.csv`. Everyone reads the same file, so your numbers will match this lesson. The code below finds the file from wherever you run it. `Path` is a tool for working with file locations. Leave the first lines as they are. Week 2 explained files.

```python
from pathlib import Path

import pandas as pd

ASSETS = Path(__file__).resolve().parents[4] / "assets"
LOG_FILE = ASSETS / "data" / "web_log.csv"

df = pd.read_csv(LOG_FILE)
```

**Example: Where does the path come from?** `__file__` is the path of the file you are running. `parents[4]` goes up four folders to the top of the course. If you save your own file somewhere else, change this line to point to `web_log.csv`.

### A first look at a table

Never trust a table you have not looked at. These are the first things to check. Code: `5.1_code/explore_log.py`.

```python
print(df.head())      # the first 5 rows
print(df.tail(3))     # the last 3 rows
print(df.shape)       # (rows, columns)
print(df.columns)     # the column names
print(df.dtypes)      # the type of each column
df.info()             # a summary of everything
print(df.describe())  # statistics for number columns
```

The code files in this course also call `pd.set_option("display.max_columns", None)`. It tells Pandas to print every column instead of hiding the middle ones with `...`. It only changes how a table is shown, not the data.

```output
              ip         date      time method              path  status     size
0     192.0.2.33  09/Nov/2026  07:13:45    GET     /contact.html     200   2260.0
1  198.51.100.23  09/Nov/2026  07:22:54    GET  /images/logo.png     200  18240.0
2  198.51.100.56  09/Nov/2026  07:32:30    GET      /courses.html     200   7215.0
3     192.0.2.40  09/Nov/2026  07:34:13    GET     /contact.html     200   2260.0
4   198.51.100.7  09/Nov/2026  07:41:34    GET     /css/site.css     200   4096.0
                ip         date      time method            path  status    size
197     192.0.2.40  10/Nov/2026  18:36:42    GET  /old-page.html     404   318.0
198  198.51.100.56  10/Nov/2026  18:37:01    GET   /contact.html     200  2260.0
199     192.0.2.15  10/Nov/2026  18:46:08    GET   /contact.html     304     NaN
(200, 7)
Index(['ip', 'date', 'time', 'method', 'path', 'status', 'size'], dtype='str')
ip            str
date          str
time          str
method        str
path          str
status      int64
size        float64
dtype: object
<class 'pandas.DataFrame'>
RangeIndex: 200 entries, 0 to 199
Data columns (total 7 columns):
 #   Column  Non-Null Count  Dtype  
---  ------  --------------  -----  
 0   ip      200 non-null    str    
 1   date    200 non-null    str    
 2   time    200 non-null    str    
 3   method  200 non-null    str    
 4   path    200 non-null    str    
 5   status  200 non-null    int64  
 6   size    188 non-null    float64
dtypes: float64(1), int64(1), str(5)
memory usage: 11.1 KB
           status          size
count  200.000000    188.000000
mean   252.695000   4964.367021
std     87.141149   5086.255531
min    200.000000    318.000000
25%    200.000000   1280.000000
50%    200.000000   4096.000000
75%    304.000000   5120.000000
max    500.000000  18240.000000
```

What each line tells you:

- `head()` and `tail()` show the start and end of the table. Give a number to change how many rows.
- `shape` says there are 200 rows (requests) and 7 columns.
- `dtypes` gives the type of each column. Text columns show as `str` here. In an older version of Pandas they show as `object`. Both mean text.
- `info()` lists the **non-null count** for each column. Every column has 200, except `size`, which has 188. Twelve cells are empty. Section 5.4 explains why.
- `size` is `float64` (a decimal number), even though sizes are whole bytes. Section 5.4 explains that too.
- `describe()` gives the count, mean, standard deviation (std, from Week 4), minimum, quartiles and maximum. It only covers number columns. The mean of `status` (252.695) is not useful, because a status code is a label, not a quantity. Pandas cannot tell the difference. You must.

📷 Image placeholder: episodes/fig/pycharm_dataframe_output.png — the Run window in PyCharm showing the output of `df.head()`

### Select columns

Use square brackets and a column name in quotes. One name gives a Series. A list of names gives a smaller DataFrame. Code: `5.1_code/select_columns.py`.

```python
status = df["status"]
print(status.head())
print(status.max())
print(df["ip"].nunique())

small = df[["ip", "status"]]
print(small.head())
```

```output
0    200
1    200
2    200
3    200
4    200
Name: status, dtype: int64
500
14
              ip  status
0     192.0.2.33     200
1  198.51.100.23     200
2  198.51.100.56     200
3     192.0.2.40     200
4   198.51.100.7     200
```

- `df["status"]` has one pair of brackets and gives a Series.
- `df[["ip", "status"]]` has two pairs. The outer brackets select. The inner brackets make a list of names. The result is a DataFrame.
- `nunique()` counts the different values. There are 14 different addresses in the log.

### Make a new column

You can make a new column by giving it a name and a value. The value can be worked out from other columns, one row at a time, with no loop.

```python
df["size_kb"] = df["size"] / 1024
df["is_error"] = df["status"] >= 400
print(df[["path", "status", "size", "size_kb", "is_error"]].head())
print(df["is_error"].sum())
```

```output
               path  status     size    size_kb  is_error
0     /contact.html     200   2260.0   2.207031     False
1  /images/logo.png     200  18240.0  17.812500     False
2     /courses.html     200   7215.0   7.045898     False
3     /contact.html     200   2260.0   2.207031     False
4     /css/site.css     200   4096.0   4.000000     False
45
```

The first line divides every size by 1024 (the number of bytes in a kilobyte). The second line makes a column of `True` and `False` values. Adding up `True` and `False` counts the `True` values, as it did with NumPy masks in Week 4. So 45 requests had a status of 400 or more.

The new columns live only in your DataFrame in memory. The CSV file on disk is not changed.

### Common mistakes

- **Forgetting the quotes:** `df[status]` looks for a variable called `status`. Write `df["status"]`.
- **Wrong capital letters:** column names are case sensitive. `df["Status"]` raises `KeyError: 'Status'`.
- **One pair of brackets for two columns:** `df["ip", "status"]` raises `KeyError`. Write `df[["ip", "status"]]`.
- **Thinking `describe()` understands meaning:** it gives an average of status codes, which means nothing.
- **Expecting the file to change:** a new column is not saved unless you save it. This course does not save files this week.

::::::::::::::::::::::::::::::::::::: challenge

### Exercises

Use the `df` you made from `web_log.csv`. Put your answers in a file called `exercises_11_1.py`.

::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::: challenge

### Exercises: Level 1

1. Install Pandas in your virtual environment. Create `exercises_11_1.py`, import Pandas as `pd` and read the web log. Print `df.shape`. You should see `(200, 7)`.
2. Print the first 8 rows. Then print the last 2 rows.
3. Print the column names and the type of each column. Which column is the only decimal one?
4. Print the `method` column's `nunique()`. Then print `df["path"].nunique()`. How many different paths are there?
5. Select the three columns `ip`, `path` and `status` into a new DataFrame called `slim`. Print its first 3 rows.
6. Make a new column `is_post` that is `True` when `method` is `"POST"`. Print how many requests were POST requests.

::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::: challenge

### Exercises: Level 2

1. Make a new column `size_kb` rounded to one decimal place. Search for the Series method `round`. Print the first 5 values.
2. Make a small DataFrame by hand with three of your own made-up users and their login counts. Print the sum and the maximum of one column.
3. Print `df.describe()` for only the `size` column, using `df["size"].describe()`.

### Further reading

- Pandas development team (2026) *pandas documentation*. Available at: https://pandas.pydata.org/docs/ (Accessed: 11 November 2026).

::::::::::::::::::::::::::::::::::::::::::::::::

## 5.2 Filtering and sorting {#section-5-2}

### Why filtering matters

A log has hundreds or thousands of rows. You rarely want all of them. You want the failed logins, or the requests from one address, or the activity at 2 am. **Filtering** means keeping only the rows that match a condition. **Sorting** puts rows in order so the biggest or latest ones are easy to see.

In Week 4 you made a boolean mask with NumPy, such as `scores > 50`, and used it to pick values. Pandas works the same way. If you remember masks, you already know most of this section.

All examples use `df = pd.read_csv(...)` on the web log, set up as in Section 5.1.

### Filter with a boolean mask

A **mask** is a Series of `True` and `False`, one for each row. Code: `5.2_code/filter_rows.py`.

```python
mask = df["status"] == 404
print(mask.head())
print(mask.sum())

not_found = df[mask]
print(not_found.head())
print(len(not_found))
```

```output
0    False
1    False
2    False
3    False
4    False
Name: status, dtype: bool
16
               ip         date      time method            path  status   size
29  198.51.100.23  09/Nov/2026  11:50:19    GET  /old-page.html     404  318.0
49   198.51.100.7  09/Nov/2026  14:45:43    GET  /old-page.html     404  318.0
81     192.0.2.10  09/Nov/2026  18:39:27    GET  /old-page.html     404  318.0
84   203.0.113.77  09/Nov/2026  23:41:17    GET          /admin     404  318.0
85   203.0.113.77  09/Nov/2026  23:41:21    GET   /wp-login.php     404  318.0
16
```

- `df["status"] == 404` compares every row at once. The mask has 200 values. `head()` shows the first five, which are all `False`.
- `mask.sum()` counts the `True` values. Sixteen requests were "not found".
- `df[mask]` keeps the rows where the mask is `True`. Notice that the index numbers (29, 49, 81 ...) are kept from the original table. They tell you where each row came from.
- Most people skip the variable and write `df[df["status"] == 404]`. Read it as "the rows of `df` where `df["status"]` equals 404".

`len(table)` gives the number of rows. It is the same as `table.shape[0]`.

### Combine conditions

Join masks with `&` (and) and `|` (or). **Each condition must be inside its own round brackets.**

```python
failed = df[(df["path"] == "/login") & (df["status"] == 401)]
print(len(failed))
print(failed.head(3))

problems = df[(df["status"] == 401) | (df["status"] == 404)]
print(len(problems))
```

```output
27
               ip         date      time method    path  status   size
13     192.0.2.10  09/Nov/2026  09:06:20   POST  /login   401  512.0
20  198.51.100.23  09/Nov/2026  11:06:27   POST  /login   401  512.0
58  198.51.100.56  09/Nov/2026  15:17:58   POST  /login   401  512.0
43
```

- `&` means both conditions must be true. There were 27 failed logins: a request to `/login` that was refused with status 401.
- `|` means at least one must be true. There were 43 requests with status 401 or 404 (27 and 16).
- Python's own `and`, `or` and `not` do not work on a whole Series. Use `&`, `|` and `~` (not).
- The brackets matter because `&` is worked out before `==`. Without brackets Python gets the order wrong, and Pandas stops with an error.

### Match several values with `isin`

When you want one of many values, `|` gets long. `isin` takes a list.

```python
same_problems = df[df["status"].isin([401, 404])]
print(len(same_problems))

big_ok = df[(df["status"] == 200) & (df["size"] > 10000)]
print(len(big_ok))
```

```output
43
20
```

`isin([401, 404])` means "status is 401 or status is 404". It gives the same 43 rows as before, in less space. The second example mixes a status check with a size check: 20 successful requests sent more than 10,000 bytes.

### Sort rows

`sort_values` puts rows in order. It gives you a new DataFrame and leaves `df` unchanged. Code: `5.2_code/sort_count.py`.

```python
by_size = df.sort_values("size")
print(by_size[["path", "status", "size"]].head(3))

biggest = df.sort_values("size", ascending=False)
print(biggest[["path", "status", "size"]].head(3))

ordered = df.sort_values(["status", "ip"], ascending=[False, True])
print(ordered[["ip", "time", "path", "status"]].head(5))
```

```output
              path  status   size
29  /old-page.html     404  318.0
49  /old-page.html     404  318.0
86           /.env     404  318.0
                path  status   size
1   /images/logo.png     200  18240.0
10  /images/logo.png     200  18240.0
8   /images/logo.png     200  18240.0
                ip      time            path  status
148     192.0.2.33  11:47:03   /contact.html     500
44   198.51.100.23  14:02:11   /courses.html     500
81     192.0.2.10  18:39:27  /old-page.html     404
197     192.0.2.40  18:36:42  /old-page.html     404
29   198.51.100.23  11:50:19  /old-page.html     404
```

- The default is smallest first. Add `ascending=False` for largest first.
- To sort by two columns, give a list. The second column breaks ties in the first. `ascending` can also be a list, one choice for each column. Here the status goes from large to small, and the address from small to large inside each status.
- Rows with a missing size are put at the end. Section 5.4 explains missing values.
- Rows with equal values may come out in a different order on your computer. Your row numbers might differ from the lesson for the tied rows.
- `df[["path", "status", "size"]]` after the sort picks only the columns we want to see.

### Count values

`value_counts()` counts how often each value appears in a column and puts the biggest first. It is one of the most useful methods for logs.

```python
print(df["status"].value_counts())
print(df["method"].value_counts())
print(df["ip"].value_counts().head(3))
```

```output
status
200    143
401     27
404     16
304     12
500      2
Name: count, dtype: int64
method
GET     166
POST     34
Name: count, dtype: int64
ip
198.51.100.56    22
203.0.113.45     22
192.0.2.15       20
Name: count, dtype: int64
```

The result is a Series. The values of the column become its index, so `df["status"].value_counts()[404]` gives 16. Two addresses tie at 22 requests, so the first two lines of the last result could swap places on another computer. Section 5.3 and the Build show how to make a tie order fixed.

### Text methods on a column

In Week 1 you sliced strings, such as `"07:13:45"[:2]` to get `"07"`. A Series of text has a `.str` helper that does the same to every row. Code: `5.2_code/hour_column.py`.

```python
print(df["time"].head(3))
print(df["time"].str[:2].head(3))

df["hour"] = df["time"].str[:2].astype(int)
print(df[["time", "hour"]].head(3))
print(df["hour"].dtype)

night = df[df["hour"] < 6]
print(len(night))
print(night["ip"].value_counts())

pages = df[df["path"].str.endswith(".html")]
print(len(pages))
print(df["method"].str.lower().head(2))
```

```output
0    07:13:45
1    07:22:54
2    07:32:30
Name: time, dtype: str
0    07
1    07
2    07
Name: time, dtype: str
       time  hour
0  07:13:45     7
1  07:22:54     7
2  07:32:30     7
int64
22
ip
203.0.113.45    22
Name: count, dtype: int64
93
0    get
1    get
Name: method, dtype: str
```

- `.str[:2]` is the Week 1 slice, applied to every row. The result is still text.
- `.astype(int)` changes the type of a column. Now `07` is the number 7, so you can compare with `< 6`.
- 22 requests came before 6 am, and all of them came from one address, `203.0.113.45`.
- `.str.endswith(".html")` is a Week 1 string method, applied to every row. 93 requests were for `.html` pages.
- `.str.lower()` makes every method lower case. The original column is not changed.
- Other helpers include `.str.lower()`, `.str.upper()`, `.str.startswith()` and `.str.contains()`.

### Common mistakes

- **Using `and` instead of `&`:** `df[(a) and (b)]` stops with `ValueError: The truth value of a Series is ambiguous.` Use `&`.
- **Missing brackets:** `df[df["path"] == "/login" & df["status"] == 401]` stops with a `TypeError`. Put each condition in round brackets.
- **Using one `=`:** `=` sets a value. `==` compares. Use `==` in a mask.
- **Forgetting that sorting does not change `df`:** write `df = df.sort_values(...)` or keep the result in a new name.
- **Text compared with a number:** `df["status"] == "404"` finds nothing, because `status` holds numbers, not text.

::::::::::::::::::::::::::::::::::::: challenge

### Exercises

Put your answers in `exercises_11_2.py`. Read the web log first.

::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::: challenge

### Exercises: Level 1

1. Keep the rows where `method` is `"POST"`. Print how many there are. You should get 34.
2. Keep the rows where `status` is 500. Print the `ip`, `time` and `path` columns for those rows.
3. Keep the rows where the status is 200 **and** the size is more than 5000. Print how many there are.
4. Use `isin` to keep the rows with status 304 or 500. Print how many there are. You should get 14.
5. Sort the whole table by `size`, largest first. Print the `path` and `size` of the top 3 rows.
6. Use `value_counts()` on the `path` column. Print the top 3 paths.

::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::: challenge

### Exercises: Level 2

1. Make an `hour` column. Print how many requests were made at hour 23.
2. Keep the rows where the path starts with `/admin`. Use `.str.startswith("/admin")`.
3. Use `~` to keep the rows where the status is **not** 200. You should get 57.
4. Sort by `ip` ascending and `time` descending in one call.

### Further reading

- Pandas development team (2026) *pandas documentation*. Available at: https://pandas.pydata.org/docs/ (Accessed: 11 November 2026).

::::::::::::::::::::::::::::::::::::::::::::::::

## 5.3 Grouping with groupby {#section-5-3}

### Why grouping matters

Filtering answers "show me these rows". Grouping answers "for each address, how many requests?" or "for each status, what is the average size?". Security teams use it to find the one address that makes far more requests than the rest. Data teams use it to total sales for each region.

In Part 1 you could count things with a loop and a dictionary. `groupby` does that in one line.

### Split, apply, combine

`groupby` works in three steps. Think of sorting a pile of cards into piles by suit.

1. **Split:** the rows are divided into groups, one for each different value in a column.
2. **Apply:** the same calculation is done on each group (count it, add it up, average it).
3. **Combine:** the answers are put together into one result, with the group names as its index.

All examples use the web log read into `df` as in Section 5.1.

### Count rows in each group

Code: `5.3_code/groupby_basics.py`.

```python
per_ip = df.groupby("ip").size()
print(per_ip.head())
print(per_ip["203.0.113.77"])

busiest = per_ip.sort_values(ascending=False)
print(busiest.head(3))
```

```output
ip
192.0.2.10    12
192.0.2.15    20
192.0.2.21    15
192.0.2.33    15
192.0.2.40    10
dtype: int64
10
ip
203.0.113.45     22
198.51.100.56    22
192.0.2.15       20
dtype: int64
```

- `df.groupby("ip")` splits the log into one group for each address. On its own it shows nothing. It waits for you to say what to do.
- `.size()` counts the rows in each group. The result is a Series. The addresses are its index, in alphabetical order.
- `per_ip["203.0.113.77"]` picks one group by name. This address made 10 requests.
- `.sort_values(ascending=False)` puts the biggest count first. A Series has no column to name, so you give no argument except the direction.
- Two addresses tie at 22. The Build task asks you to settle ties by address, so the answer is always the same.

### Work out a number for each group

Choose a column in square brackets, then a calculation. Code: `5.3_code/groupby_basics.py`.

```python
print(df.groupby("status")["size"].mean())
print(df.groupby("status")["size"].sum())
print(df.groupby("status")["size"].count())
print(df.groupby("status").size())
```

```output
status
200    6385.657343
304            NaN
401     512.000000
404     318.000000
500     620.000000
Name: size, dtype: float64
status
200    913149.0
304         0.0
401      13824.0
404      5088.0
500      1240.0
Name: size, dtype: float64
status
200    143
304      0
401     27
404     16
500      2
Name: size, dtype: int64
status
200    143
304     12
401     27
404     16
500      2
dtype: int64
```

Read these four results carefully.

- `["size"].mean()` gives the average size for each status. A successful page averages about 6,386 bytes. A failed login always sends back 512 bytes, and a not-found page 318.
- `.sum()` adds up the sizes in each group.
- `.count()` counts only the cells that have a value. It does **not** count empty cells.
- `.size()` counts all the rows in each group, empty or not.
- Status 304 has 12 rows (`size()`) but 0 counted sizes (`count()`). Every 304 row has an empty size, so its mean is `NaN` (not a number, see Section 5.4) and its sum is 0.
- The difference between `size()` and `count()` is a common trap. When in doubt, use `size()` to count rows.

### Several answers with `agg`

`agg` (short for aggregate) takes a list of calculation names. You get one column for each.

```python
summary = df.groupby("status")["size"].agg(["count", "mean", "max"])
print(summary)
```

```output
        count         mean      max
status                             
200       143  6385.657343  18240.0
304         0          NaN      NaN
401        27   512.000000    512.0
404        16   318.000000    318.0
500         2   620.000000    620.0
```

Now this is a DataFrame. Each row is a status, and each column is one answer. Code: `5.3_code/groupby_agg.py`.

You can also keep only the groups you care about with a mask on the result:

```python
per_ip = df.groupby("ip").size()
print(per_ip[per_ip >= 20])
```

```output
ip
192.0.2.15       20
198.51.100.56    22
203.0.113.45     22
dtype: int64
```

Only three addresses made 20 or more requests.

### Filter first, then group

Filter the rows, then group what is left. This finds who failed to log in.

```python
failed = df[(df["path"] == "/login") & (df["status"] == 401)]
print(failed.groupby("ip").size().sort_values(ascending=False))
```

```output
ip
203.0.113.45     22
192.0.2.10        2
198.51.100.23     1
198.51.100.56     1
198.51.100.7      1
dtype: int64
```

One address, `203.0.113.45`, has 22 of the 27 failed logins. The other four addresses have one or two each, which is a normal number of typing mistakes. That does not prove anything. It is a good reason to look closer. Addresses with no failed logins do not appear at all, because there are no rows for them.

### Tidy the result with `reset_index`

A group result has the group names as its index. Sometimes you want an ordinary table with normal columns. `reset_index` moves the index back into a column. Giving it a `name` names the count column.

```python
table = per_ip.reset_index(name="requests")
print(table.head(3))

top = table.sort_values(["requests", "ip"], ascending=[False, True])
print(top.head(4))
```

```output
           ip  requests
0  192.0.2.10        12
1  192.0.2.15        20
2  192.0.2.21        15
               ip  requests
9   198.51.100.56        22
12   203.0.113.45        22
1      192.0.2.15        20
6   198.51.100.23        17
```

Now `table` is a DataFrame with the columns `ip` and `requests`, so you can use `sort_values` with column names. Sorting by `requests` (largest first) and then `ip` (smallest first) gives a tie order that never changes. `198.51.100.56` comes before `203.0.113.45` because `"1"` comes before `"2"`. Addresses are sorted as text, so `192.0.2.15` would sort before `192.0.2.2`. That is fine for a repeatable order.

### Common mistakes

- **Forgetting the calculation:** `df.groupby("ip")` alone prints something like `<pandas...DataFrameGroupBy object>`. Add `.size()`, `.sum()` or another calculation.
- **Mixing up `size()` and `count()`:** `size()` counts rows. `count()` counts filled cells in a column.
- **Averaging a label:** `df.groupby("ip")["status"].mean()` runs, but an average status code means nothing.
- **Forgetting the column name:** `df.groupby("status").mean()` tries to average every column, including text ones, and may stop with an error. Pick the column first: `df.groupby("status")["size"].mean()`.
- **Expecting a column called `ip` after `groupby`:** the addresses are in the index until you call `reset_index`.

::::::::::::::::::::::::::::::::::::: challenge

### Exercises

Put your answers in `exercises_11_3.py`.

::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::: challenge

### Exercises: Level 1

1. Count the requests for each `method` with `groupby`. You should get 166 GET and 34 POST.
2. Count the requests for each `path`. Sort the result largest first and print the top 3.
3. Work out the average `size` for each `method`. Which method has the larger average?
4. Count the requests made on each `date`. You should get 94 for 09/Nov/2026 and 106 for 10/Nov/2026.
5. Work out the total `size` for each `ip`. Print the top 3, largest first.
6. Keep only the rows with status 404. Count them for each `ip` and print the result sorted largest first. Which address stands out?

::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::: challenge

### Exercises: Level 2

1. Use `agg(["count", "sum"])` on `size`, grouped by `method`.
2. Make a table of requests for each `ip` with `reset_index(name="requests")`. Sort it by `requests` and then `ip`, as in the lesson.
3. Group by two columns at once with `df.groupby(["date", "method"]).size()`. What do you see?

### Further reading

- Pandas development team (2026) *pandas documentation: Group by, split-apply-combine*. Available at: https://pandas.pydata.org/docs/ (Accessed: 11 November 2026).

::::::::::::::::::::::::::::::::::::::::::::::::

## 5.4 Missing values {#section-5-4}

### Why missing values matter

Real data has gaps. A sensor stops for an hour. A person leaves a form field empty. A web server sends back "nothing has changed" and so has no size to record. If you ignore the gaps, your totals and averages can be wrong without any warning. Good analysts find the gaps first, decide what to do, and write the decision down.

### What `NaN` is

In `web_log.csv` a missing size is an empty cell. When `read_csv` meets an empty cell it stores **`NaN`**, short for "not a number". `NaN` means "no value here".

This also explains something you saw in Section 5.1. The `size` column is `float64` (decimal), not whole numbers. Whole-number columns in Pandas cannot hold `NaN`. One empty cell is enough to make Pandas change the whole column to decimals. That is why `size` shows `2260.0` and not `2260`.

Which rows are empty? Code: `5.4_code/missing_values.py`.

```python
print(df.tail(3))
```

```output
                ip         date      time method            path  status    size
197     192.0.2.40  10/Nov/2026  18:36:42    GET  /old-page.html     404   318.0
198  198.51.100.56  10/Nov/2026  18:37:01    GET   /contact.html     200  2260.0
199     192.0.2.15  10/Nov/2026  18:46:08    GET   /contact.html     304     NaN
```

Row 199 has status 304, which means "not modified". The server told the browser to reuse its saved copy, so it sent no page and recorded no size.

### Find missing values

`isna()` gives `True` where a value is missing. Add `sum()` to count them, as with any mask.

```python
print(df.isna().sum())
print(df["size"].isna().sum())

no_size = df[df["size"].isna()]
print(no_size["status"].value_counts())
```

```output
ip         0
date       0
time       0
method     0
path       0
status     0
size      12
dtype: int64
12
status
304    12
Name: count, dtype: int64
```

- `df.isna().sum()` counts the missing cells in every column at once. Only `size` has gaps: 12.
- All 12 rows with no size have status 304. So these gaps are not mistakes. They mean "no data was sent".

Finding the reason matters. A gap that means "no data was sent" should be treated differently from a gap that means "the recording broke".

### Drop or fill

There are two common choices.

- **Drop** the rows with a gap: `dropna`. You lose those rows.
- **Fill** the gap with a value: `fillna`. You keep the rows but you invent a value.

```python
print(df["size"].count())
print(df["size"].sum())
print(df["size"].mean())

dropped = df.dropna(subset=["size"])
print(dropped.shape)
print(dropped["size"].mean())

filled = df["size"].fillna(0)
print(filled.tail(3))
print(filled.mean())

df["size_filled"] = df["size"].fillna(0).astype(int)
print(df[["status", "size", "size_filled"]].tail(3))
print(df["size_filled"].sum())
```

```output
188
933301.0
4964.367021276596
(188, 7)
4964.367021276596
197     318.0
198    2260.0
199       0.0
Name: size, dtype: float64
4666.505
     status    size  size_filled
197     404   318.0          318
198     200  2260.0         2260
199     304     NaN            0
933301
```

Go through it line by line.

- `count()` counts filled cells: 188 of 200.
- `dropna(subset=["size"])` drops only the rows where `size` is empty. `subset` says which column to look at. Without it, a gap in *any* column drops the row. The new shape is `(188, 7)`.
- The mean of the dropped table is the same as the mean of the original: 4964.37. The next part explains why.
- `fillna(0)` replaces every `NaN` with 0. The mean changes to 4666.505, because 200 values are now added up and divided by 200, and 12 of them are zeros.
- `.astype(int)` turns the filled column into whole numbers again. It only works after the gaps are filled.
- The sum is 933,301 either way. A zero adds nothing.

So which is right? It depends on the question.

| Question | Better choice | Why |
|---|---|---|
| What is the average size of a response that sent data? | Drop (or leave as `NaN`) | A 304 sent nothing, so it should not pull the average down. |
| How many bytes did the server send in total? | Fill with 0 | No data sent means 0 bytes. The total is the same either way. |
| What is the typical size of a 200 response? | Filter to status 200 first | The empty sizes are not in that group at all. |

Do not fill with 0 just because it is easy. A temperature of 0 degrees is not "no reading".

### A mean skips missing values

Pandas does not warn you when it skips a gap. Code: `5.4_code/small_missing.py`.

```python
import pandas as pd

scores = pd.Series([10, None, 30])
print(scores)
print(scores.mean())
print(scores.fillna(0).mean())
print(len(scores), scores.count())
```

```output
0    10.0
1     NaN
2    30.0
dtype: float64
20.0
13.333333333333334
3 2
```

- `mean()` skipped the `NaN`. It worked out (10 + 30) / 2 = 20, not (10 + 30) / 3.
- With `fillna(0)` the mean is 13.33. Same data, a different answer.
- `len(scores)` is 3 but `count()` is 2. If the two numbers differ, you have gaps. Check before you trust an average.

### Write down what you did

Whatever you choose, record it. A comment in the code or a line in your note is enough. Your note should say:

1. What was missing, and how many (12 of 200 sizes).
2. Why it was missing, if you could find out (all were status 304).
3. What you did (filled with 0 for the total, left as `NaN` for averages).
4. How that changes the answer.

This is the habit the Concepts Bridge this week calls "recording every cleaning step". Someone else should be able to repeat your work and get the same result.

### Common mistakes

- **Comparing with `NaN`:** `df["size"] == None` and `df["size"] == float("nan")` do not find gaps. Use `isna()`.
- **Dropping without looking:** `df.dropna()` with no `subset` removes a row if *any* column is empty. Here that is only the 12 rows, but in another table it could remove most of the data.
- **Filling with 0 for an average:** zeros pull the mean down, as you saw (4666.505 against 4964.367).
- **Forgetting that `dropna` and `fillna` give a new result:** the original `df` is unchanged unless you keep the result.
- **Not noticing that the type changed:** a column with gaps is decimal. Use `astype(int)` after filling if you need whole numbers.

::::::::::::::::::::::::::::::::::::: challenge

### Exercises

Put your answers in `exercises_11_4.py`.

::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::: challenge

### Exercises: Level 1

1. Print how many missing values each column of the web log has.
2. Keep the rows where `size` is missing. Print the number of rows and the different `status` values they have.
3. Print `df["size"].count()` and `len(df)`. Why are they different?
4. Make a new DataFrame called `known` with the rows that have a size. Print its shape. You should get `(188, 7)`.
5. Work out the mean of `size` in `df`. Then work out the mean after `fillna(0)`. Write one sentence on why the two numbers differ.
6. Make a small Series `pd.Series([4, None, 8, None])`. Predict its mean, then run it. Print `count()` as well.

::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::: challenge

### Exercises: Level 2

1. Fill the missing sizes with the **median** of the column (`df["size"].median()`) instead of 0. Compare the new mean with the other two. When might this be a sensible choice, and when not?
2. Make a new column `has_size` that is `True` when the size is not missing. Use `notna()`. Count the `True` values.
3. Write three lines of comments that record what you did with the missing sizes, using the list in "Write down what you did".

### Further reading

- Pandas development team (2026) *pandas documentation: Working with missing data*. Available at: https://pandas.pydata.org/docs/ (Accessed: 11 November 2026).

::::::::::::::::::::::::::::::::::::::::::::::::

## Concepts Bridge: Cleaning Data and Personal Information {#week-5-bridge}

**Time: 30 minutes.** Reading 12 minutes, activities 12 minutes, checking the model answer 6 minutes.

### Why this matters

Real data is rarely tidy. If you analyse it without cleaning it, your answers can be wrong and you will not know. Real data can also be about real people. Then you have a duty to treat it with care, and in Australia there are rules about it.

This bridge has two parts. Part 1 is about cleaning. Part 2 is about personal information. It is an introduction only. It is **not legal advice**.

### Part 1: common data problems

In the lessons you could look at every row. The web log has 200 rows, and the 12 missing sizes were easy to find. A real log may have millions of rows, so you need a checklist.

| Problem | Example | What you might do |
|---|---|---|
| **Missing values** | A `size` cell is empty. | Find out why. Drop the row, or fill the gap, or leave it as `NaN`. |
| **Duplicates** | The same row appears twice. | Check that it is a real duplicate, then drop one copy. |
| **Wrong types** | A number stored as text, such as `"eight"` or `"12"`. | Convert it, or mark the row as bad if it cannot be converted. |
| **Inconsistent spelling** | `Finance`, `finance` and `Fnance`. | Make the case the same, then fix known mistakes. |
| **Impossible values** | A login count of -3, or a time of 25:70. | Do not guess. Mark it, check the source, or set it to missing. |

The most important habit is to **record every cleaning step**. Write down what you found, how many rows it affected, what you did and why. Then:

- someone else can repeat your work and get the same answer,
- you can explain a surprising number later,
- you can tell the difference between what the data said and what you changed.

Never change the original file. Clean a copy, and keep the steps in code or in a note.

### Part 2: personal information

**Personal information** is information or an opinion about a person who is identified, or who could reasonably be identified. It does not have to include a name. Think about whether someone could work out who it is about, perhaps by combining it with other data.

Some data is clearly personal: a name, an address, a date of birth. Other data becomes personal in combination.

- An **IP address** (the address of a device on a network) in a web log can be linked to a household or a workplace. With the time and the pages visited, it may point to one person.
- A **username** such as `jwilson` could point to one person. Together with a login time and a department, it almost certainly does.

When you wonder "is this personal?", ask: could someone reasonably work out who this is about, using this data and other data they might have?

#### The Australian Privacy Principles

In Australia, the **Privacy Act 1988** sets rules for how many organisations handle personal information. It covers Australian Government agencies and many private organisations. Not every organisation is covered. The rules are called the **Australian Privacy Principles (APPs)**. They are written in careful legal language. In plain words, the ideas are:

- **Collect only what you need.** If you do not need a piece of data, do not collect it.
- **Use it for the purpose it was collected for.** Data collected to run a login system is not free to use for something unrelated.
- **Keep it secure.** Protect it from loss and from people who should not see it.
- **De-identify or delete it when it is no longer needed.** To **de-identify** data is to remove or change details so a person can no longer reasonably be identified.

This is a general summary. It leaves out many details and exceptions. The real text is on the website of the Office of the Australian Information Commissioner (OAIC): https://www.oaic.gov.au/privacy/australian-privacy-principles. Read it there. If you handle personal information at work, ask your privacy officer or a lawyer.

#### Why this course uses only synthetic data

**Synthetic data** is made up by a person or program. It looks like real data, but it describes nobody. Every file in this course is synthetic. The addresses in the web log come from ranges reserved for examples and belong to nobody. The users are called `user01` and so on.

This means you can practise on logs and login tables without any risk to a real person, and without needing permission to use the data. Real web logs need care for exactly the reasons above. Your log summary note this week asks you to say so in one sentence.

::::::::::::::::::::::::::::::::::::: challenge

### Activity 1: clean a small table (6 minutes)

Here is a small, made-up staff table.

| name | department | logins | start_date |
|---|---|---|---|
| Jack Wilson | Finance | 12 | 2024-03-01 |
| jack wilson | finance | 12 | 2024-03-01 |
| Olivia Thompson | Fnance | -3 | 2024-04-15 |
| user03 | IT | eight | 15/04/2024 |
| Olivia Thompson | HR | (empty) | 2024-05-10 |

List the cleaning steps you would take, in order. For each one, say which problem from the table in Part 1 it fixes. Then say what you would write down.

### Activity 2: personal or not? (6 minutes)

A staff login table has four columns. You must write a report about **how many logins each department has**. For each column, decide: is it personal information, and would you **keep** it, **drop** it, or **replace it with a code** in the report? Give one reason each.

| Column | Example |
|---|---|
| `full_name` | Olivia Thompson |
| `username` | othompson |
| `last_ip` | 203.0.113.45 |
| `department` | Finance |

:::::::::::::::: solution

### Model answer

**Activity 1.** One sensible order:

1. Make a copy of the table and keep the original. Start a list of steps.
2. Make `name` and `department` the same case (inconsistent spelling). `Jack Wilson` and `jack wilson` are now the same.
3. Fix `Fnance` to `Finance` (inconsistent spelling).
4. Drop the duplicate of the first row (duplicates). Rows 1 and 2 now match.
5. Change `eight` to `8` (wrong type), or mark it as missing if you are not sure.
6. Write all the dates in the same format (wrong type or inconsistent format).
7. Mark the login count of -3 as missing, because it is impossible (impossible values). Check the source if you can.
8. Decide what to do with the empty `logins` (missing values). For example, leave it as `NaN` so it does not change an average.

You would write down each step, how many rows it touched, and why. For example: "Dropped 1 duplicate row (row 2). Set 1 impossible value to missing (row 3)."

**Activity 2.**

| Column | Personal? | For a report on logins by department | Reason |
|---|---|---|---|
| `full_name` | Yes | **Drop** | The report does not need names. |
| `username` | Yes, it can point to one person | **Drop**, or **replace with a code** such as `user01` if you must count different people | It is not needed to count logins by department. A code lets you count people without naming them. |
| `last_ip` | Can be, with other data | **Drop** | It is not needed for this question. With time and username, it may identify a person. |
| `department` | Not on its own | **Keep** | The report is about departments. Take care if a department has only one or two people, because the count could then point to them. |

These answers follow the idea "collect only what you need". Other answers can be reasonable if you give a reason. The reason matters more than the label.

:::::::::::::::::::::::::
::::::::::::::::::::::::::::::::::::::::::::::::

### Further reading

- Office of the Australian Information Commissioner (n.d.) *Australian Privacy Principles*. Available at: https://www.oaic.gov.au/privacy/australian-privacy-principles (Accessed: 11 November 2026).
- Pandas development team (2026) *pandas documentation: Working with missing data*. Available at: https://pandas.pydata.org/docs/ (Accessed: 11 November 2026).

## Practice task: Web-Log Summary with Pandas {#week-5-practice}

:::::::::::::::::::::::::::::::::::::::: callout

### Files for this task

The easiest way to get every file is the [course zip file](data/course-data.zip) from the Setup page. Unzip it and open the folder in PyCharm. The programs find the data files by their place in that folder, so keep the folder layout. You can also download single files here:

- [starter.py](files/week-5/starter.py)
- [solution.py](files/week-5/solution.py)
- [test_solution.py](files/week-5/test_solution.py)

:::::::::::::::::::::::::::::::::::::::::::::::::::

**Time: 2 hours.** This is your portfolio item for Week 5. Your tutor marks it at the end of the week.

### Goal

Use Pandas to summarise the course web log, `assets/data/web_log.csv`. You write small functions that each answer one question. Then you write a short note saying what the summary shows.

You do not need your Week 2 files. The log is read from the course folder.

### Set up first

The tests need Pandas and pytest. Install both in your project's virtual environment (the one from Week 4). In the PyCharm Terminal, with `(.venv)` showing at the start of the line:

```output
python -m pip install pandas pytest
```

If you installed them already, pip tells you so. Nothing is harmed.

### Files

| File | What it is |
|---|---|
| `starter.py` | Your functions to fill in, and a given helper called `sorted_pairs`. |
| `test_solution.py` | Tests for the functions. |
| `solution.py` | A model answer. Try the task yourself before you look. |

### What each function returns

The functions take a DataFrame and return plain Python values, so the tests are simple. The exact return types are fixed:

| Function | Returns | Example |
|---|---|---|
| `load_log(path)` | a DataFrame | 200 rows and 7 columns for the course log |
| `status_counts(df)` | dictionary: status to count | `{200: 143, 401: 27}` |
| `missing_sizes(df)` | an `int`: rows with no size | `12` |
| `total_bytes(df)` | an `int`: sum of `size`, with a missing size counted as 0 | `933301` |
| `requests_per_ip(df, n=5)` | list of `(ip, count)` tuples, top `n` | `[("198.51.100.56", 22), ...]` |
| `failed_logins(df)` | list of `(ip, count)` tuples, all addresses with a failed login | `[("203.0.113.45", 22), ...]` |
| `not_found_paths(df, n=5)` | list of `(path, count)` tuples, top `n` | `[("/old-page.html", 6), ...]` |
| `requests_per_hour(df)` | dictionary: hour (an `int`, 0 to 23) to count | `{2: 22, 7: 6, ...}` |
| `suspicious_ips(df, threshold=10)` | sorted list of addresses (text) | `["203.0.113.45", "203.0.113.77"]` |

**The tie rule.** Lists of pairs are sorted by count, largest first. When two counts are equal, they are sorted by the name (address or path) in ascending order, a to z. In the real log, `198.51.100.56` and `203.0.113.45` both have 22 requests. The tie rule puts `198.51.100.56` first. The given helper `sorted_pairs` does this for you.

A **failed login** is a row where `path` is `"/login"` **and** `status` is `401`. A request that was not found (status 404) is not a failed login.

### Steps

1. **Set up (10 min).** Install Pandas and pytest as above. Open `starter.py`. Read `sorted_pairs` and its docstring. Leave the lines that set `ASSETS` and `LOG_FILE` as they are. Near the bottom, leave the two `if __name__ == "__main__":` lines too. Run the file. It should print only a heading.
2. **Load and count (20 min).** Write `load_log`, `status_counts`, `missing_sizes` and `total_bytes`. Try each in `main()` with a `print` while you work, then take the prints out or keep them for the report. The real log should give `{200: 143, 401: 27, 404: 16, 304: 12, 500: 2}`, 12 missing sizes and a total of 933301.
3. **Busiest and failed (20 min).** Write `requests_per_ip` and `failed_logins`. Use `groupby("ip").size()` and pass the result to `sorted_pairs`.
4. **Paths, hours and suspicious addresses (20 min).** Write `not_found_paths`, `requests_per_hour` and `suspicious_ips`. For the hour, use the first two characters of `time` (Section 5.2).
5. **The report (15 min).** Write `main()` to print a tidy summary that uses every function. See the example run below.
6. **Test (10 min).** Run the tests. Fix the failures one at a time.
7. **Your note (15 min).** Write `log_summary.txt` (see below).
8. **Tidy up (10 min).** Check the checklist. Delete any files you made only for trying things. Make sure comments and docstrings are clear.

Total: 10 + 20 + 20 + 20 + 15 + 10 + 15 + 10 = 120 minutes.

### Example run

```output
Web-log summary
===============
Rows: 200
Rows with no size: 12
Total bytes sent (missing size counted as 0): 933,301

Requests for each status code
  200: 143
  304: 12
  401: 27
  404: 16
  500: 2

Busiest addresses
  198.51.100.56    22
  203.0.113.45     22
  192.0.2.15       20
  198.51.100.23    17
  198.51.100.48    17

Failed logins (/login with status 401)
  203.0.113.45     22
  192.0.2.10        2
  198.51.100.23     1
  198.51.100.56     1
  198.51.100.7      1

Paths most often not found (status 404)
  /old-page.html    6
  /.env             1
  /admin            1
  /admin/login      1
  /backup.zip       1

Requests for each hour
  02:00   22
  07:00    6
  ...

Addresses with 10 or more 401 or 404 responses
  203.0.113.45
  203.0.113.77

A pattern in a log is a reason to look closer. It is not proof.
```

The hours list has 14 lines in the real run. Your wording can differ.

### Hints

- `df["status"].value_counts().to_dict()` gives the status counts as a dictionary.
- `df["size"].isna().sum()` counts the gaps. It gives a NumPy number. Wrap it in `int(...)` so the result is a plain `int`.
- `df["size"].fillna(0).sum()` adds the sizes with each gap counted as 0. Wrap it in `int(...)` too.
- Two conditions need brackets: `df[(df["path"] == "/login") & (df["status"] == 401)]`.
- `sorted_pairs(...)` returns a list. To keep the top `n`, slice it: `pairs[:n]`.
- `df["time"].str[:2].astype(int)` gives the hours as whole numbers. `value_counts().sort_index().to_dict()` turns them into a dictionary in hour order.
- `counts[counts >= threshold]` keeps the large counts in a Series. `.index` holds the addresses. `sorted(...)` makes a list.
- Keep `print` inside `main()` only. Functions that only take values and return values are easy to test.
- Do not change the DataFrame you are given. If you need a new column, make a copy first, or calculate without one.

### Your note: `log_summary.txt`

Write five or six sentences in your own words in a plain text file called `log_summary.txt`. Cover:

1. What does the summary show? (For example, the number of requests and the most common status.)
2. Which two addresses stand out, and why?
3. What did you do about the 12 missing sizes, and why? (Section 5.4.)
4. What would you check next?
5. One sentence on why a real web log needs care under privacy rules. (See the Concepts Bridge.)

Say clearly that a pattern in a log is a reason to look closer, not proof that someone did something wrong.

### Check your work

- [ ] Run the tests. In PyCharm, right-click `test_solution.py` and choose **Run pytest**, or in the terminal: `python -m pytest weeks/week-5/practice`.
- [ ] To test your own file, open `test_solution.py` and change `import solution as log` to `import starter as log`.
- [ ] `starter.py` runs and prints a tidy report with no errors.
- [ ] Every function returns the type in the table above (plain `int`, dictionary, list or DataFrame).
- [ ] Ties are broken by name, so `198.51.100.56` comes before `203.0.113.45`.
- [ ] No function changes the DataFrame it is given, and only `main()` prints.
- [ ] `log_summary.txt` has five or six sentences, in your own words, and says that a pattern is not proof.

:::::::::::::::::::::::::::::::::::::: keypoints

- Each week has four blocks: Watch, Read & practise, Concepts Bridge and Build.
- A DataFrame is a table with named columns; a Series is one column.
- head, info and describe show you the data before you work on it.
- df[df["status"] == 404] keeps the rows that pass the test.
- Put each condition in brackets when you combine them.
- value_counts() counts how often each value appears.
- groupby splits the rows into groups, applies a calculation and combines the results.
- size() counts rows; count() counts values that are not missing.
- A missing value shows as NaN.
- Totals and means skip missing values unless you fill them.
- Write down every cleaning step you take.
- Record every cleaning step you take.
- Collect only what you need, use it for its purpose, keep it secure and remove it when it is no longer needed.
- This course uses synthetic data only.
- A pattern in a log is a reason to look closer, not proof.

::::::::::::::::::::::::::::::::::::::::::::::::
