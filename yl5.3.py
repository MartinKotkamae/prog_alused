fail = open("kontoyl5.3.txt", encoding="UTF-8")
andmed = []

for rida in fail:
    andmed.append(float(rida))

fail.close()

for i in andmed:
    if i > 0:
        print(i)