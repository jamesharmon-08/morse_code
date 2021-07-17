import pygame
import numpy as np

pygame.mixer.init()

morse = {
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    " ": "       ",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    "0": "-----",
}


class play_sound():

    def __init__(self):

        self.dot = np.sin(2 * np.pi * np.arange(5000) * 440 / 5000).astype(np.float32)
        self.dash = np.sin(2 * np.pi * np.arange(15000) * 440 / 15000).astype(np.float32)
        self.blank = np.sin(2 * np.pi * np.arange(0) * 440 / 0).astype(np.float32)

    def play(self, symbol):
        if symbol == 'dot':
            sound = pygame.mixer.Sound(self.dot)
        elif symbol == 'dash':
            sound = pygame.mixer.Sound(self.dash)
        else:
            sound = pygame.mixer.Sound(self.blank)
        sound.play(0)
        pygame.time.wait(int(sound.get_length() * 2500))
