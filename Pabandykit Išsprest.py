# Šitas darbas yra tik taip pramogai
from dotenv import load_dotenv
import os

load_dotenv()
import random

word_to_guess = os.getenv('WORD_TO_GUESS')

if word_to_guess is None:
    print("Klaida: WORD_TO_GUESS kintamasis nebuvo rastas .env faile.")
    exit()
letters = list(word_to_guess.replace(" ", ""))
guessed_letters = ['_'] * len(letters)
attempts = 6

def print_word(guessed_letters):
    """ Atspausdina paslepta zodi su atidengtomis raidemis ir tusciais simboliais. """
    print("Zodis:", end="")
    for letter in guessed_letters:
        print(letter, end=" ")
    print()

def check_win(guessed_letters, letters):
    """ Patikrina, ar zaidejas laimejo (ar visi simboliai atspeti.) """
    return guessed_letters == letters
def play_game():
    global attempts
    print("Kartuves zaidimas: Spek zodi!")
    print("Zaidimo tikslas: Atspeti zodi!")
    print("Turi", attempts, "bandymus.")

    guessed_letters = ['_'] * len(letters)
    guessed = []

    while attempts > 0:
        print_word(guessed_letters)
        guess = input("Iveskite raide: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Prasome ivesti tik viena raide.")
            continue

        if guess in guessed:
            print("jus jau spejote sia raide.")
            continue

        guessed.append(guess)

        if guess in letters:
            for i in range(len(letters)):
                if letters[i] == guess:
                    guessed_letters[i] = guess
            print("Teisingai!")
        else:
            attempts -= 1
            print(f"Neteisingai! Bandymu liko: {attempts}")

        if check_win(guessed_letters, letters):
            print_word(guessed_letters)
            print("Sveikiname, jus laimejote!")

    if attempts == 0:
        print("Jus pralaimejote! Zodis buvo pasleptas, taciau teisingas zodis buvo:", word_to_guess)

if __name__ == "__main__":
    play_game()
