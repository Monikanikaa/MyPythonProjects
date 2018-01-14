# Kalkulator

import math

mem = float(0)
wynik = float(0)
while(1):
    print("\nSpis czynności:\n"
          "+ - dodawanie\n"
          "- - odejmowanie\n"
          "* - mnożenie\n"
          "/ - dzielenie\n"
          "** - potęgowanie\n"
          "$ - pierwiastkowanie\n"
          "! - silnia\n\n"
          "Czynności dostępne po wykonaniu pierwszego działania: \n"
          "M+ - dodaje wynik do pamięci kalkulatora\n"
          "M- - odejmuje wynik od pamięci kalkulatora\n"
          "MR - wyświetla zawartość pamięci\n\n")

    czynnosc = ""
    a = input("Czy chcesz wykonać operację na pamięci kalkulatora? T/N ")
    a = a.upper()
    if (a == "T"):
        czynnosc2 = input("Co zrobić z wynikiem? ")
        if (czynnosc2 == "M+"):
            mem = mem + wynik
        elif (czynnosc2 == "M-"):
            mem = mem - wynik
        elif (czynnosc2 == "MR"):
            print("Pamięć: ", mem)
        else:
            print("Twój wynik to: ", wynik)
    if (a == "N"):
        x = float(input("Podaj pierwszą liczbę: "))
        czynnosc = input("Podaj czynność: ")
        if(czynnosc != "$" and czynnosc != "!"):
            y = float(input("Podaj drugą liczbę: "))



    if (czynnosc == "+"):
        wynik = x + y
        print("Twój wynik to: ", x, "+", y, "=", wynik)
        czynnosc2 = input("Co zrobić z wynikiem? ")
        if (czynnosc2 == "M+"):
            mem = mem + wynik
        elif (czynnosc2 == "M-"):
            mem = mem - wynik
        elif (czynnosc2 == "MR"):
            print("Pamięć: ", mem)

    elif (czynnosc == "-"):
        wynik = x - y
        print("Twój wynik to: ", x, "-", y, "=", wynik)
        czynnosc2 = input("Co zrobić z wynikiem? ")
        if (czynnosc2 == "M+"):
            mem = mem + wynik
        elif (czynnosc2 == "M-"):
            mem = mem - wynik
        elif (czynnosc2 == "MR"):
            print("Pamięć: ", mem)

    elif (czynnosc == "*"):
        wynik = x * y
        print("Twój wynik to: ", x, "*", y, "=", wynik)
        czynnosc2 = input("Co zrobić z wynikiem? ")
        if (czynnosc2 == "M+"):
            mem = mem + wynik
        elif (czynnosc2 == "M-"):
            mem = mem - wynik
        elif (czynnosc2 == "MR"):
            print("Pamięć: ", mem)

    elif (czynnosc == "/") and (y != 0):
        wynik = x / y
        print("Twój wynik to: ", x, "/", y, "=", wynik)
        czynnosc2 = input("Co zrobić z wynikiem? ")
        if (czynnosc2 == "M+"):
            mem = mem + wynik
        elif (czynnosc2 == "M-"):
            mem = mem - wynik
        elif (czynnosc2 == "MR"):
            print("Pamięć: ", mem)

    elif (czynnosc == "/") and (y == 0):
        print("Cholero! Nie dziel przez 0!")
        czynnosc2 = input("Co zrobić z wynikiem? ")
        if (czynnosc2 == "M+"):
            mem = mem + wynik
        elif (czynnosc2 == "M-"):
            mem = mem - wynik
        elif (czynnosc2 == "MR"):
            print("Pamięć: ", mem)

    elif (czynnosc == "**"):
        wynik = x**y
        print("Twój wynik to: ", x, "^", y, "=", wynik)
        czynnosc2 = input("Co zrobić z wynikiem? ")
        if (czynnosc2 == "M+"):
            mem = mem + wynik
        elif (czynnosc2 == "M-"):
            mem = mem - wynik
        elif (czynnosc2 == "MR"):
            print("Pamięć: ", mem)

    elif (czynnosc == "$"):
        wynik = math.sqrt(x)
        print("Twój wynik to: ", "pierwiastek z ", x,"=", wynik)
        czynnosc2 = input("Co zrobić z wynikiem? ")
        if (czynnosc2 == "M+"):
            mem = mem + wynik
        elif (czynnosc2 == "M-"):
            mem = mem - wynik
        elif (czynnosc2 == "MR"):
            print("Pamięć: ", mem)

    elif (czynnosc == "!"):
        wynik = int(1)
        for i in range(1, int(x+1)):
            wynik = (wynik * i)
        print("Twój wynik to: ", wynik)
        czynnosc2 = input("Co zrobić z wynikiem? ")
        if (czynnosc2 == "M+"):
            mem = mem + wynik
        elif (czynnosc2 == "M-"):
            mem = mem - wynik
        elif (czynnosc2 == "MR"):
            print("Pamięć: ", mem)
            

input("\n\nAby zakończyć, wciśnij ENTER. ")

