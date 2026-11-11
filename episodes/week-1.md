---
title: 'Week 1: Text and encoding'
teaching: 119
exercises: 178
---

:::::::::::::::::::::::::::::::::::::: questions

- What will I learn in Week 1, and how should I spend my 6 hours?
- How do I pick out part of a piece of text?
- Why can I not change a string in place?
- How do I tidy and take text apart?
- How do I print neat, aligned tables?
- How does a computer store letters?
- Why does the length of a string differ from the length of its bytes?
- What is a computer really storing when it stores text?
- Can I clean text and count what is in it?

::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::: objectives

- Plan your study time for the week using the time plan.
- Use indexes and negative indexes to read one character.
- Cut out part of a string with a slice.
- Explain what immutable means for strings.
- Use methods such as lower, strip, replace, split and join.
- Format numbers and columns with f-string format specs.
- Use ord and chr to move between characters and numbers.
- Encode and decode text with UTF-8.
- Explain what goes wrong when the wrong encoding is used.
- Explain bits, bytes and hexadecimal.
- Explain why two files that look the same can differ in bytes.
- Build a letter-frequency analyser with a bar chart made of # characters.

::::::::::::::::::::::::::::::::::::::::::::::::

## Week 1 overview {#week-1-overview}

**Theme:** work with text in Python, from cutting and tidying strings to understanding how letters are stored as numbers.

Welcome to Part 2. It follows on from Part 1, so you already know the basics of Python. Part 2 covers text, files and logs, checking data and files, and then NumPy, Pandas and Matplotlib. You will use them for both data science and cyber security work. All the data is made up for the course. This first week is about text, because almost all data starts as text.

### Learning goals

By the end of this week you can:

1. Pick out and cut up text with indexing and slicing, and explain why strings are immutable.
2. Clean and split text with string methods, and print neat aligned tables with f-strings.
3. Explain how text is stored as numbers (ASCII and UTF-8), and use `ord`, `chr`, `encode` and `decode`.
4. Build a letter-frequency analyser that reads a text file and reports the ten most common letters.

### Time plan (under 6 hours)

| Block | What you do | Time |
|---|---|---|
| Watch | three short videos | 27 min |
| Read & practise | Sections 1.1, 1.2 and 1.3, plus exercises | 2 h 0 m |
| Concepts Bridge | Text is stored as numbers | 30 min |
| Build | Practice task: a letter-frequency analyser | 2 h |
| Quiz | Canvas quiz, 6 questions | 15 min |
| **Total** | | **5 h 12 min** |

Suggested split for Read & practise: Section 1.1 (45 min), Section 1.2 (45 min), Section 1.3 (30 min).

The week totals less than 6 h on purpose. Use any spare time to repeat exercises you found hard, or try the optional material.

---

### 1. Watch (27 min)

Watch these in order. Pause and try the code yourself in PyCharm. The videos are from different presenters, so the style changes from video to video.

| # | Video | Length | Look out for |
|---|---|---|---|
| 1 | [Corey Schafer] [Python Tutorial: Slicing Lists and Strings](https://www.youtube.com/watch?v=ajrtAuDg3yw) | 10:44 | How an index picks one character and how `[start:stop]` cuts a piece. The video also uses lists. Slicing a string works the same way. |
| 2 | [Bro Code] [String methods in Python are easy!](https://www.youtube.com/watch?v=tb6EYiHtcXU) | 12:05 | What `strip`, `split`, `join` and `replace` each give back. The video ends with an exercise, which you can skip. |
| 3 | [LeetCoder] [ASCII, Unicode, UTF-8: Explained Simply](https://www.youtube.com/watch?v=DntKZ9xJ1sM) | 3:29 | Why one character can need more than one byte. |

**Total: 26 min 18 s, shown as 27 min.**

---

### 2. Read & practise (2 h 0 m)

Open each lesson, read it, type the examples into PyCharm and run them. Then do the exercises.

#### Section 1.1: Strings, indexing and slicing (about 45 min)

- Lesson: [Section 1.1](#section-1-1)
- Read all of it. Type in the examples as you go.
- Do the Level 1 exercises (1 to 6). Level 2 is optional.

#### Section 1.2: String methods and formatting (about 45 min)

- Lesson: [Section 1.2](#section-1-2)
- Read all of it. Pay most attention to `lower`, `strip`, `split`, `join` and the f-string format specs, because the Build task uses them.
- Do the Level 1 exercises (1 to 6). Level 2 is optional.

#### Section 1.3: ASCII and UTF-8 (about 30 min)

- Lesson: [Section 1.3](#section-1-3)
- Read all of it. Run the examples in the PyCharm Python Console.
- Do the Level 1 exercises (1 to 6). Level 2 is optional.

> **PyCharm note:** the **Python Console** tab at the bottom of PyCharm is a quick place to test one line of code. It uses UTF-8, so characters such as `é` show correctly.

---

### 3. Concepts Bridge (30 min)

Everything in a computer is numbers. Text is the worked example. You decode a few code points by hand and predict the difference between the length of text and the length of its bytes.

- [Open the Week 1 Bridge](#week-1-bridge)

---

### 4. Build (2 h)

Build a letter-frequency analyser. It reads a short passage, counts the letters, and prints a table and a bar chart. You also write a short note about what you found. This is your portfolio item for this week.

- [Open the Week 1 practice task](#week-1-practice)

---

### 5. Quiz (15 min)

Take the Canvas quiz for Week 1 after you finish the Build. It has 6 questions, drawn from a pool. It is marked automatically.

### Portfolio this week

Submit at the end of the week, in your portfolio folder:

- `starter.py` (your completed functions and `main()`)
- `frequency_note.txt` (five or six sentences about your results)

Your tutor marks the portfolio. The quiz is marked automatically.

---

### Optional (not required)

Only do these if you have time left after the core work.

**More videos: Data with Baraa, Python Ultimate Course**

This lesson is from a different presenter and is much longer than the Watch block, so treat it as extra explanation. Find it in the [playlist](https://www.youtube.com/playlist?list=PLNcg_FV9n7qZGfFl2ANI_zISzNp257Lwn).

- [Data with Baraa] [Python String Functions Explained](https://www.youtube.com/watch?v=Yveo5hCrGLE&list=PLNcg_FV9n7qZGfFl2ANI_zISzNp257Lwn) (1:14:37)

**Lesson sections**
- Level 2 exercises in Sections 1.1, 1.2 and 1.3.

**Build stretch**
- Change `main()` so it prints all 26 letters, not just the top 10.
- Add a `count_words(text)` function that returns how many words the passage has.

**Reading**
- Python Software Foundation (2026) *Unicode HOWTO*. Available at: https://docs.python.org/3/howto/unicode.html (Accessed: 11 November 2026).
- Python Software Foundation (2026) *Built-in Types: text sequence type (str)*. Available at: https://docs.python.org/3/library/stdtypes.html (Accessed: 11 November 2026).

---

## 1.1 Strings, indexing and slicing {#section-1-1}

The main examples are also in [1.1_code/strings_demo.py](files/code/1.1/strings_demo.py).

### Why this matters

Most data starts life as text. A line in a log file is text. A row in a spreadsheet export is text. A password typed by a user is text.

Here is one line from a made-up system log:

```output
2026-11-09 07:13:45 LOGIN user01
```

To a person, it has four parts: a date, a time, an event and a user name. To Python, it is one long string. Before you can count logins or find a busy hour, you must cut the string into its parts. This section shows you how to do that by position.

### A string is a sequence of characters

In Part 1 you used strings as whole values, such as a name or a message. A **string** is really a **sequence**, which means an ordered row of items. Each item is one **character**. A character is a single letter, digit, space or symbol.

`len()` tells you how many characters a string has. Spaces and punctuation count too.

```python
word = "Python"
print(len(word))

line = "2026-11-09 07:13:45 LOGIN user01"
print(len(line))

empty = ""
print(len(empty))
```

```output
6
32
0
```

A string with no characters, `""`, is called an **empty string**. Its length is 0.

### Indexing: picking one character

Every character has a position number, called its **index**. Python counts from 0, the same as it does for lists.

| Character | P | y | t | h | o | n |
|---|---|---|---|---|---|---|
| Index | 0 | 1 | 2 | 3 | 4 | 5 |
| Negative index | -6 | -5 | -4 | -3 | -2 | -1 |

Put the index in square brackets after the string.

```python
word = "Python"
print(word[0])
print(word[1])
print(word[5])
```

```output
P
y
n
```

A **negative index** counts from the end. `-1` is the last character, `-2` is the one before it, and so on. This is handy when you do not know how long the string is.

```python
word = "Python"
print(word[-1])
print(word[-2])
print(word[len(word) - 1])
```

```output
n
o
n
```

The last index is always `len(word) - 1`, because counting starts at 0. If you ask for an index that does not exist, Python stops with an `IndexError`.

```python
word = "Python"
print(word[6])
```

```output
IndexError: string index out of range
```

### Slicing: cutting out a piece

A **slice** is a piece of a string. You write `[start:stop]`. The slice begins at index `start` and ends just **before** index `stop`. The character at `stop` is not included.

```python
word = "Python"
print(word[0:2])
print(word[2:6])
```

```output
Py
thon
```

An easy check: `stop - start` is the length of the slice. `word[2:6]` has 6 − 2 = 4 characters.

You can leave out either number. No `start` means "from the beginning". No `stop` means "to the end".

```python
word = "Python"
print(word[:2])
print(word[2:])
print(word[-3:])
print(word[:])
```

```output
Py
thon
hon
Python
```

Now cut up the log line. The date is the first 10 characters. The time starts at index 11 and is 8 characters long. The user name is the last 6 characters.

```python
line = "2026-11-09 07:13:45 LOGIN user01"

date = line[:10]
time = line[11:19]
user = line[-6:]
hour = line[11:13]

print(date)
print(time)
print(user)
print(hour)
```

```output
2026-11-09
07:13:45
user01
07
```

Notice that `hour` is the string `"07"`, not the number 7. A slice of a string is always a string. Use `int(hour)` if you need a number.

Slices are forgiving. If `stop` is past the end, Python just stops at the end. There is no error.

```python
word = "Python"
print(word[2:100])
print(word[10:20] == "")
```

```output
thon
True
```

### Slicing with a step

A slice can have a third number, the **step**: `[start:stop:step]`. The step says how far to jump each time. A step of 2 takes every second character.

```python
digits = "0123456789"
print(digits[::2])
print(digits[1::2])
print(digits[2:9:3])
```

```output
02468
13579
258
```

A step of `-1` walks backwards. `[::-1]` is a quick way to reverse a string.

```python
word = "Python"
print(word[::-1])
```

```output
nohtyP
```

### Strings are immutable

**Immutable** means "cannot be changed after it is made". A list is mutable: you can replace one item. A string is immutable: you cannot replace one character.

```python
word = "Python"
word[0] = "J"
```

```output
TypeError: 'str' object does not support item assignment
```

Instead, you build a **new** string and give it a name. Here the new string is `"J"` joined to a slice of the old one.

```python
word = "Python"
new_word = "J" + word[1:]
print(new_word)
print(word)
```

```output
Jython
Python
```

The old string is still there, unchanged. This matters in the next section too: every string method returns a new string, and never changes the original.

Why would a language do this? It makes strings safe to share. If you pass a user name into a function, the function cannot quietly alter it.

### Looping over a string

Because a string is a sequence, a `for` loop visits it one character at a time.

```python
for character in "log":
    print(character)
```

```output
l
o
g
```

You can use this to count things. This loop counts the digits in the log line.

```python
line = "2026-11-09 07:13:45 LOGIN user01"

digit_count = 0
for character in line:
    if character in "0123456789":
        digit_count = digit_count + 1

print(digit_count)
```

```output
16
```

Your Build task this week uses the same pattern to count letters.

### Checking with in

`in` asks "is this smaller string somewhere inside the bigger one?". The answer is `True` or `False`. The smaller string can be one character or many. It is often called a **substring**, which means a string inside another string.

```python
line = "2026-11-09 07:13:45 LOGIN user01"

print("LOGIN" in line)
print("LOGOUT" in line)
print("login" in line)
print("x" not in line)
```

```output
True
False
False
True
```

Upper case and lower case are different characters, so `"login"` is not found. Section 1.2 shows how to deal with that.

`in` is a simple way to filter lines of a log.

```python
lines = [
    "2026-11-09 07:13:45 LOGIN user01",
    "2026-11-09 07:15:02 ERROR disk nearly full",
    "2026-11-09 07:16:30 LOGOUT user01",
]

for line in lines:
    if "ERROR" in line:
        print(line[20:])
```

```output
ERROR disk nearly full
```

### Common mistakes

- **Counting from 1.** The first character is `text[0]`. `text[1]` is the second.
- **Asking for `text[len(text)]`.** The last index is `len(text) - 1`. Use `text[-1]` for the last character.
- **Expecting the `stop` character in a slice.** `text[0:3]` gives indexes 0, 1 and 2. Index 3 is left out.
- **Trying to change a character.** `text[0] = "x"` is a `TypeError`. Build a new string instead.
- **Forgetting that a slice is still a string.** `"07" + 1` fails. Convert with `int()` first.
- **Forgetting that case matters.** `"error" in "ERROR found"` is `False`.

::::::::::::::::::::::::::::::::::::: challenge

### Exercises: Level 1

Use this string for exercises 1 to 4.

```python
record = "203.0.113.45 FAILED admin 02:14"
```

1. Print the length of `record`. Then print its first character and its last character.
2. Use a slice to print the time (`02:14`). Use a negative index so it still works if the start of the line gets longer.
3. Use slices to print the IP address (`203.0.113.45`) and the word `FAILED`.
4. Use `in` to print `True` if the record contains `FAILED`. Then check for `OK`.
5. Write a `for` loop that counts how many times the character `"."` appears in `"203.0.113.45"`. Print the count. (It should be 3.)
6. Make a new string from `"backup"` that starts with a capital B, without typing the whole word again. Use a slice.

::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::: challenge

### Exercises: Level 2

1. A **palindrome** is a word that reads the same backwards, such as `"level"`. Write a function `is_palindrome(word)` that returns `True` or `False`. Use `[::-1]`.
2. Write a function `mask(card)` that takes a string of digits such as `"1234567812345678"` and returns a string of the same length where every character except the last four is `*`. Use `len`, a slice and the `*` operator on a string.
3. Print every second character of `"s3e1c8r9e2t"` starting from index 0. What word appears?

::::::::::::::::::::::::::::::::::::::::::::::::

## 1.2 String methods and formatting {#section-1-2}

The main examples are also in [1.2_code/methods_demo.py](files/code/1.2/methods_demo.py) and [1.2_code/table_demo.py](files/code/1.2/table_demo.py).

### Why this matters

Text from the real world is messy. One person types `Perth`, another types ` perth ` with spaces, and a third types `PERTH`. To a computer these are three different strings. If you count sales by city without tidying first, you get three cities instead of one.

The same problem appears in security work. A log might record `Admin`, `admin` and `ADMIN`. They are the same account, and a report must treat them as one.

This section gives you the tools to tidy text, pull it apart, ask questions about it, and print results in neat columns.

### What a string method is

In Part 1 you met **methods**: functions that belong to an object and are called with a dot, such as `library.add_book(book)`. Strings have methods too. You write the string, a dot, then the method name.

Remember from Section 1.1 that strings are immutable. So a string method never changes the string. It **returns a new string** (or another value). If you want to keep the result, store it in a variable.

```python
city = "Perth"
city.upper()
print(city)

shout = city.upper()
print(shout)
```

```output
Perth
PERTH
```

The second line did the work and then threw the answer away. Only the version that stored the result was useful.

### Changing case: lower and upper

`lower()` returns the text in lower case. `upper()` returns it in upper case. Characters that are not letters stay the same.

```python
name = "Admin01"
print(name.lower())
print(name.upper())
```

```output
admin01
ADMIN01
```

The most common use is comparing text without caring about case. Convert both sides the same way first.

```python
typed = "ADMIN"
stored = "admin"

print(typed == stored)
print(typed.lower() == stored.lower())
```

```output
False
True
```

### Tidying: strip and replace

`strip()` removes **whitespace** from both ends of a string. Whitespace means characters you cannot see: spaces, tabs and the new-line character `\n`. It does not touch spaces in the middle.

```python
raw = "   Jack Wilson  \n"
tidy = raw.strip()

print(len(raw))
print(len(tidy))
print(tidy)
```

```output
17
11
Jack Wilson
```

`replace(old, new)` returns a copy where every `old` is swapped for `new`. To delete something, replace it with the empty string `""`.

```python
date = "09/11/2026"
print(date.replace("/", "-"))

phone = "08 5550 0123"
print(phone.replace(" ", ""))
```

```output
09-11-2026
0855500123
```

Each method returns a string, so you can call another method on the result straight away. This is called **chaining**. Read it from left to right.

```python
raw = "  PERTH \n"
print(raw.strip().lower())
```

```output
perth
```

### Splitting and joining: split and join

`split()` cuts a string into a **list** of smaller strings. With no argument, it cuts at whitespace, and it treats several spaces in a row as one gap.

```python
line = "2026-11-09 07:13:45 LOGIN user01"
parts = line.split()

print(parts)
print(len(parts))
print(parts[3])
```

```output
['2026-11-09', '07:13:45', 'LOGIN', 'user01']
4
user01
```

This is often easier than slicing by position, because it still works when a part changes length.

You can give `split` a **separator**, which is the text to cut at.

```python
row = "Perth,Notebook,12,6.50"
fields = row.split(",")
print(fields)

time = "07:13:45"
hour = time.split(":")[0]
print(hour)
```

```output
['Perth', 'Notebook', '12', '6.50']
07
```

Every piece is still a string. `fields[2]` is `"12"`, so use `int(fields[2])` before doing sums.

`join()` is the opposite of `split()`. It glues a list of strings into one string. The string you call it on is the glue that goes between the items.

```python
words = ["server", "room", "door"]

print(" ".join(words))
print("-".join(words))
print(",".join(words))
print("".join(words))
```

```output
server room door
server-room-door
server,room,door
serverroomdoor
```

It looks backwards at first: the separator comes before the dot, and the list goes in the brackets. `join` only works when every item in the list is a string.

### Asking questions: startswith, endswith, find and count

These methods do not make new text. They tell you something about the text.

`startswith(text)` and `endswith(text)` return `True` or `False`.

```python
filename = "report_2026.csv"
print(filename.endswith(".csv"))
print(filename.startswith("report"))
print(filename.endswith(".txt"))
```

```output
True
True
False
```

`find(text)` returns the **index** where the text first appears. If the text is not there, it returns `-1`. It does not raise an error.

```python
email = "olivia@example.com"
at = email.find("@")

print(at)
print(email[:at])
print(email[at + 1:])
print(email.find("#"))
```

```output
6
olivia
example.com
-1
```

Here `find` and a slice work together: find the position, then cut there.

`count(text)` returns how many times the text appears.

```python
address = "203.0.113.45"
print(address.count("."))

sentence = "the report said the backups finished"
print(sentence.count("the"))
print(sentence.count("e"))
```

```output
3
2
4
```

### Checking the kind of text: isalpha and isdigit

`isalpha()` returns `True` if every character is a letter. `isdigit()` returns `True` if every character is a digit. Both return `False` for an empty string.

```python
print("Perth".isalpha())
print("Perth 6000".isalpha())
print("6000".isdigit())
print("60.5".isdigit())
print("-5".isdigit())
print("".isdigit())
```

```output
True
False
True
False
False
False
```

A space, a full stop or a minus sign is not a digit, so `"60.5"` and `"-5"` both fail. `isdigit()` is a good check for "whole number with no sign", such as a postcode or a year.

```python
answer = "2026"
if answer.isdigit():
    year = int(answer)
    print(year + 1)
else:
    print("Please type digits only.")
```

```output
2027
```

### Formatting numbers with f-strings

You used f-strings in Part 1: an `f` before the quote, and values inside `{ }`. You can add a **format spec** after a colon inside the braces. A format spec is a short code that says how the value should look.

| Format spec | Meaning | Example | Result |
|---|---|---|---|
| `:.2f` | 2 decimal places | `f"{3.14159:.2f}"` | `3.14` |
| `:,` | commas between thousands | `f"{1234567:,}"` | `1,234,567` |
| `:>8` | right-align in 8 characters | `f"{'abc':>8}"` | five spaces, then `abc` |
| `:<10` | left-align in 10 characters | `f"{'abc':<10}"` | `abc`, then seven spaces |

The number of characters a value is given is called its **width**. If the value is shorter than the width, Python pads it with spaces.

```python
price = 6.5
total = 1234567.891

print(f"{price:.2f}")
print(f"{total:.1f}")
print(f"{total:,}")
print(f"{total:,.2f}")
```

```output
6.50
1234567.9
1,234,567.891
1,234,567.89
```

`:.2f` rounds for display only. The variable `price` still holds `6.5`.

Alignment is easier to see with a marker at each end.

```python
word = "abc"
print(f"[{word:>8}]")
print(f"[{word:<8}]")
print(f"[{42:>8}]")
print(f"[{3.14159:>8.2f}]")
```

```output
[     abc]
[abc     ]
[      42]
[    3.14]
```

The last line combines two specs: width 8, right-aligned, with 2 decimal places. The order is always alignment, then width, then `.2f`.

### Lining up a table

Print each column with a fixed width and the rows line up. Text usually looks best left-aligned. Numbers look best right-aligned, so the decimal points sit under each other.

```python
rows = [
    ("Notebook", 120, 6.5),
    ("Pen pack", 85, 4.0),
    ("Desk lamp", 9, 32.0),
]

print(f"{'Product':<10}{'Units':>8}{'Price':>8}")
print("-" * 26)
for product, units, price in rows:
    print(f"{product:<10}{units:>8}{price:>8.2f}")
```

```output
Product      Units   Price
--------------------------
Notebook       120    6.50
Pen pack        85    4.00
Desk lamp        9   32.00
```

Three things to notice:

- The header row uses the same widths as the data rows. The header words are in single quotes because the f-string itself uses double quotes.
- `"-" * 26` repeats a string. 26 is the three widths added together: 10 + 8 + 8.
- `for product, units, price in rows` unpacks each tuple into three names, as you did with tuples in Part 1.

Your Build task prints a table like this for letter counts.

### Common mistakes

- **Not storing the result.** `name.strip()` alone does nothing useful. Write `name = name.strip()`.
- **Forgetting the brackets.** `name.upper` without `()` does not call the method.
- **Calling `join` the wrong way round.** It is `", ".join(items)`, not `items.join(", ")`.
- **Joining numbers.** `"-".join([1, 2, 3])` is a `TypeError`. The items must be strings.
- **Expecting `find` to return `False`.** It returns `-1` when nothing is found. Test with `== -1`, or use `in`.
- **Treating split pieces as numbers.** `"12,6.50".split(",")` gives strings. Convert with `int()` or `float()`.
- **Using a text format on a number spec.** `f"{'abc':.2f}"` is a `ValueError`, because `.2f` only works for numbers.

::::::::::::::::::::::::::::::::::::: challenge

### Exercises: Level 1

1. Start with `raw = "  Olivia.Thompson@Example.COM \n"`. Print a tidy version with no spaces at the ends, all in lower case.
2. From your tidy address, use `find` and slices to print the part before the `@` and the part after it.
3. Start with `line = "198.51.100.7 GET /index.html 200"`. Use `split()` to print the IP address and the last part. Then print the last part plus 1, as a number.
4. Start with `tags = ["urgent", "backup", "disk"]`. Use `join` to print `urgent; backup; disk`.
5. Print `True` or `False` for each of these: does `"photo.JPG"` end with `.jpg` when you ignore case? Is `"6000"` all digits? Is `"WA6000"` all letters?
6. Print this table with f-string format specs. Names are left-aligned in 12 characters. Amounts are right-aligned in 10 characters, with commas and 2 decimal places.

   ```output
   Name            Amount
   Perth         1,250.50
   Fremantle       980.00
   Joondalup    12,004.75
   ```

::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::: challenge

### Exercises: Level 2

1. Write a function `initials(full_name)` that turns `"jack wilson"` into `"J.W."`. Use `split`, indexing, `upper` and `join`.
2. Write a function `is_time(text)` that returns `True` for text such as `"07:13"`: two digits, a colon, two digits. Use `len`, slices and `isdigit`. Do not worry about whether the hour is below 24.
3. Count how many words are in `"the  quiet   server room"` (there are extra spaces). Then build the same sentence with exactly one space between words, using `split` and `join`.

::::::::::::::::::::::::::::::::::::::::::::::::

## 1.3 ASCII and UTF-8 {#section-1-3}

The main examples are also in [1.3_code/encoding_demo.py](files/code/1.3/encoding_demo.py).

### Why this matters

Have you ever opened a file and seen `cafÃ©` where `café` should be? Nothing is wrong with the file. The program reading it guessed the wrong rule for turning stored numbers back into letters.

This happens all the time with real data. A customer list exported from one system shows broken names in another. A log search for a user name finds nothing, because the name is stored in a way the search did not expect. Once you know how text is stored, these problems stop being mysterious, and you can fix them.

### Every character has a number

A computer stores numbers, not letters. So every character is given a number. That number is called its **code point**.

`ord()` takes one character and returns its code point. `chr()` goes the other way: it takes a code point and returns the character.

```python
print(ord("A"))
print(ord("a"))
print(ord("0"))
print(ord(" "))
print(chr(65))
print(chr(97))
```

```output
65
97
48
32
A
a
```

Three things are worth noticing:

- `"A"` and `"a"` have different numbers. This is why upper case and lower case are different to Python.
- The character `"0"` has code point 48. The character is not the number zero.
- Even a space has a number.

The letters are in order, so the numbers go up by one each time.

```python
for character in "abc":
    print(character, ord(character))

print(chr(ord("a") + 1))
print(ord("a") - ord("A"))
```

```output
a 97
b 98
c 99
b
32
```

Each lower-case letter is exactly 32 above its upper-case partner. The order of the numbers is also why `"Zebra" < "apple"` is `True` in Python: `Z` is 90 and `a` is 97.

### ASCII: the first 128 characters

**ASCII** (say "ask-ee") is an early standard list of characters and their numbers. It has 128 characters, numbered 0 to 127.

| Code points | What they are |
|---|---|
| 0 to 31, and 127 | Control characters you cannot see, such as new line (10) and tab (9) |
| 32 | Space |
| 48 to 57 | The digits `0` to `9` |
| 65 to 90 | The upper-case letters `A` to `Z` |
| 97 to 122 | The lower-case letters `a` to `z` |
| The rest up to 126 | Punctuation and symbols, such as `!`, `@` and `~` |

ASCII covers plain English and nothing else. It has no `é`, no `ñ`, no `€`, and no Chinese, Arabic or Hindi letters.

```python
print(ord("é"))
print(ord("€"))
print("cafe".isascii())
print("café".isascii())
```

```output
233
8364
True
False
```

`isascii()` is a string method that returns `True` when every character is in the ASCII range.

### Unicode and UTF-8

**Unicode** is the modern list. It gives a code point to every character in every writing system, plus symbols and emoji. The first 128 code points are the same as ASCII, so old ASCII text is still valid.

A list of numbers is not enough, though. The numbers must be stored. Storage is measured in **bytes**. One byte holds a number from 0 to 255. (The Concepts Bridge this week explains bytes in more detail.) A code point such as 8364 does not fit in one byte.

An **encoding** is a rule for turning code points into bytes. **UTF-8** is the encoding used by most of the web and most modern files. Its rule is simple to describe:

| Character | Code point | Bytes in UTF-8 |
|---|---|---|
| ASCII characters, such as `A` | 0 to 127 | 1 |
| Accented Latin letters, such as `é` | 128 to 2,047 | 2 |
| Most other letters and symbols, such as `€` | 2,048 to 65,535 | 3 |
| Emoji and rare characters | above 65,535 | 4 |

So UTF-8 stores every character as 1 to 4 bytes. Plain English text uses 1 byte per character, exactly as in ASCII.

### Encoding and decoding

To **encode** is to turn a string into bytes. To **decode** is to turn bytes back into a string.

```python
word = "café"
data = word.encode("utf-8")

print(data)
print(type(data))
```

```output
b'caf\xc3\xa9'
<class 'bytes'>
```

The result is a **bytes** object. Python shows it with a `b` in front. Bytes that match an ASCII character are shown as that character, so you see `c`, `a` and `f`. The other bytes are shown as `\x` and two hex digits. (**Hex** is a short way to write a byte. The Bridge explains it.) Here `\xc3\xa9` is two bytes, and together they are the letter `é`.

Turn the bytes into a list to see the numbers.

```python
data = "café".encode("utf-8")
print(list(data))
```

```output
[99, 97, 102, 195, 169]
```

99, 97 and 102 are `c`, `a` and `f`. The pair 195, 169 is `é`.

`decode` reverses it.

```python
data = b"caf\xc3\xa9"
text = data.decode("utf-8")

print(text)
print(text == "café")
```

```output
café
True
```

### Characters are not bytes

`len()` of a string counts characters. `len()` of a bytes object counts bytes. They are equal only for pure ASCII text.

```python
word = "café"

print(len(word))
print(len(word.encode("utf-8")))

print(len("cafe"))
print(len("cafe".encode("utf-8")))

print(len("€".encode("utf-8")))
print(len("😀".encode("utf-8")))
```

```output
4
5
4
4
3
4
```

`"café"` has 4 characters, but `é` needs 2 bytes, so the encoded form is 5 bytes. The euro sign needs 3 bytes. An emoji needs 4.

This matters whenever a limit is given in bytes. A database field that holds "20 bytes" may not hold 20 characters.

### When the wrong encoding is used

Bytes do not carry a label saying which encoding made them. The program that reads them must be told, or it guesses. If it uses a different encoding from the one that wrote them, the text comes out wrong.

**Latin-1** is an older encoding where every byte is one character. Watch what happens when UTF-8 bytes are decoded as Latin-1.

```python
word = "café"
data = word.encode("utf-8")
wrong = data.decode("latin-1")

print(wrong)
print(len(wrong))
```

```output
cafÃ©
5
```

Latin-1 treated the two bytes of `é` as two separate characters: 195 is `Ã` and 169 is `©`. Text scrambled like this is called **mojibake** (a Japanese word, said "mo-jee-bah-keh"). No data was lost. The bytes were read with the wrong rule.

Because nothing was lost, this case can be undone by reversing the two steps.

```python
wrong = "cafÃ©"
fixed = wrong.encode("latin-1").decode("utf-8")
print(fixed)
```

```output
café
```

The mistake can also go the other way and stop the program. ASCII has no rule for `é`, so encoding it as ASCII raises an error.

```python
"café".encode("ascii")
```

```output
UnicodeEncodeError: 'ascii' codec can't encode character '\xe9' in position 3: ordinal not in range(128)
```

A `UnicodeEncodeError` or `UnicodeDecodeError` nearly always means "the encoding does not match the data".

### What this means for logs and data files

- **Say the encoding when you read a file.** The Build task this week gives you a ready-made function that opens the text file with `encoding="utf-8"`. If you leave the encoding out, Python uses your computer's default, which can differ between computers. Week 2 covers reading files properly.
- **Mojibake breaks searches.** If a name is stored as `RenÃ©e`, a search for `Renée` finds nothing. A report built on that search quietly misses records.
- **Text that looks the same may not be the same.** Two user names can look identical on screen but hold different code points. In security work, that is one way a fake name can pass for a real one. Comparing code points with `ord()` shows the difference.
- **Count in the right unit.** Size limits for files, messages and database fields are usually in bytes, not characters.

### Common mistakes

- **Mixing up `ord` and `chr`.** `ord` goes from character to number. `chr` goes from number to character.
- **Giving `ord` more than one character.** `ord("ab")` is a `TypeError`. It takes exactly one.
- **Thinking `"7"` is 7.** `ord("7")` is 55. Use `int("7")` to get the number 7.
- **Mixing strings and bytes.** `"abc" + b"def"` is a `TypeError`. Decode the bytes first.
- **Assuming one character is one byte.** That is true only for ASCII.
- **Guessing the encoding.** Find out what the file uses. If you have no other information, UTF-8 is the best first try.

::::::::::::::::::::::::::::::::::::: challenge

### Exercises: Level 1

1. Print the code points of `"Z"`, `"z"`, `"9"` and `"?"`. Then print the characters for code points 80, 121 and 33.
2. Write a `for` loop that prints each character of `"Log7!"` with its code point, one per line.
3. Without running it, predict `len("naïve")` and `len("naïve".encode("utf-8"))`. Then run both and check. (The letter `ï` is not ASCII.)
4. Encode `"Renée"` as UTF-8 and print the bytes as a list of numbers. Which two numbers are the `é`?
5. Make mojibake on purpose: encode `"Renée"` as UTF-8, decode it as Latin-1 and print the result. Then write the line that repairs it.
6. Use `isascii()` to test each name in `["user01", "Zoë", "admin"]`. Print each name with `True` or `False`.

::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::: challenge

### Exercises: Level 2

1. Write a function `shift_letter(letter)` that returns the next lower-case letter, using `ord` and `chr`. `"a"` gives `"b"`. Make `"z"` wrap around to `"a"`. (You will meet this idea again in Week 3.)
2. Write a function `byte_length(text)` that returns the number of UTF-8 bytes in a string. Use it to find which of `"Perth"`, `"Zürich"` and `"São Paulo"` has a different number of bytes from characters.
3. Write a function `non_ascii(text)` that returns a list of the characters in `text` that are not ASCII. Test it on `"The café serves crème brûlée"`.

### Further reading

- Python Software Foundation (2026) *Unicode HOWTO*. Available at: https://docs.python.org/3/howto/unicode.html (Accessed: 11 November 2026).

::::::::::::::::::::::::::::::::::::::::::::::::

## Concepts Bridge: Text Is Stored as Numbers {#week-1-bridge}

**Time: 30 minutes.** Reading 12 minutes, activities 13 minutes, checking the model answer 5 minutes.

### Why this matters

Section 1.3 showed that every character has a code point, and that UTF-8 turns code points into bytes. This bridge steps back and asks a bigger question. What is a computer actually storing?

The answer is the same for everything: **numbers**. Text, photos, music, programs and logs are all numbers underneath. Text is the easiest example to see. Once you see it, you can understand why a file can look right on screen and still be different inside. That idea comes back in Week 3, when you compare files by their hashes.

### Everything is numbers

A computer's memory is made of tiny switches that are either off or on. One switch holds a **bit**, which is a 0 or a 1. A group of 8 bits is a **byte**.

With 8 bits there are 2 × 2 × 2 × 2 × 2 × 2 × 2 × 2 = 256 different patterns. So a byte holds a whole number from 0 to 255. Everything else is built from bytes. A file is a long row of bytes. The meaning of the bytes depends on the rule used to read them.

The same byte can mean different things:

| Rule used to read it | The byte 65 means |
|---|---|
| A number | sixty-five |
| ASCII or UTF-8 text | the letter `A` |
| A shade of grey in a picture | a fairly dark grey |

The byte does not know which one it is. The program decides. This is exactly why the wrong encoding in Section 1.3 produced mojibake: the bytes were fine, and the rule was wrong.

#### Writing a byte three ways

People write the same byte in different ways. All three of these are the number sixty-five.

| Way of writing | Value | In Python |
|---|---|---|
| Decimal (the usual way) | 65 | `65` |
| Binary (bits) | 01000001 | `bin(65)` gives `'0b1000001'` |
| Hex (hexadecimal) | 41 | `hex(65)` gives `'0x41'` |

**Hex** counts in sixteens. It uses the digits 0 to 9 and then the letters `a` to `f` for ten to fifteen. Two hex digits always fit one byte, from `00` (0) to `ff` (255). That makes hex a short way to write bytes. Binary needs 8 digits for the same byte. In Python, `0x` in front of a number says "this is hex".

```python
print(hex(255))
print(0x41)
print(chr(0x41))
print("AB".encode("utf-8").hex())
print("café".encode("utf-8").hex())
```

```output
0xff
65
A
4142
636166c3a9
```

In the last line, each pair of hex digits is one byte: `63 61 66 c3 a9`. That is the five bytes of `café` from Section 1.3. Security tools often show data like this, so it helps to be able to read it.

### Same on screen, different inside

Two pieces of text can look identical and still be different bytes. Here is an example. The letter `é` can be stored in two ways:

- as one code point, `é` (code point 233), or
- as a plain `e` followed by a separate "combining accent" code point (code point 769) that draws the accent on top.

```python
one = "café"
two = "café"

print(one == two)
print(len(one), len(two))
print(len(one.encode("utf-8")), len(two.encode("utf-8")))
```

```output
False
4 5
5 6
```

(`é` is a way to write a code point by its hex number inside a string.) On screen, both show as `café`. Python says they are not equal, because the numbers are different. A search for one will not find the other.

Other ways two files can look the same but differ:

- one is saved as UTF-8 and the other as Latin-1,
- one has a hidden space or tab at the end of a line,
- one uses a letter from another alphabet that looks like an English letter.

The rule for your own work is simple. **When two things should match but do not, compare the numbers, not what you see.** Use `ord`, `encode` and `len` to look inside.

::::::::::::::::::::::::::::::::::::: challenge

### Activity 1: decode by hand (6 minutes)

Do the first two before you run any code. The letter `a` is 97, `A` is 65, and the letters go up by one each, in alphabet order.

1. These are code points. Write the word they spell: `83, 101, 99, 117, 114, 101`. (Start from `a` = 97 and count along the alphabet. `S` is 83.)
2. These are bytes written in hex. Write the word: `48 69`. (Hint: `0x48` is 72, and `H` is 72.)
3. Now check both answers with Python. For the first, use `chr()` on each number. For the second, try `bytes([0x48, 0x69]).decode("utf-8")`.

### Activity 2: text versus bytes (7 minutes)

For each string, predict two numbers: `len(text)` and `len(text.encode("utf-8"))`. Write your guesses down first.

| Text | Your guess: characters | Your guess: bytes |
|---|---|---|
| `"Log7"` | | |
| `"naïve"` | | |
| `"€5"` | | |
| `"Zoë"` | | |

Then run the code in the Python Console and check. For any guess that was wrong, work out which character needed more than one byte.

:::::::::::::::: solution

### Model answer

**Activity 1**

1. The word is `Secure`. `S` is 83, `e` is 101, `c` is 99, `u` is 117, `r` is 114 and `e` is 101. `"".join(chr(n) for n in [83, 101, 99, 117, 114, 101])` prints it, or call `chr` on each number one at a time.
2. The word is `Hi`. `0x48` is 72, which is `H`. `0x69` is 105, which is `i`. `bytes([0x48, 0x69]).decode("utf-8")` gives `Hi`.

**Activity 2**

| Text | Characters | Bytes | Why |
|---|---|---|---|
| `"Log7"` | 4 | 4 | All ASCII, so 1 byte each. |
| `"naïve"` | 5 | 6 | `ï` needs 2 bytes. |
| `"€5"` | 2 | 4 | `€` needs 3 bytes and `5` needs 1. |
| `"Zoë"` | 3 | 4 | `ë` needs 2 bytes. |

The general rule: the byte count equals the character count only when every character is ASCII.

:::::::::::::::::::::::::
::::::::::::::::::::::::::::::::::::::::::::::::

### Further reading

- Python Software Foundation (2026) *Unicode HOWTO*. Available at: https://docs.python.org/3/howto/unicode.html (Accessed: 11 November 2026).
- Python Software Foundation (2026) *Built-in Types: bytes objects*. Available at: https://docs.python.org/3/library/stdtypes.html (Accessed: 11 November 2026).

## Practice task: Letter-Frequency Analyser {#week-1-practice}

:::::::::::::::::::::::::::::::::::::::: callout

### Files for this task

The easiest way to get every file is the [course zip file](data/course-data.zip) from the Setup page. Unzip it and open the folder in PyCharm. The programs find the data files by their place in that folder, so keep the folder layout. You can also download single files here:

- [starter.py](files/week-1/starter.py)
- [solution.py](files/week-1/solution.py)
- [test_solution.py](files/week-1/test_solution.py)

:::::::::::::::::::::::::::::::::::::::::::::::::::

**Time: about 2 hours.** This is your portfolio item for Week 1. Your tutor marks it at the end of the week.

### Goal

Write a program that counts how often each letter appears in a short passage, then prints a table of the ten most common letters with a bar chart made of `#` characters.

Counting how often things appear is called a **frequency count**. It is one of the most common jobs in data and security work. Here you do it with letters.

The passage is `assets/files/sample_text.txt`. It is a short story called "The Quiet Server Room". It contains the word `café`, with an `é`. That is on purpose.

### Files

| File | What it is |
|---|---|
| `starter.py` | A ready-made `read_text` function, and your functions to fill in. |
| `test_solution.py` | Tests for the functions. |
| `solution.py` | A model answer. Try the task yourself before you look. |

You also write `frequency_note.txt` (see below).

### Steps

1. **(10 min)** Open `starter.py` and read it. Find `read_text(path)`. Leave it as it is. It opens the file with `encoding="utf-8"`, and Week 2 explains how it works. Run the file. It should run without errors and print nothing, because `main()` is empty. Also open `sample_text.txt` and read the passage.
   - Near the bottom you will see `if __name__ == "__main__":`. Leave those two lines as they are.
2. **(20 min)** Write `clean(text)` and `count_letters(text)`.
   - `clean` returns the text in lower case, so `E` and `e` are counted together.
   - `count_letters` returns a dictionary with all 26 letters `a` to `z` as keys. Each value is how often that letter appears.
   - Count **only** the 26 letters `a` to `z`. Ignore digits, spaces, punctuation and letters such as `é`. This keeps the table to one fixed alphabet, and it is a choice you will explain in your note.
3. **(15 min)** Write `total_letters(counts)` and `percentages(counts)`.
   - `percentages` returns a dictionary of letter to percent, rounded to 1 decimal place. If the total is 0, give 0.0 for every letter, so the function does not crash.
4. **(15 min)** Write `top_letters(counts, n)`.
   - It returns a list of `(letter, count)` tuples for the `n` biggest counts.
   - The biggest count comes first. Letters with the same count go in alphabetical order.
5. **(15 min)** Write `format_row(letter, count, percent)` and `bar(percent)`.
   - `format_row` returns one line using f-string format specs from Section 1.2.
   - `bar` returns one `#` for each whole percent. Use `int(percent)` to drop the part after the decimal point.
6. **(15 min)** Write `main()`. Keep all `print()` calls inside `main()`. Print a heading, the number of characters in the file, the number of letters counted, a header row, and then the top 10 letters with their bars.
7. **(10 min)** Run the tests (see "Check your work"). Fix any that fail.
8. **(15 min)** Write your note in `frequency_note.txt` (see below).
9. **(5 min)** Tidy up. Remove any `print()` lines you added for testing. Check that the checklist is complete.

### Example run

```output
Letter frequency: sample_text.txt
Characters in the file: 987
Letters a to z counted: 779

Letter   Count       %  Bar
------------------------------------
e           96    12.3  ############
a           67     8.6  ########
s           64     8.2  ########
t           62     8.0  ########
o           60     7.7  #######
n           53     6.8  ######
i           52     6.7  ######
r           46     5.9  #####
h           40     5.1  #####
d           35     4.5  ####
```

Your wording and layout can differ a little. The numbers should match.

### Hints

- Start `counts = {}`, then loop over `ALPHABET` and set `counts[letter] = 0` for each letter.
- Inside a loop over `clean(text)`, use `if character in ALPHABET:` to skip everything that is not `a` to `z`.
- `sum(counts.values())` adds up all the values in a dictionary.
- `round(3.14159, 1)` gives `3.1`.
- `counts.items()` gives `(letter, count)` pairs. To sort them, use `sorted(pairs, key=...)`. The key can be a `lambda` that returns a tuple, such as `(a, b)`. Python sorts by `a` first and then `b`. Putting a minus sign in front of a number, such as `-count`, sorts biggest first.
- A slice such as `pairs[:n]` keeps the first `n` items.
- Format specs: `f"{letter:<8}"` is left-aligned in 8 characters. `f"{count:>6}"` is right-aligned in 6. `f"{percent:>8.1f}"` is right-aligned in 8 with one decimal place.
- `"#" * 5` gives `"#####"`.
- Functions that only take values and return values are **pure** and easy to test. Keep `print()` inside `main()` only.

### Your note: frequency_note.txt

Write five or six sentences in a plain text file called `frequency_note.txt`, in your own words. Guiding questions:

1. Which letters are the most common in the passage?
2. Is that what you expected for English text? Why or why not?
3. Why did your program leave out `é`, and how would you change it to include `é`?
4. Name one way letter frequency is used in security or data work. (A hint: simple ciphers, such as the Caesar cipher you will meet in Week 3, keep the letter pattern of the original text, so counting letters can help you recognise them. You do not need to know how a cipher works yet.)

A longer passage would give more reliable percentages than a short one. You could mention that too.

### Check your work

- [ ] Run the tests. In PyCharm, right-click `test_solution.py` and choose **Run pytest**, or in the terminal: `python -m pytest weeks/week-1/practice`.
- [ ] To test your own file, open `test_solution.py` and change `import solution as freq` to `import starter as freq`.
- [ ] `starter.py` runs without errors and prints a table that matches the example run.
- [ ] `count_letters` returns exactly 26 keys, and `é`, digits and spaces are not counted.
- [ ] `count_letters("")` does not crash, and `percentages` on an empty count does not crash.
- [ ] All the `print()` calls are inside `main()`.
- [ ] You did not change `read_text`.
- [ ] `frequency_note.txt` has five or six sentences in your own words.

:::::::::::::::::::::::::::::::::::::: keypoints

- Each week has four blocks: Watch, Read & practise, Concepts Bridge and Build.
- A string is a sequence of characters, counted from 0.
- A slice [start:stop:step] makes a new string and stops before stop.
- Strings cannot be changed; every method gives you a new string.
- Tidy text first (lower, strip) before you count or compare it.
- split makes a list of pieces; join puts them back together.
- f-string format specs such as :>8 and :.2f line up columns.
- Every character has a number; ASCII covers 128 of them.
- UTF-8 stores each character in 1 to 4 bytes.
- Always say which encoding a file uses; the wrong one gives garbled text.
- Everything in a computer is stored as numbers.
- A byte is a number from 0 to 255; hexadecimal is a short way to write it.
- Small, pure functions that take text and return values are easy to test.

::::::::::::::::::::::::::::::::::::::::::::::::
