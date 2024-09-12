userInput = list(input("Palindrome? "))

if (userInput == userInput[::-1]):
    print(f"{str(userInput)} is a palindrome!")

else:
    print(f"{str(userInput)} is NOT a palindrome.")