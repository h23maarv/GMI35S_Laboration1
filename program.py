import modules
menu = int
while menu != 3:
    try:
        menu = int(input
            ("\n--------------------------------------------------------------------------------------"
            "\n1. Hitta och skriva ut alla tal mellan 1 och 1600 som är delbara med två valda heltal."
            "\n2. Gissa på ett tal mellan 1 och 60. Användaren ska få gissa fram tills de gissat rätt."
            "\n3. Avsluta programmet."
            "\n--------------------------------------------------------------------------------------\n"))
        match menu:
            case 1:
                while True:
                    try:
                        number1 = int(input("Vilket är ditt första tal?\n"))
                        break
                    except ValueError:
                        print("Ej giltig input, testa ett heltal.\n")
                while True:
                    try:
                        number2 = int(input("Vilket är ditt andra tal?\n"))
                        break
                    except ValueError:
                        print("Ej giltig input, testa ett heltal.\n")
                modules.delbara_heltal(number1, number2)
            case 2:
                modules.gissnings_lek()
            case 3:
                pass
            case default:
                print("Du får inte vara med och leka.\n")
    except ValueError:
        print("Ej giltig input, testa ett heltal.\n")
