import random
from random import randint


def delbara_heltal(number1, number2):
    answer = []
    for i in range(1, 1601):
        if i % number1 == 0 and i % number2 == 0:
            answer.append(i)
    print(answer)
    input("Tryck på valfri tangent för att fortsätta programmet")


def gissnings_lek():
        random_number = (randint(1, 60))
        print("\nDu valde att leka gissningsleken. Jag har nu valt ut ett heltal mellan 1 och 60.\n")
        while True:
            try:
                user_guess = int(input("Skriv in din gissning här: "))
                break
            except ValueError:
                print("Felaktig inmatning. Mata in ett heltal.")
        while user_guess != random_number:
            if user_guess < random_number:
                print(str(user_guess) + " är för lågt.")
            elif int(user_guess) > random_number:
                print(str(user_guess) + " är för högt.")
            while True:
                try:
                    user_guess = int(input("Gissa igen: "))
                    break
                except ValueError:
                    print("Felaktig inmatning. Mata in ett heltal.")
        print("Rätt svar! Talet var " + str(random_number))
        input("Tryck på valfri tangent för att fortsätta programmet")