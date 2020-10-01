fail = open("rebasedyl5.1.txt", encoding="UTF-8")

vastuvõetud = []

for rida in fail:
    vastuvõetud.append(int(rida))

fail.close()

sisseaasta = int(input("Sisestage vastuvõttu aasta(2011/2019): "))
vastuvõetudinimesed = 0

for i in vastuvõetud:
    if i == sisseaasta:
        vastuvõetudinimesed += 1

print("Aastal "+str(sisseaasta)+" ,võeti vastu "+str(vastuvõetudinimesed)+" inimene/inimest")
