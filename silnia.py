x = int(input("\nPodaj liczbę: "))
wynik = int(1)
for i in range(1, x+1):
    wynik = int(wynik * i)
print("Twój wynik to: ", x, "!", "=", wynik)

input("Aby zakończyć, wciśnij ENTER.")
