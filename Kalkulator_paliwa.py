import re

def koszt_podrozy():
    ret = 0
    dystans = input("Podaj długość trasy do przejechania [km]: ").replace(',', '.')
    spalanie = input("Średnie spalanie Twojego pojazdu [litry/100 km]: ").replace(',', '.')
    cena_litra = input("Podaj cenę za 1 litr paliwa: ").replace(',', '.')

    if (((re.match('^[0-9\.]*$', dystans)) and (re.match('^[0-9\.]*$', spalanie)) and (re.match('^[0-9\.]*$', cena_litra)))
    and dystans.count(".") <= 1 and spalanie.count(".") <= 1 and cena_litra.count(".") <= 1):
    #sprawdzenie czy wpisany ciąg posiada liczby 0-9 i .
        ret = round((float(dystans) / 100 * float(spalanie) * float(cena_litra)),2)
    else:
        print("Błąd!")
        
    return ret

def dystans_litry():
    ret = [0, 0]
    litry = input("Ile litrów paliwa masz do dyspozycji? ").replace(',', '.')
    spalanie = input("Średnie spalanie Twojego pojazdu [litry/100 km]: ").replace(',', '.')

    if (((re.match('^[0-9\.]*$', litry)) and (re.match('^[0-9\.]*$', spalanie )))
    and spalanie.count(".") <= 1 and litry.count(".") <= 1):
        dystans =  float(litry) / float(spalanie) * 100
        lista = [float(litry), round(dystans,2)]
        ret = lista
    else:
        print("Błąd!")

    return ret
    
def dystans_kwota():
    ret = [0, 0]
    kwota = input("Podaj kwotę, za jaką chcesz jechać: ").replace(',', '.')
    spalanie = input("Średnie spalanie Twojego pojazdu [litry/100 km]: ").replace(',', '.')
    cena_litra = input("Podaj cenę za 1 litr paliwa: ").replace(',', '.')

    if (((re.match('^[0-9\.]*$', kwota)) and (re.match('^[0-9\.]*$', spalanie)) and (re.match('^[0-9\.]*$', cena_litra)))
    and kwota.count(".") <= 1 and spalanie.count(".") <= 1 and cena_litra.count(".") <= 1):
        dystans = float(kwota) / float(cena_litra) / float(spalanie) * 100
        ret = [float(kwota), round(dystans,2)]
    else:
        print("Błąd!")
        
    return ret

 
while True:
    
    opcja = input("""Dostępne opcje:
    1 - obliczanie kosztu podróży
    2 - obliczanie maksymalnego dystansu do przejechania na x - litrach paliwa
    3 - obliczanie dystansu na podstawie kwoty wydanej na paliwo
    Wybierz opcję: """)

    if opcja == "1":
        podroz = koszt_podrozy()
        print("Koszt Twojej podróży wynosi: ", podroz, "zł.")
    elif opcja == "2":
        podroz = dystans_litry()
        print(f"Mając do dyspozycji {podroz[0]} l paliwa, możesz przejechać maksymalnie {podroz[1]} km.")
    elif opcja == "3":
        podroz = dystans_kwota()
        print(f"Mając do dyspozycji {podroz[0]} zl możesz przejechać {podroz[1]} km.")
    else:
        print("Wybór nieprawidłowy. Możesz wybrać od 1 do 3.")
        continue
