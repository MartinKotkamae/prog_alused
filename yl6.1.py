def banner(x):
    x = x.upper()
    return x

reklaamlause = input("Sisestage reklaamlause: ")

print(banner(reklaamlause))

kord = int(input("Mitu korda soovite lauset korrata: "))
reklaamlause2 = input("Kui tahate reklaamlauset muuta sisestage uus, kui ei soovi muuta sisestage (ei): ")

if reklaamlause2 == "ei":
    reklaamlause2 = reklaamlause

while kord > 0:
    print(banner(reklaamlause2))
    kord -= 1