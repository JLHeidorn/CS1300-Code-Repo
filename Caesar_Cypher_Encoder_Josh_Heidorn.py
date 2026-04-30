def caesar_encode(text, shift):
    result = ""

    for ch in text:
        if ch.isalpha():
            if ch.islower():
                result += chr((ord(ch) - 97 + shift) % 26 + 97)
            else:
                result += chr((ord(ch) - 65 + shift) % 26 + 65)
        else:
            result += ch

    return result


# Tests
print(caesar_encode("Hello, World!", 3))  # Khoor, Zruog!
print(caesar_encode("abc xyz", 2))        # cde zab
print(caesar_encode("Python 3", 5))       # Udymts 3
