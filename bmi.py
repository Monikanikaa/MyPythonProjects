# Program do obliczania wskaźnika BMI
imie = input("Wprowadź imię: ")
p = ""
while (p != "M" and p != "K"):
    p = input("Wprowadź płeć M / K: ")

print("\nCześć, ",imie)
print("Jeśli chcesz dowiedzieć się, czy Twoja waga jest prawidłowa,")
print ("naciśnij Enter i wykonaj polecenia.")
masa = float(input("\nPodaj wagę w kilogramach: "))
wzrost = float(input("Podaj wzrost w centymetrach: "))

# Wyświetlanie wskaźnika BMI
Wskaznik_BMI = round(float((masa / wzrost**2)*10000), 2)
print("\n\nTwój wskaźnik BMI to: ", Wskaznik_BMI)

# Opis wskaźników
if (Wskaznik_BMI <= 16):
    print("\nWygłodzenie")
    print("Lepiej idź coś zjeść ;)")
elif Wskaznik_BMI > 16 and Wskaznik_BMI < 17:
    print("\nWychudzenie")
    print("Lepiej idź coś zjeść ;)")
elif Wskaznik_BMI >= 17 and Wskaznik_BMI < 18.5:
    print("\nNiedowaga")
elif Wskaznik_BMI >= 18.5 and Wskaznik_BMI < 25:
    print("\nWaga prawidłowa")
    if p == "M":
        print("Możesz być z siebie dumny")
    else:
        print("Możesz być z siebie dumna")
elif Wskaznik_BMI >= 25 and Wskaznik_BMI < 30:
    print("\nNadwaga")
elif Wskaznik_BMI >= 30 and Wskaznik_BMI < 35:
    print("\nI stopień otyłości")
elif Wskaznik_BMI >= 35 and Wskaznik_BMI < 40:
    print("\nII stopień otyłości")
elif Wskaznik_BMI >= 40:
    print("\nOtyłość skrajna! \nMususz schudnąć, grubasie!")

input("\n\n\nAby zakończyć, wciśnij Enter")
