liczby = [6, 2, 10, 4, 9, 3, 5, 1, 7]

"""liczby.sort()
print(max(liczby))
"""



for i in range(len(liczby) - 1):
    for i in range(len(liczby) - 1):
        if (liczby[i] > liczby[i+1]):
            x = liczby[i]
            liczby[i] = liczby[i+1]
            liczby[i+1] = x
        else:
            continue
        for i in range(len(liczby)):
            print(liczby[i])
        print("koniec petli wewnetrznej")
    print("koniec petli zewnetrznej\n\n")
