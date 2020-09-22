ringid = int(input("Sisestage ringide arv: "))
porgand = 0
kordus = 2

while ringid > 1:
    porgand += kordus
    kordus += 2
    ringid -= 2

print("Porgandite koguarv on "+str(porgand))