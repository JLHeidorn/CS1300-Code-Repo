print("=== PALINDROME CHECKER ===")

text = input("Enter a word or phrase: ")

# Normalize the string
cleaned = text.lower().replace(" ", "")

# Check palindrome
if cleaned == cleaned[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")