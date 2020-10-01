import random

taringuarv = int(input("Täringute arv: "))

while taringuarv > 0:
    arv = random.randint(1,6)
    print(arv)
    taringuarv -= 1