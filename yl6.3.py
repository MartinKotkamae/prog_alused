def kuu_nimi(x):
    kuud = ["jaanuar", "veebruar", "märts", "aprill", "mai",
            "juuni", "juuli", "august", "september", "oktoober", "november", "detsember"]
    getmonth = x.split(".")
    kuu = kuud[int(getmonth[1])-1]
    x = (getmonth[0])+". "+str(kuu)+" "+str(getmonth[2])+". a"
    return x

kuupäev = input("Sisesta kuupäev kujul DD.MM.YYYY: ")

print(kuu_nimi(kuupäev))