kirjasuurus = float(input("Sisestage kirja suurus (mb): "))
kirjateema = input("Sisestage kirja teema pealkiri: ")
ynfile = input("Kas kirjaga on kaasas fail? (jah/ei) ")

if kirjateema == "" or ynfile == "jah" and kirjasuurus > 1:
    print("Kiri on spämm")
else:
    print("Kiri ei ole spämm")