# Sprzedawca samochodu
# Aplikacja do obliczania rzeczywistego kosztu związanego z zakupem rejestracją auta
# Podatek od kupna: 2% wartości auta

cena_auta = float(input("Wprowadz cene auta w zl: "))
recykling = 500 #opłata recyklingowa (rejestracja w PL przed 2016): 500zł
podatek = cena_auta * 0.02
DR = 54
pozw_czas = 13.5 #pozwolenie czasowe
nk = 18.5 #naklejka kontrolna
nl = 12.5 #naklejka legalizacyjna
oe = 2 #opłata ewidencyjna

tab = input("Tablica rejestracyjna zwykła czy indywidualna?"
            "\nZwykła - z, indywidualna - i: ")
tab = tab.lower()
if (tab == "i"):
    tab = 1000
elif(tab == "z"):
    tab = 80

r = input("Czy auto pierwsza rejestracja w kraju nastąpiła przed 2016r.?"
          "\nT lub N: ")
r = r.upper()
if (r == "T"):
    r = recykling
elif(r == "N"):
    r = 0

koszt = cena_auta + podatek + DR + pozw_czas + nk + nl + oe + tab + r

print("Koszt całkowity Twojego nowego auta wynosi: ", koszt, "zł")
input("\nAby zakończyć wciśnij Enter.")
