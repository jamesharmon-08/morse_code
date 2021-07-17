from morse import morse, play_sound

# get the text to be converted
text = input("What do you wish to convert").upper()

# snd = play_sound()
# loop through the letter and print the morse code
for letter in text:
    print(morse[letter], end=" ")
    # for symbol in morse[letter]:
    #     if symbol == '.':
    #         snd.play('dot')
    #     elif symbol == '-':
    #         snd.play('dash')
    #     else:
    #         snd.play('blank')

