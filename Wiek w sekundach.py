from datetime import date

rok = int(input("W którym roku się urodziłeś/aś?: "))
mies = int(input("W którym miesiącu się urodziłeś/aś? Podaj liczbę: "))
dzien = int(input("W którym dniu się urodziłeś/aś? "))
urodziny = date(rok, mies, dzien)

dzisiaj = date.today()
print("\nDziś jest ", dzisiaj,".")

wiek_w_dniach = dzisiaj - urodziny
wiek_w_dniach = wiek_w_dniach.days
print("\nMasz {} dni.".format(wiek_w_dniach))

wiek_w_sekundach = int(wiek_w_dniach) * 86400
print("To jest ", wiek_w_sekundach, "sekund.")
