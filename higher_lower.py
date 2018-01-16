import random

print("Higher/Lower to gra, w której użytkownik zgaduje wylosowaną liczbę,\n"
      "a komputer podpowiada mu, czy liczba jest większa czy mniejsza od podanej "
      "\nprzez użytkownika.\n")

runda = int(input("Określ liczbę rund: "))
start_zakres = int(input("Wprowadź liczbę stanowiącą początek przedziału liczbowego: "))
end_zakres = int(input("Wprowadź liczbę stanowiącą koniec przedziału liczbowego: "))

liczba = random.randrange(start_zakres, end_zakres)


for i in range(runda):
    wybor = int(input("Odgadnij liczbę: "))
    print("Liczba, którą wybrałeś to: ", wybor)

    if wybor < liczba:
        print("Podana liczba jest ZA MAŁA! \nSpróbuj jeszcze raz ;)")

    elif wybor > liczba:
        print("Podana liczba jest ZA DUŻA! \n Spróbuj jeszcze raz ;)")

    elif wybor == liczba:
        print("Brawo, zgadłeś/aś! Odgadnięta liczba to: ", liczba)

print("\n\nNiestety nie udało Ci się odgadnąć wylosowanej liczby :( \n"
      "Zagraj jeszcze raz!")

