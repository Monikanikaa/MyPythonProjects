# Kalkulator napiwku
# Oblicza kwoty napiwku w wysokości 15% i 20% ogólnej kwoty rachunku

print("Celem programu jest obliczenie za Ciebie kwoty, jaką powinieneś wręczyć "
      + "\nkelnerowi w ramach napiwku za Twoje zamówienie."
      + "\nNapiwek naliczony jest w dwóch wariantach - 15% i 20%. \n")

print("\n")
suma_rachunku = float(input("Wprowadź sumę widoczną na Twoim rachunku: "))
napiwek_15 = round(float(suma_rachunku * 0.15), 2)
napiwek_20 = round(float(suma_rachunku * 0.20), 2)

print("\n")
print("Wariant 15 - procentowy napiwku to: %0.2f" %(napiwek_15),"zł.")
print("Wariant 20 - procentowy napiwku to: %0.2f" %(napiwek_20),"zł.")

input("\nAby zakończyć, wciśnij Enter.")
