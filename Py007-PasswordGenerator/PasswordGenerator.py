# Python Password Generator

# Import the random module to generate random characters
import random

# Create an empty list to store the characters of the password
passwordList = []

# Define the characters that can be used in the password
smallCharacters = "abcdefghijklmnopqrstuvwxyz"
capitalCharacters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numCharacters = "0123456789"
specialCharacters = "!@#$%^&*()_+~`|}{[]\\:;?><,./-="

# Welcome the user to the password generator
print("Welcome to the Password Generator!")

# Ask the user how many characters of each type they want
smallChar = int(input("How many small characters would you like in your password? "))
capitalChar = int(input("How many capital characters would you like in your password? "))
numChar = int(input("How many numbers would you like in your password? "))
specialChar = int(input("How many special characters would you like in your password? "))

# Randomly select the requested number of lowercase characters
randomSmallChar = random.choices(smallCharacters, k=smallChar)

# Add the selected lowercase characters to the password list
passwordList.extend(randomSmallChar)

# Randomly select the requested number of uppercase characters
randomCapitalChar = random.choices(capitalCharacters, k=capitalChar)

# Add the selected uppercase characters to the password list
passwordList.extend(randomCapitalChar)

# Randomly select the requested number of numbers
randomNumChar = random.choices(numCharacters, k=numChar)

# Add the selected numbers to the password list
passwordList.extend(randomNumChar)

# Randomly select the requested number of special characters
randomSpecialChar = random.choices(specialCharacters, k=specialChar)

# Add the selected special characters to the password list
passwordList.extend(randomSpecialChar)

# Shuffle all the characters to make their order random
random.shuffle(passwordList)

# Create an empty string to build the final password
password = ""

# Add each character from the list to the password string
for char in passwordList:
    password += "".join(char)

# Display the generated password
print(f"\nYour new password is: \n{password}")

