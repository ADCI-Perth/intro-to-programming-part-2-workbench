---
title: 'Week 3: Validation, integrity and a simple cipher'
teaching: 111
exercises: 166
---

:::::::::::::::::::::::::::::::::::::: questions

- What will I learn in Week 3, and how should I spend my 6 hours?
- How do I check data before I trust it?
- How can I tell whether a file or a piece of text has changed?
- How does a simple cipher scramble text?
- What is the difference between hashing, encryption and encoding?
- Can I check a password and explain what my checker cannot know?

::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::: objectives

- Plan your study time for the week using the time plan.
- Check for empty values, type, range, length and allowed characters.
- Use any and all to test the characters of a string.
- Return a list of problems instead of stopping at the first one.
- Calculate a SHA-256 hash of text and of a file.
- Explain three properties of a hash.
- Explain why systems store a hash of a password, not the password.
- Shift letters with ord, chr and the remainder operator.
- Encrypt and decrypt text with a key.
- Choose hashing, encryption or encoding for a given job and give a reason.
- Build a password strength checker, with an optional file integrity checker.

::::::::::::::::::::::::::::::::::::::::::::::::

## Week 3 overview {#week-3-overview}

**Theme:** check data before you trust it, use a hash to show that data has not changed, and learn what a simple cipher does (and why it is not security).

**What you need from earlier weeks:** strings and `ord`, `chr`, `encode` (Week 1); reading text files with `with open(...)` (Week 2); `try` / `except`, functions and tests (Part 1).

### Learning goals

By the end of this week you can:

1. Write checks for presence, type, range, length and allowed characters, using `any` and `all`, and return a list of problems.
2. Use `hashlib` to make a SHA-256 hash, and explain what a hash can and cannot do.
3. Write and test a Caesar cipher, and explain why it is not secure.
4. Explain the difference between hashing, encryption and encoding, and say which one suits a job.

### Time plan (under 6 hours)

| Block | Time | What you do |
|---|---|---|
| Watch | 37 min | Three videos (below) |
| Read & practise | 1 h 30 m | Sections 3.1 (35 min), 3.2 (30 min) and 3.3 (25 min), with Level 1 exercises |
| Concepts Bridge | 30 min | [Hashing, encryption and encoding: what each is for](#week-3-bridge) |
| Build | 2 h | [Password strength checker](#week-3-practice), your portfolio item for this week |
| Quiz | 15 min | Canvas quiz, 6 questions |
| **Total** | **4 h 52 min** | Under the 6 h cap |

### Watch (37 min)

Watch these in order. Pause and try the code yourself in PyCharm. The videos are from different presenters, so the style changes from video to video.

| # | Video | Length | Look out for |
|---|---|---|---|
| 1 | [Fabio Musanni] [How to Validate User Inputs in Python](https://www.youtube.com/watch?v=LUWyA3m_-r0) | 14:14 | What validation is, and the kinds of check you can make on input. |
| 2 | [The Coding Gopher] [Hashing Explained (SHA-256, MD5)](https://www.youtube.com/watch?v=R_mOWu3s6y4) | 11:27 | Fixed length, the same input gives the same hash, and a tiny change gives a very different hash. |
| 3 | [NeuralNine] [Simple Caesar Encryption in Python](https://www.youtube.com/watch?v=JEsUlx0Ps9k) | 10:27 | How the shift works. The Caesar cipher is a teaching cipher. It is not secure. |

**Total: 36 min 8 s, shown as 37 min.**

### Read & practise (1 h 30 m)

Open each lesson, read it, type out the examples and run them. Do not just copy and paste. The code files in each `*_code` folder are there to compare with your own.

#### Section 3.1: Checking input (35 min)

Lesson: [Section 3.1: Checking input](#section-3-1). Code: [lessons/3.1_code/](files/code/3.1/).

- Read all of it. `any` and `all` are new built-in functions, so take your time with them.
- Do the **Level 1** exercises (1 to 5), about 3 minutes each.

#### Section 3.2: Hashing with `hashlib` (30 min)

Lesson: [Section 3.2: Hashing with `hashlib`](#section-3-2). Code: [lessons/3.2_code/](files/code/3.2/).

- Read all of it. Binary file mode (`"rb"`) is new, and the lesson explains it.
- The "reading in chunks" part is optional detail.
- Do the **Level 1** exercises (1 to 5).

#### Section 3.3: The Caesar cipher (25 min)

Lesson: [Section 3.3: The Caesar cipher](#section-3-3). Code: [lessons/3.3_code/](files/code/3.3/).

- Read all of it, and remember that this cipher is a teaching tool and is not secure.
- Do the **Level 1** exercises (1 to 5).

**PyCharm note:** the code files find the course folder from their own location, so you can run them with a right-click and **Run**. Run the lesson code first, then try your own versions.

### Concepts Bridge (30 min)

Go to [bridge.md](#week-3-bridge). It compares hashing, encryption and encoding in one table, and has two short activities.

### Build (2 h)

Go to [practice/README.md](#week-3-practice). You build a password strength checker with small, testable functions, run the tests, and write a short note. An integrity checker is an optional stretch. This is your portfolio item for Week 3.

### Quiz (15 min)

Take the Canvas quiz for Week 3 after you finish the Build. It has 6 questions, drawn from a pool. It is marked automatically.

### Portfolio this week

Submit at the end of the week, in your portfolio folder:

- `starter.py` (your completed password checker)
- `password_note.txt` (five or six sentences, see the practice task)

Your tutor marks the portfolio. The quiz is marked automatically.

### Optional

Only if you have time and are curious.

- The Level 2 exercises in each section.
- The stretch in the Build: `file_hash` and `verify_file`.

**More videos: Data with Baraa, Python Ultimate Course**

These lessons are from a different presenter. They are longer than the core videos, so treat them as extra explanation when you want more detail. Find them in the [playlist](https://www.youtube.com/playlist?list=PLNcg_FV9n7qZGfFl2ANI_zISzNp257Lwn).

- [Data with Baraa] [Python Boolean Functions](https://www.youtube.com/watch?v=v8tuWg_rvjE&list=PLNcg_FV9n7qZGfFl2ANI_zISzNp257Lwn) (8:40)
- Python Software Foundation (2026) *hashlib — Secure hashes and message digests*. Available at: https://docs.python.org/3/library/hashlib.html (Accessed: 11 November 2026).

---

## 3.1 Checking input {#section-3-1}

The code for this section is in [3.1_code/checking_input.py](files/code/3.1/checking_input.py).

### Why check input?

Programs receive data from outside: a person typing, a file, a web form. That data can be wrong. Someone types their age as `abc`. A file has an empty cell. A form field holds 5,000 characters where you expected 10.

**Validation** means checking data before you use it. A program that validates its input gives a clear message instead of crashing. It also keeps bad values out of your data, where they would spoil every later result.

Validation matters for security too. Many security problems start with a program that trusted its input. A good habit is to treat all outside data as unchecked until your code has checked it.

### Five kinds of check

| Check | Question it asks | Example |
|---|---|---|
| Presence | Is there a value at all? | A username must not be empty. |
| Type | Is it the right kind of value? | An age must be a whole number. |
| Range | Is the number between the limits? | An age must be from 0 to 120. |
| Length | Does it have the right number of characters? | A postcode has exactly 4 characters. |
| Allowed characters | Does it use only the characters we accept? | A username uses only letters, digits and `_`. |

The rest of this section shows each check in Python.

### Presence: is anything there?

`input()` always returns a string. If the person presses Enter straight away, it returns the empty string `""`. A string of only spaces is also no real answer. Use `strip()` (Week 1) to remove spaces from both ends first.

```python
name = "   "
if name.strip() == "":
    print("Please type a name.")
```

```output
Please type a name.
```

### Type: is it the right kind of value?

There are two ways to check that a string holds a whole number.

**Way 1: `isdigit()`.** This string method returns `True` when every character is a digit and there is at least one character.

```python
print("42".isdigit())
print("4 2".isdigit())
print("-5".isdigit())
print("".isdigit())
```

```output
True
False
False
False
```

Notice that `"-5"` gives `False`, because `-` is not a digit. So `isdigit()` suits values that are made only of digits, such as a postcode.

**Way 2: `try` / `except ValueError`.** You met this in Part 1. Try to convert the string with `int()`. If Python raises a `ValueError`, the string was not a whole number.

```python
def is_valid_age(text):
    """Return True if text is a whole number from 0 to 120."""
    try:
        age = int(text)
    except ValueError:
        return False
    return 0 <= age <= 120
```

This way accepts `"-5"` as a number, and it also accepts spaces around the number, because `int(" 61 ")` is `61`. The last line of the function is the next check.

### Range and length

A **range check** asks whether a number is between two limits. Python lets you write both limits in one line: `0 <= age <= 120`.

```python
for text in ["34", "abc", "-5", "150", " 61 "]:
    print(repr(text), is_valid_age(text))
```

```output
'34' True
'abc' False
'-5' False
'150' False
' 61 ' True
```

`repr(text)` shows the string with its quotation marks, so you can see the spaces.

A **length check** uses `len()`. An Australian postcode is exactly four digits, so it needs a length check and a type check together.

```python
def is_valid_postcode(text):
    """Return True if text is exactly four digits, such as "6000"."""
    return len(text) == 4 and text.isdigit()


for text in ["6000", "0800", "600", "60000", "6OOO"]:
    print(repr(text), is_valid_postcode(text))
```

```output
'6000' True
'0800' True
'600' False
'60000' False
'6OOO' False
```

The last one uses the capital letter O, not zero. It looks right to a person, but the check catches it.

Keep a postcode as a string. Do not convert it with `int()`. The postcode `"0800"` would become the number `800`, and the leading zero would be lost.

### `any` and `all`

Some checks ask a question about every character in a string. Python has two built-in functions for this. Both take a list of `True` and `False` values.

- `any(...)` returns `True` if **at least one** value is `True`.
- `all(...)` returns `True` if **every** value is `True`.

```python
print(any([False, True, False]))
print(all([True, True, False]))
```

```output
True
False
```

You can build the list with a list comprehension (Part 1, Week 4). This asks "is at least one character a digit?":

```python
print(any([ch.isdigit() for ch in "kettle7"]))
```

```output
True
```

When the comprehension is the only thing inside the brackets of `any` or `all`, you may leave out the square brackets. It works the same way and is easier to read.

```python
print(any(ch.isdigit() for ch in "kettle7"))
print(all(ch.isdigit() for ch in "60o0"))
```

```output
True
False
```

Read the first line aloud as "any character is a digit, for each character in the text". The string methods `isupper()`, `islower()`, `isdigit()` and `isalpha()` (is it a letter?) all work on a single character in this way.

To test for symbols, there is no ready-made method. Make a **set** of the symbols you mean, and use `in`.

```python
SYMBOLS = set("!@#$%&*?")


def has_symbol(text):
    """Return True if at least one character is in SYMBOLS."""
    return any(ch in SYMBOLS for ch in text)


print(has_symbol("kettle!"))
print(has_symbol("kettle"))
```

```output
True
False
```

`set("!@#$%&*?")` makes a set with one item for each character in the string.

### Allowed characters: allow-list and block-list

There are two ways to decide which characters are acceptable.

- An **allow-list** names everything you accept. Anything else is refused.
- A **block-list** names everything you refuse. Anything else is accepted.

An allow-list is safer. With a block-list you must think of every bad character in advance, and you will miss some. With an allow-list, a character you never thought about is refused automatically.

```python
ALLOWED = set("abcdefghijklmnopqrstuvwxyz0123456789_")

name = "olivia_t"
print(all(ch in ALLOWED for ch in name))

name = "olivia t;"
print(all(ch in ALLOWED for ch in name))
```

```output
True
False
```

The second name has a space and a semicolon. Neither is in the allow-list, so the name is refused. Nobody had to list the space or the semicolon as "bad".

### Returning a list of problems

A function that returns only `True` or `False` cannot tell the user what to fix. A function that stops at the first problem makes the user fix one thing, try again, and then meet the next problem.

A friendlier pattern is to **collect every problem in a list** and return the list. An empty list means the value is fine.

```python
def check_username(name):
    """Return a list of problems with a username. Empty means it is fine."""
    problems = []
    if name.strip() == "":
        problems.append("The username is empty.")
        return problems
    if len(name) < 3:
        problems.append("The username is shorter than 3 characters.")
    if len(name) > 15:
        problems.append("The username is longer than 15 characters.")
    if not all(ch in ALLOWED for ch in name):
        problems.append("Use only lower-case letters, digits and underscores.")
    if name[0].isdigit():
        problems.append("The username must not start with a digit.")
    return problems


for name in ["olivia_t", "", "jw", "9 Lives!", "user01"]:
    print(repr(name), check_username(name))
```

```output
'olivia_t' []
'' ['The username is empty.']
'jw' ['The username is shorter than 3 characters.']
'9 Lives!' ['Use only lower-case letters, digits and underscores.', 'The username must not start with a digit.']
'user01' []
```

Three things to notice:

1. Each check is a separate `if`, not `elif`. With `elif`, Python would stop at the first problem.
2. The empty name returns early. The other checks make no sense on an empty name, and `name[0]` would raise an `IndexError`.
3. The function is **pure**: it takes a value and returns a value. It does not call `input()` or `print()`. That makes it easy to test, and you will use the same pattern in this week's Build.

### Common mistakes

- **Using `elif` when you want every problem.** Use a separate `if` for each check.
- **Trusting `all` on an empty string.** `all(ch.isdigit() for ch in "")` is `True`, because there is no character that fails. Check presence or length first.
- **Using `isdigit()` for numbers that may be negative or have a decimal point.** `"-5".isdigit()` and `"3.5".isdigit()` are both `False`. Use `try` / `except ValueError` with `int()` or `float()`.
- **Converting codes to numbers.** Postcodes and phone numbers are text. `int("0800")` loses the zero.
- **Writing a block-list.** Refusing a few known bad characters lets through everything you forgot. List what you accept.
- **Checking after using.** Validate first, then use the value.

::::::::::::::::::::::::::::::::::::: challenge

### Exercises: Level 1

1. Write `is_present(text)`. It returns `True` if the text has at least one character that is not a space. Test it with `""`, `"   "` and `"Jack"`.
2. Write `is_valid_year(text)`. It returns `True` if the text is a whole number from 1900 to 2026. Use `try` / `except ValueError`. Test it with `"1987"`, `"87"`, `"abc"` and `"2050"`.
3. Write `is_valid_state(text)`. It returns `True` if the text, in upper case, is in the set `{"WA", "NT", "SA", "QLD", "NSW", "VIC", "TAS", "ACT"}`. Is this an allow-list or a block-list? Write your answer in a comment.
4. Without running it, predict what each line prints. Then run it to check.
   ```python
   print(any(ch.isupper() for ch in "kettle7"))
   print(all(ch.islower() for ch in "kettle7"))
   print(all(ch.isalpha() for ch in "kettle"))
   ```
5. Write `check_pin(text)`. It returns a list of problems. A PIN must be exactly 4 characters, must be all digits, and must not be `"0000"` or `"1234"`. Test it with `"4821"`, `"12a"` and `"1234"`.

::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::: challenge

### Exercises: Level 2

6. Add a check to `check_username` that the name does not end with an underscore. Test it.
7. Write `check_phone(text)` for an Australian mobile number written as ten digits that start with `04`. First remove any spaces with `replace(" ", "")`. Return a list of problems. Use made-up numbers only.

::::::::::::::::::::::::::::::::::::::::::::::::

## 3.2 Hashing with hashlib {#section-3-2}

The code for this section is in [3.2_code/hashing.py](files/code/3.2/hashing.py).

### Why hashing matters

You download a large file. How do you know it arrived complete, and that nobody changed it on the way? You keep a report for a year. How can you show it is the same report today?

Comparing two large files byte by byte is slow, and you may not have the original. Instead, you compare two short fingerprints. This is called checking **integrity**: checking that data has not changed.

### What a hash is

A **hash function** takes any data and calculates a short, fixed-length value from it. That value is called a **hash** or a **digest**. Think of it as a fingerprint of the data.

This course uses a hash function called **SHA-256**. It is a widely used standard. Its digest is always 256 bits long. Written in **hexadecimal** (digits `0` to `9` and letters `a` to `f`), that is always 64 characters.

Python's built-in module `hashlib` provides SHA-256. Nothing needs to be installed.

### Hashing text

```python
import hashlib

text = "hello"
digest = hashlib.sha256(text.encode("utf-8")).hexdigest()
print(digest)
print(len(digest))
```

```output
2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824
64
```

Read the long line from the inside out:

1. `text.encode("utf-8")` turns the string into bytes. A hash function works on bytes, not on characters. In Week 1 you saw that `encode` turns text into the numbers that are really stored. If you forget it, Python raises a `TypeError`.
2. `hashlib.sha256(...)` calculates the hash of those bytes.
3. `.hexdigest()` gives the result as a string of 64 hexadecimal characters.

You will hash text often, so wrap the line in a function:

```python
def text_hash(text):
    """Return the SHA-256 hash of a string, as 64 hexadecimal characters."""
    return hashlib.sha256(text.encode("utf-8")).hexdigest()
```

### Three properties to remember

**1. The same input always gives the same hash.** It does not matter which computer, which day, or which program.

```python
print(text_hash("hello") == text_hash("hello"))
```

```output
True
```

**2. A tiny change gives a very different hash.** These two messages differ in one character.

```python
print(text_hash("Pay Jack $100"))
print(text_hash("Pay Jack $900"))
```

```output
b9d6c4b2010b10a0d377302124d9fa036c33280d4ce74e1d67ee1fb29e5c108e
c55c9148b69a949a626999d3cbbcedc46fce25a55c0f0a125b2e8d9ec6a1f2ef
```

The two digests have nothing visible in common. So a hash shows **that** data changed. It does not show what changed or how much.

**3. It is one-way.** You cannot work back from the hash to the data. There is no "unhash" function. The digest is 64 characters whether the input is one letter or a whole book, so the data is simply not in there.

```python
print(len(text_hash("a")))
print(len(text_hash("a" * 100000)))
```

```output
64
64
```

Hashing is also **exact**. `"Hello"` and `"hello"` have different hashes. So do `"hello"` and `"hello "` with a space at the end.

### Hashing a file

Until now you have opened files in text mode, where Python decodes the bytes into characters for you. For a hash you want the exact bytes on the disk. Open the file in **binary mode** by adding `"b"` to the mode: `"rb"` means "read, binary". In binary mode `read()` returns a `bytes` value, not a string, and you do not give an `encoding`.

```python
def file_hash(path):
    """Return the SHA-256 hash of a file, read in binary mode."""
    with open(path, "rb") as file:
        data = file.read()
    return hashlib.sha256(data).hexdigest()
```

There is no `encode` this time, because `data` is already bytes.

To try it, the next lines save a small file that holds the five bytes of `hello`, then hash it. `"wb"` means "write, binary".

```python
from pathlib import Path

demo = Path(__file__).with_name("demo_note.txt")
with open(demo, "wb") as file:
    file.write("hello".encode("utf-8"))

print(file_hash(demo))
print(file_hash(demo) == text_hash("hello"))
```

```output
2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824
True
```

`Path(__file__).with_name("demo_note.txt")` means "a file called `demo_note.txt` in the same folder as this program". The file's hash equals the hash of the text `"hello"`, because both are the hash of the same five bytes. A hash does not care where the bytes came from.

**Why binary mode matters.** A text file's line endings can differ between Windows and other systems. In text mode Python hides that difference. The bytes are still different, so the hashes are different. Always hash files in `"rb"` mode.

**Optional detail: reading in chunks.** `file.read()` loads the whole file into memory. For a very large file, you can read a piece at a time and feed each piece to the hash with `update`. The answer is the same.

```python
def file_hash_in_chunks(path):
    """The same answer as file_hash, but reads a large file a piece at a time."""
    hasher = hashlib.sha256()
    with open(path, "rb") as file:
        chunk = file.read(4096)
        while chunk != b"":
            hasher.update(chunk)
            chunk = file.read(4096)
    return hasher.hexdigest()
```

`file.read(4096)` reads at most 4,096 bytes. `b""` is an empty bytes value, which means the end of the file. You do not need this version for the course's small files.

### Use 1: checking a downloaded file

Many software publishers print the SHA-256 hash of each file on their download page. After you download the file, you calculate its hash yourself and compare.

```python
published = "2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824"
if file_hash(demo) == published:
    print("The file matches the published hash.")
else:
    print("Warning: the file does NOT match. Do not use it.")
```

```output
The file matches the published hash.
```

If the hashes match, your copy is the same as the publisher's, byte for byte. If they differ, the download was damaged or the file was changed. Either way, do not use it.

The same idea lets you prove that a log file or a piece of evidence has not been altered: record its hash when you collect it, and calculate the hash again later.

### Use 2: storing passwords

A website must check your password when you log in. It should not keep the password itself. If its database were stolen, every password would be exposed.

Instead, a well-built system stores a **hash** of the password. At login, it hashes what you typed and compares the two hashes. Because hashing is one-way, a stolen list of hashes does not hand over the passwords directly.

Real systems go further than plain SHA-256. They add a random value called a **salt** to each password before hashing, and they use slow, purpose-built password-hashing functions. That is beyond this course. The idea to keep is: **store a hash, never the password**.

### Common mistakes

- **Forgetting `encode`.** `hashlib.sha256("hello")` raises `TypeError`. Hash bytes, not a string.
- **Forgetting `.hexdigest()`.** Without it you print a hash object, not the 64 characters.
- **Opening a file in text mode to hash it.** Use `"rb"`.
- **Extra spaces or a newline.** `"hello\n"` is not `"hello"`. If a hash does not match, check for a stray newline or space. `strip()` helps when you read an expected hash from a file.
- **Calling hashing "encryption".** Encryption can be reversed with a key. Hashing cannot be reversed at all. This week's Concepts Bridge compares them.
- **Thinking a hash hides a weak password.** Anyone can hash the word `password` and get the same digest as everyone else. That is one reason common passwords are dangerous.

::::::::::::::::::::::::::::::::::::: challenge

### Exercises: Level 1

1. Print the SHA-256 hash of your first name in lower case. Check that it has 64 characters.
2. Print the hash of `"Olivia"` and of `"olivia"`. Are they the same? Write one sentence in a comment saying why.
3. Write `same_text(a, b)`. It returns `True` if the two strings have the same SHA-256 hash. Test it with two equal strings and two that differ by one space.
4. Use `file_hash` on the course file `assets/files/sample_text.txt`. Use this path, which is ready-made: `Path(__file__).resolve().parents[4] / "assets" / "files" / "sample_text.txt"` (it works from a program in a folder such as `lessons/3.2_code/`; adjust the number if your program is somewhere else). Print the hash.
5. Copy `sample_text.txt` to your own folder. Change one letter in the copy and save it. Hash both files. What do you see? Write one sentence in a comment.

::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::: challenge

### Exercises: Level 2

6. Write `verify_text(text, expected)`. It returns `True` if the hash of `text` equals `expected`, ignoring upper and lower case in `expected` and any spaces around it.
7. Hash every line of `assets/files/common_passwords.txt` and print the first three as `password -> hash`. Remember to `strip()` each line. This shows why a common password is not protected by hashing alone: its hash is the same everywhere.

::::::::::::::::::::::::::::::::::::::::::::::::

## 3.3 The Caesar cipher {#section-3-3}

The code for this section is in [3.3_code/caesar.py](files/code/3.3/caesar.py).

### Why look at an old cipher?

People have hidden messages for thousands of years. The Caesar cipher is named after Julius Caesar, who is said to have used it. It is far too weak for real use today. It is still a good way to practise `ord`, `chr`, the `%` operator and loops over text, and it shows what a cipher is.

**This is a teaching cipher. It is NOT secure. Never use it to protect real data.** Section 3.3 ends by explaining why.

### Key terms

- **Plaintext:** the message before it is scrambled.
- **Cipher:** a method for scrambling text so that only people who know the method and the key can read it.
- **Key:** the secret value that controls the scrambling. In the Caesar cipher the key is a number.
- **Encrypt:** turn plaintext into scrambled text, called **ciphertext**.
- **Decrypt:** turn ciphertext back into plaintext.

### The idea: shift each letter

The Caesar cipher moves every letter a fixed number of places along the alphabet. The number is the key. With a key of 3:

```output
plain:   a b c d e f g h i j k l m n o p q r s t u v w x y z
cipher:  d e f g h i j k l m n o p q r s t u v w x y z a b c
```

So `a` becomes `d`, `b` becomes `e`, and `x` wraps around to `a`. The word `cat` becomes `fdw`.

### Letters as positions

In Week 1 you used `ord` to get a character's number and `chr` to turn a number back into a character. For the letters `a` to `z`, the numbers run in order, so subtracting `ord("a")` gives the letter's **position** in the alphabet, counting from 0.

```python
print(ord("a"), ord("d"), ord("z"))
print(ord("d") - ord("a"))
```

```output
97 100 122
3
```

So `a` is position 0, `d` is position 3 and `z` is position 25. Upper-case letters work the same way, starting from `ord("A")`, which is 65.

### Wrapping around with `% 26`

If you add 3 to the position of `y` (24), you get 27. There is no position 27, because the alphabet has 26 letters. We want to wrap around to the start.

The **remainder operator** `%` gives what is left after dividing. `27 % 26` is `1`, so `y` moves to position 1, which is `b`.

```python
print((24 + 3) % 26)
print(-3 % 26)
```

```output
1
23
```

The second line is useful. In Python, `%` with a positive divisor never gives a negative answer. A shift of -3 from position 0 lands on position 23, which is `x`. That is why shifting backwards works with no extra code.

### Building `shift_letter`

The function must:

1. Work out whether the character is lower case, upper case, or not a letter.
2. Leave non-letters (spaces, digits, punctuation) alone.
3. Convert the letter to a position, add the key, wrap with `% 26`, and convert back.
4. Keep the case.

```python
def shift_letter(letter, key):
    """Shift one letter `key` places along the alphabet, keeping its case.

    Anything that is not a letter from a to z or A to Z is returned unchanged.
    """
    if "a" <= letter <= "z":
        start = ord("a")
    elif "A" <= letter <= "Z":
        start = ord("A")
    else:
        return letter
    position = ord(letter) - start
    new_position = (position + key) % 26
    return chr(start + new_position)
```

`"a" <= letter <= "z"` compares characters by their numbers, so it is `True` for the 26 lower-case letters only. The `start` variable holds the number where that case begins. Test it:

```python
print(shift_letter("a", 3))
print(shift_letter("y", 3))
print(shift_letter("Y", 3))
print(shift_letter("!", 3))
print(shift_letter("d", -3))
```

```output
d
b
B
!
a
```

### Encrypting a message

Apply `shift_letter` to every character, then join the pieces back into one string with `"".join(...)`. (You used `join` in Week 1.)

```python
def encrypt(text, key):
    """Shift every letter in the text by `key` places."""
    return "".join(shift_letter(ch, key) for ch in text)


secret = encrypt("Meet at the cafe, 9 pm!", 3)
print(secret)
```

```output
Phhw dw wkh fdih, 9 sp!
```

Case, spaces, the digit and the punctuation are all kept. Only the letters moved.

### Decrypting

To undo a shift of 3, shift by -3. So decrypting is encrypting with the negative key.

```python
def decrypt(text, key):
    """Undo encrypt by shifting every letter back by `key` places."""
    return encrypt(text, -key)


print(decrypt(secret, 3))
```

```output
Meet at the cafe, 9 pm!
```

Two more things to try. A key of 13 applied twice gives back the original, because 13 + 13 = 26. A key of 26 changes nothing, because it is a full lap.

```python
print(encrypt("Hello, World!", 13))
print(encrypt("xyz", 26))
```

```output
Uryyb, Jbeyq!
xyz
```

Letters with accents, such as the é in `café`, are not in `a` to `z`. This version leaves them unchanged. `encrypt("café", 1)` gives `dbgé`, with the `é` left as it was.

### Why this cipher is not secure

There are only 25 useful keys (1 to 25). Anyone who sees a Caesar ciphertext can try all 25 and read the one that makes sense. That takes a computer a fraction of a second, and a patient person a few minutes. Keeping the method secret does not help, because the method is public knowledge.

Modern encryption uses standard, carefully tested methods with keys so large that trying them all is impossible. If you ever need to protect real data, use those tools. Do not invent your own cipher, and never use this one.

This week's Concepts Bridge compares encryption with hashing and encoding.

### Common mistakes

- **Forgetting the wrap.** Without `% 26`, shifting `z` gives a character such as `{`.
- **Forgetting to subtract the start.** Using `ord(letter) + key` directly mixes up positions and character numbers.
- **Treating upper and lower case the same.** If you use `ord("a")` for a capital letter, you get the wrong answer. Choose `start` for each case.
- **Shifting spaces and punctuation.** Return non-letters unchanged.
- **Believing a cipher means security.** A weak cipher gives a false sense of safety, which is worse than none.

::::::::::::::::::::::::::::::::::::: challenge

### Exercises: Level 1

1. Without running it, work out `shift_letter("m", 5)`, `shift_letter("x", 5)` and `shift_letter("B", 2)`. Then run them.
2. Encrypt `"Perth is warm"` with a key of 4. Then decrypt the result and check you get the original.
3. Write `is_letter(ch)`. It returns `True` for a to z and A to Z. Use it to count the letters in `"Meet at 9 pm!"`.
4. Encrypt the sentence `"Keep this a secret"` with key 7 and print it. Ask yourself: would you trust this to hide a real password? Write a one-sentence answer in a comment.
5. Check that `decrypt(encrypt(text, key), key) == text` for three different texts and keys, including one with capital letters and digits.

::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::: challenge

### Exercises: Level 2

6. Write `rotate_word(word, key)` that shifts only the lower-case letters and leaves capitals alone. Test it.
7. Change `encrypt` so it also accepts keys larger than 26 or smaller than -26. Does your program already handle them? Explain why in a comment.

::::::::::::::::::::::::::::::::::::::::::::::::

## Concepts Bridge: Hashing, Encryption and Encoding {#week-3-bridge}

**Time: 30 minutes.** Reading 12 minutes, activities 13 minutes, checking the model answers 5 minutes.

### Why this matters

People often mix up three ideas: **encoding**, **encryption** and **hashing**. All three change data into a different form, so they look alike. They have different jobs. If you pick the wrong one, you can give a false sense of safety. Choosing the right tool for a job is part of LO 4.

### The three ideas

- **Encoding** changes data into another format so that it can be stored or sent. Everyone knows the rules, so anyone can reverse it. UTF-8 (Week 1) is an encoding. So is Base64, which writes bytes using only letters, digits and a few symbols so that they can travel in text.
- **Encryption** scrambles data so that only someone with the right **key** can read it. It is for secrecy. The Caesar cipher (Section 3.3) is a very weak form of encryption.
- **Hashing** calculates a short, fixed-length fingerprint of data. It is one-way. It is for integrity and for checking that two things match. SHA-256 (Section 3.2) is a hash.

| | Encoding | Encryption | Hashing |
|---|---|---|---|
| **Purpose** | Represent data in a usable format | Keep data secret | Fingerprint data to check it has not changed, or to check a match |
| **Can it be reversed?** | Yes, by anyone, because the rules are public | Yes, but only by someone with the right key | No. It is one-way, for everyone |
| **Needs a key?** | No | Yes | No |
| **Output length** | Grows with the input | About the same as the input | Always the same (64 hex characters for SHA-256) |
| **Example in this course** | UTF-8 `encode` and `decode`; Base64-style encoding | Caesar cipher (weak, for teaching only) | `hashlib.sha256` |
| **Safe for secrecy?** | No | Yes, if the method is strong and the key stays secret | No. It hides nothing about guessable inputs |

### The common mix-up: encoding is not security

Base64 and similar encodings look scrambled. For example, the text `hello` in Base64 is `aGVsbG8=`. It is not secret. Anyone can decode it in one line, with no key. If you see a "password" that is only encoded, treat it as if it were written in plain text.

A second mix-up: "hashing a password encrypts it". It does not. Nothing can be decrypted, because there is no key and no way back. That is exactly why a website can check a password without being able to read it.

### Choosing the tool

Ask three questions about the job:

1. Do I need to get the data back later? If no, hashing may fit. If yes, you need encoding or encryption.
2. Must the data stay secret from other people? If yes, you need encryption (a strong, standard method, not the Caesar cipher).
3. Do I only need to know whether the data changed, or whether two values match? That is hashing.

::::::::::::::::::::::::::::::::::::: challenge

### Activity 1: choose the tool (8 minutes)

For each scenario, write **encoding**, **encryption** or **hashing**, with a reason in one sentence.

1. A program saves the text `Zoë` so that it uses the right bytes in a file.
2. You want to check that a file you downloaded is the same as the one the publisher posted.
3. A staff member sends a private message that only the person who receives it should be able to read.
4. A login system must check a password without keeping the password.
5. A file stores each byte as letters and digits so that it can be pasted into an email.

### Activity 2: why can't a site email you your old password? (5 minutes)

You press "I forgot my password" on a website. It sends a link to choose a new one. Another site emails you your **old** password. In two or three sentences, explain what the second site's behaviour tells you about how it stores passwords, and why that is a problem.

:::::::::::::::: solution

### Model answers

**Activity 1**

1. **Encoding.** The program is only choosing how to represent the characters as bytes (UTF-8). Nothing is hidden.
2. **Hashing.** You compare the SHA-256 hash of your copy with the hash the publisher posted. If one byte differs, the hashes differ.
3. **Encryption.** The message must stay secret, and only the holder of the key should be able to read it.
4. **Hashing.** The system keeps a hash of the password. At login it hashes what you typed and compares the two hashes.
5. **Encoding.** Writing bytes as text, such as Base64, is representation. It is not secret, and anyone can undo it.

**Activity 2.** If a site can email your old password, it has the password itself, or it stores it in a way it can reverse. A hash cannot be reversed, so a site that stores only a hash cannot tell you the old password. The second site is storing passwords unsafely. If someone stole its database, they would get every password. It is also a risk because email is not private: the password then sits in an inbox. A well-built site stores a hash and lets you set a new password instead.

:::::::::::::::::::::::::
::::::::::::::::::::::::::::::::::::::::::::::::

### Further reading

- Python Software Foundation (2026) *hashlib — Secure hashes and message digests*. Available at: https://docs.python.org/3/library/hashlib.html (Accessed: 11 November 2026).
- Python Software Foundation (2026) *base64 — Base16, Base32, Base64, Base85 Data Encodings*. Available at: https://docs.python.org/3/library/base64.html (Accessed: 11 November 2026).

## Practice task: Password Strength Checker {#week-3-practice}

:::::::::::::::::::::::::::::::::::::::: callout

### Files for this task

The easiest way to get every file is the [course zip file](data/course-data.zip) from the Setup page. Unzip it and open the folder in PyCharm. The programs find the data files by their place in that folder, so keep the folder layout. You can also download single files here:

- [starter.py](files/week-3/starter.py)
- [solution.py](files/week-3/solution.py)
- [test_solution.py](files/week-3/test_solution.py)

:::::::::::::::::::::::::::::::::::::::::::::::::::

**Time: 2 hours.** This is your portfolio item for Week 3. Your tutor marks it at the end of the week.

### Goal

Build a program that rates a password as `"weak"`, `"fair"` or `"strong"` and tells the user what is wrong with it, in plain English. You write small functions that take values and return values (pure functions), so they are easy to test. `input()` and `print()` stay in `main()`.

There is also an **optional stretch**: an integrity checker that hashes a file.

### Privacy and safety notes (read first)

- **Test only with made-up passwords.** Never type a real password into a practice program.
- The program must **never save a password, and never print one to a file.** It only reads a password, rates it and forgets it.
- A checker like this can only apply rules. It cannot know whether a password is safe. See your note below.
- **Length matters most.** A **passphrase** (several unrelated words, such as `purple teapot morning walk`) is long and easy to remember, so it is a good pattern.

### Files

| File | What it is |
|---|---|
| `starter.py` | The function names and docstrings, with `TODO` bodies for you to fill in. |
| `test_solution.py` | Tests for the functions. |
| `solution.py` | A model answer. Try the task yourself before you look. |

The list of common passwords is `assets/files/common_passwords.txt` (50 common passwords, one per line, in lower case). `starter.py` already finds it for you with `COMMON_FILE`.

### The fixed wording

The tests check these exact messages. `starter.py` already has them as constants (`TOO_SHORT` and so on), so use the names.

| Constant | Message |
|---|---|
| `TOO_SHORT` | It is shorter than 12 characters. |
| `NO_UPPER` | It has no upper-case letter. |
| `NO_LOWER` | It has no lower-case letter. |
| `NO_DIGIT` | It has no digit. |
| `NO_SYMBOL` | It has no symbol. |
| `IS_COMMON` | It is on the list of common passwords. |

`find_problems` returns the messages in the order above. An empty list means no problems.

### The rating rule

`strength(password, common)` checks these in order:

1. **weak** if the password is a common password (ignoring case), or is shorter than 8 characters.
2. **strong** if `find_problems` returns an empty list (no problems at all).
3. **fair** for everything else.

A **symbol** is any character that is not a letter, a digit or a space.

### Steps (120 minutes)

Run the tests after each step to see more of them pass. In PyCharm, right-click `test_solution.py` and choose **Run pytest**. To test your own file, open `test_solution.py` and change `import solution as checker` to `import starter as checker`. Change it back if you want to compare with the model answer.

| Step | What you do | Time |
|---|---|---|
| 1 | Read `starter.py` from top to bottom. Run it. It should print nothing and not crash. Read the fixed wording and the rating rule above. | 10 min |
| 2 | Write `load_common_passwords(path)`. Open the file with `with open(path, encoding="utf-8") as file:`. For each line, `strip()` and `lower()` it, skip empty lines, and add it to a set. Return the set. | 10 min |
| 3 | Write `check_length`, `has_upper`, `has_lower`, `has_digit` and `has_symbol`. Use `any(...)` for the four `has_` functions. | 15 min |
| 4 | Write `is_common(password, common)`. Make the password lower case and test it with `in`. | 5 min |
| 5 | Write `find_problems(password, common)`. Start with an empty list, use a separate `if` for each check (not `elif`), and append the matching message. Return the list. | 15 min |
| 6 | Write `strength(password, common)` using the three rules, in order. | 10 min |
| 7 | Write `main()`. Load the list, remind the user to use made-up passwords, then ask for passwords until an empty line. For each one, print the rating and each problem on its own line. | 15 min |
| 8 | Run all the tests. Fix anything that fails. Read each failure message carefully, because it shows what the test expected. | 15 min |
| 9 | Try your program by hand with five made-up passwords, such as `qwerty`, `Tuesday1`, `purple teapot morning walk` and `Blue-Kettle-47-Rain`. Check the ratings make sense. | 5 min |
| 10 | Write `password_note.txt` (see below). | 15 min |
| 11 | Tidy up: remove unused code and debug `print` lines, check your docstrings, and make sure no password is saved anywhere. | 5 min |
| | **Total** | **120 min** |

#### Stretch (optional): an integrity checker

**If you have time left inside the 2 hours, or as an optional extra.** About 20 minutes. You do not need it to meet the checklist.

1. Write `file_hash(path)`. Open the file in `"rb"` mode, read it, and return the SHA-256 hex digest.
2. Write `verify_file(path, expected_hash)`. Return `True` if the file's hash equals `expected_hash`, ignoring upper and lower case and spaces around `expected_hash`.

The last three tests in `test_solution.py` are for the stretch. **They fail until you write these two functions, and that is fine.**

### Example run

```output
Password strength checker.
Use made-up passwords only. Never type a real password here.
Press Enter on an empty line to finish.
Password to check: sunshine
  Rating: weak
  - It is shorter than 12 characters.
  - It has no upper-case letter.
  - It has no digit.
  - It has no symbol.
  - It is on the list of common passwords.
Password to check: purple teapot morning walk
  Rating: fair
  - It has no upper-case letter.
  - It has no digit.
  - It has no symbol.
Password to check: Blue-Kettle-47-Rain
  Rating: strong
  No problems found.
Password to check:
Goodbye.
```

Your wording for the lines in `main()` can differ. The problem messages must match the table above.

### Hints

- A string method such as `isupper()` works on one character. To ask about a whole password, use `any(ch.isupper() for ch in password)`.
- `line.strip()` removes the newline and spaces at the ends. `.lower()` makes it lower case.
- A set is made with `set()` and filled with `.add(item)`.
- `problems.append(TOO_SHORT)` adds one message to a list.
- Compare lists with `==`. An empty list is `[]`.
- `purple teapot morning walk` is only "fair" because this checker asks for a capital, a digit and a symbol. That shows a limit of rule-based checkers. Say so in your note.

### Your note: `password_note.txt`

Write five or six sentences, in your own words, in a plain text file called `password_note.txt`. Cover these points:

1. What does your checker test, and what can it **not** know?
2. Why does a list of common passwords matter?
3. Why does length help?
4. Why should a website store a hash of a password, and not the password?
5. What is one limit of rule-based checkers?

### Check your work

- [ ] The tests pass (apart from the optional stretch tests, if you have not done the stretch).
- [ ] `find_problems` returns an empty list for a password with no problems, and lists every problem for a bad one (not only the first).
- [ ] `strength` follows the three rules in order.
- [ ] The four `has_` functions use `any`.
- [ ] `is_common` ignores upper and lower case.
- [ ] Only `main()` uses `input()` and `print()`.
- [ ] The program does not save or write any password.
- [ ] You tested only with made-up passwords.
- [ ] `password_note.txt` has five or six sentences, in your own words.

:::::::::::::::::::::::::::::::::::::: keypoints

- Each week has four blocks: Watch, Read & practise, Concepts Bridge and Build.
- Validation means checking data before you use it.
- An allow-list (what is allowed) is safer than a block-list (what is banned).
- Report every problem at once so the user can fix them together.
- A hash is a fixed-length fingerprint of data.
- The same input always gives the same hash; a tiny change gives a very different one.
- You cannot work back from a hash to the data.
- The Caesar cipher shifts every letter by a fixed number.
- It is a teaching cipher. It is not secure and must never protect real data.
- Encoding represents data. It is not security.
- Encryption hides data and can be reversed with the key.
- Hashing gives a fingerprint and cannot be reversed.
- Never type or save a real password in a practice program.

::::::::::::::::::::::::::::::::::::::::::::::::
