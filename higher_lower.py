import random

print("Higher/Lower to gra, w której użytkownik zgaduje wylosowaną liczbę,\n"
      "a komputer podpowiada mu, czy liczba jest większa czy mniejsza od podanej "
      "\nprzez użytkownika.\n")

runda = int(input("Określ liczbę rund: "))
start_zakres = int(input("Wprowadź liczbę stanowiącą początek przedziału liczbowego: "))
end_zakres = int(input("Wprowadź liczbę stanowiącą koniec przedziału liczbowego: "))

while end_zakres < start_zakres:
    print("Liczba z końca przedziału musi być większa od liczby z początku przedziału!")
    end_zakres = int(input("Wprowadź liczbę stanowiącą koniec przedziału liczbowego: "))

liczba = random.randrange(start_zakres, end_zakres)


for i in range(runda):
    wybor = int(input("Odgadnij liczbę: "))
    print("Liczba, którą wybrałeś to: ", wybor)

    odpowiedz = ""
    jeszcze_raz = "Spróbuj jeszcze raz ;)"

    if wybor < liczba:
        odpowiedz = "Podana liczba jest ZA MAŁA!"
        print(odpowiedz)
        if not i == runda - 1:
            print(jeszcze_raz)

    elif wybor > liczba:
        odpowiedz = "Podana liczba jest ZA DUŻA!"
        print(odpowiedz)
        if not i == runda - 1:
            print(jeszcze_raz)

    elif wybor == liczba:
        print("Brawo, zgadłeś/aś! Odgadnięta liczba to: ", liczba)
        
    if i == runda - 1:
        print("\n\nNiestety nie udało Ci się odgadnąć wylosowanej liczby :( \n"
              "Zagraj jeszcze raz!")

input("Aby zakończyć, wciśnij ENTER")
