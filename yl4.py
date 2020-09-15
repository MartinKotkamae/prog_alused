nimi = input("Sisestage oma nimi: ")
lkiirus = int(input("Sisestage lubatud kiirus (km/h): "))
tkiirus = int(input("Sisestage tegelik kiirus (km/h): "))

vahe = tkiirus-lkiirus
if vahe > 0:
    trahv = vahe*3
    if trahv > 190:
        trahv = 190
    print(nimi + ", kiiruse ületamise eest on teie trahv " + str(trahv) + " eurot")
else:
    print(nimi + ", kiiruse ületamise eest on teie trahv 0 eurot")

