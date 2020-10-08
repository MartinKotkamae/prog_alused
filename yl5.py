ainepunkt = int(input("Sisestage ainepunktide arv: "))
nadal = int(input("Sisestage nädalate arv: "))

ajakulu = ainepunkt * 26

najakulu = round(ajakulu / nadal)

print(najakulu)
