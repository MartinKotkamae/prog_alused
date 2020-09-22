import random

valik1 = input("Kas soovite istekohta ise valida (""ise"") või loosida (""loos"")? ")

if valik1 == "ise":
    valik2 = input("Kas soovite istuda akna ääres (""aken"") või mitte (""muu"")? ")
    if valik2 == "aken":
        print("Valisite ise. Aknakoht")
    else:
        print("Valisite ise. Vahekäigukoht")

else:
    loosinr = (random.randint(1, 3))
    if loosinr == 1:
        print("Istekoht loositi. Aknakoht")
    else:
        print("Istekoht loositi. Vahekäigukoht")
