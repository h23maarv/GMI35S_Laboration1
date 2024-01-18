import random
from random import randint

def delbara_heltal():
    answer = []
    while(True):
        try:
            number1 = int(input("Vilket är ditt första tal?\n"))
            number2 = int(input("Vilket är ditt andra tal?\n"))

            for i in range(1, 1601):
                if i % number1 == 0 and i % number2 == 0:
                    answer.append(i)
            print(answer)
            break
        except:
            print("Ej giltig input, testa ett heltal.\n")

def gissnings_lek():
    guess = []
    guesses_made = 0
    number = random.randint(1, 60)
    while(True):
        try:
            print("Jag tänker på en siffra mellan 1 och 60.\n")

            while guess != number:
                guess = int(input("Ta en gissning: \n"))
                guesses_made += 1
                if guess < number:
                    print("Din gissning är för låg.\n")
                elif guess > number:
                    print("Din gissning är för hög.\n")
                else:
                    break
            if guess == number:
                print(f"Bra jobbat! Du gissade numret på {guesses_made} försök!\n")
                break
        except:
            print("Ej giltig input, testa ett heltal.\n")