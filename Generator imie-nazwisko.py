import random

damskie = ["Joanna", "Anna", "Julia", "Kamila", "Monika", "Iwona", "Paulina", "Małgorzata"]
meskie = ["Adam", "Bartosz", "Daniel", "Dariusz", "Marcin", "Marek", "Piotr", "Kamil"]

nazwiskoD = ["Kowalska", "Nowak", "Jasińska", "Kłos", "Dąbrowska"]
nazwiskoM = ["Kowalski", "Nowak", "Jasiński", "Kłos", "Dąbrowski"]


while True:
    czynnosc = input("\nAby wygenerować losowe imię i nazwisko wybierz: "
                     "\nD - dla damskiego lub M - dla męskiego."
                     "\nCokolwiek innego spowoduje powtórzenie pytania.\n\n")
    czynnosc = czynnosc.lower()

    if czynnosc == "d":
        iD = random.choice(damskie)
        nD = random.choice(nazwiskoD)
        print("\nWylosowane imię i nazwisko damskie to:", iD, nD)

    elif czynnosc == "m":
        iM = random.choice(meskie)
        nM = random.choice(nazwiskoM)
        print("\nWylosowane imię i nazwisko męskie to:", iM, nM)

    else:
        print("\n\nNiestety wybór jest nieprawidłowy")
       
