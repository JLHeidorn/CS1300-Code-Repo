print("=== TEXT ANALYZER ===")

sentence = input("Enter a sentence: ")

print("--- Analysis Results ---")

# Character counts
print("Total characters (with spaces):", len(sentence))
print("Total characters (without spaces):", len(sentence.replace(" ", "")))

# Word count
words = sentence.split()
print("Number of words:", len(words))

# Vowel count
vowels = "aeiou"
vowel_count = 0

for char in sentence.lower():
    if char in vowels:
        vowel_count += 1

print("Number of vowels:", vowel_count)

# Case changes
print("Uppercase version:", sentence.upper())
print("Lowercase version:", sentence.lower())

# Reverse
print("Reversed:", sentence[::-1])

# Starts with capital
if len(sentence) > 0 and sentence[0].isupper():
    print("Starts with capital: Yes")
else:
    print("Starts with capital: No")

# Ends with punctuation
if len(sentence) > 0 and sentence[-1] in ".!?":
    print("Ends with punctuation: Yes")
else:
    print("Ends with punctuation: No")