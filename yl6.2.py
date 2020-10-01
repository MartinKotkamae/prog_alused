def rahasumma (x):
    kogusumma = 55 + x*10
    return kogusumma

paljuini = int(input("Mitu inimest on kutsutud? "))
tulevadini = int(input("Mitu inimest tulevad? "))

print("Maksimaalne eelarve: "+str(rahasumma(paljuini)))
print("Minimaalne eelarve: "+str(rahasumma(tulevadini)))