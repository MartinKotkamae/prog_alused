import random

poialpoiss = int(input("Mitu pöialpoissi tahab õuna (0/7)? "))
ounukokku = 14

while poialpoiss > 0:
    ounarv = random.randint(1,2)
    print(ounarv)
    ounukokku -= ounarv
    poialpoiss -= 1

print("Lumivalgekesele jäi "+str(ounukokku))
