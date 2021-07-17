from morse import morse

# get the text to be converted
text = input("What do you wish to convert").upper()

# loop through the letter and print the morse code
for letter in text:
    print(morse[letter], end=" ")

