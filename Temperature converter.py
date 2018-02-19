#Temperature converter

C = float()
F = float()
liczba = float()

def analiza():
    if C == 0:
        print ("Jest to temperatura zamarzania.")
    elif C == 100:
        print ("Jest to temperatura wrzenia.")
    elif C < -273.15:
        print ("""Podana wartość temperatury jest niewłaściwa.\n
                Temperatura poniżej zera absolutnego!""")
    elif C >= -273.15 and C < 0:
        print("Jest to temperatura poniżej zera.")
    elif C >= 0 and C < 100:
        print("Jest to zwykła temperatura.")
    else:
        print("Temperatura powyżej temperatury wrzenia.")

def FtoC():
    ret = (liczba - 32)/1.8
    print(liczba, "*F to ", ret, "*C\n")
    return ret

def CtoF():
    ret = (liczba * 1.8) + 32
    print(liczba, "*C to ", ret, "*F\n")
    return ret


# Start konwersji

while True:
    print("""Dostępne opcje konwersji temperatury:
    FC - stopnie Fahrenheita na stopnie Celsjusza
    CF - stopnie Celsjusza na stopnie Fahenheita
    X - wyjście z programu""")
    opcja = input("Wybierz opcję: ")
    opcja = opcja.upper()

    
    if opcja == "X":
        print("Do zobaczenia!")
        break
    elif opcja == "FC":
        liczba = float(input("Wprowadź liczbę: "))
        C = FtoC()
        analiza()
    elif opcja == "CF":
        liczba = float(input("Wprowadź liczbę: "))
        C = liczba
        F = CtoF()
        analiza()
    input("Aby policzyć jeszcze raz, wciśnij Enter.")

