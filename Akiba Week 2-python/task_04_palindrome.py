word = input("Enter a Word: ").lower()
if word == word[:: -1]:
    print("Palindrome")
else:
    print("Not Palindrome")