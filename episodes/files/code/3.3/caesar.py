"""Section 3.3: the Caesar cipher.

A teaching cipher only. It is NOT secure and must never protect real data.
"""


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


def encrypt(text, key):
    """Shift every letter in the text by `key` places."""
    return "".join(shift_letter(ch, key) for ch in text)


def decrypt(text, key):
    """Undo encrypt by shifting every letter back by `key` places."""
    return encrypt(text, -key)


print("--- positions ---")
print(ord("d") - ord("a"))
print((24 + 3) % 26)
print(-3 % 26)

print("--- one letter ---")
print(shift_letter("a", 3))
print(shift_letter("y", 3))
print(shift_letter("Y", 3))
print(shift_letter("!", 3))
print(shift_letter("d", -3))

print("--- a message ---")
secret = encrypt("Meet at the cafe, 9 pm!", 3)
print(secret)
print(decrypt(secret, 3))

print("--- other keys ---")
print(encrypt("Hello, World!", 13))
print(encrypt("xyz", 26))
print(encrypt("café", 1))
