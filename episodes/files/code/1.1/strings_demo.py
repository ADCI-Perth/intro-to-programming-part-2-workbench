"""Section 1.1: strings, indexing and slicing."""

word = "Python"
print(len(word))
print(word[0], word[5], word[-1], word[-2])
print(word[0:2], word[2:6])
print(word[:2], word[2:], word[-3:], word[:])
print(word[2:100])
print(word[::-1])

line = "2026-11-09 07:13:45 LOGIN user01"
print(len(line))
print(line[:10])
print(line[11:19])
print(line[-6:])
print(line[11:13])

digits = "0123456789"
print(digits[::2], digits[1::2], digits[2:9:3])

new_word = "J" + word[1:]
print(new_word, word)

digit_count = 0
for character in line:
    if character in "0123456789":
        digit_count = digit_count + 1
print(digit_count)

print("LOGIN" in line, "LOGOUT" in line, "login" in line, "x" not in line)

try:
    word[0] = "J"
except TypeError as error:
    print("TypeError:", error)
