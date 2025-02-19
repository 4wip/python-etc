import random

nombre = random.randint(1, 100)

i = 0

while True:
    user = int(input("Entre un nombre : "))
    i += 1
    if user == nombre:
        print("Bravo !")
        break
    elif user < nombre:
        print("Trop petit !")
    elif user > nombre:
        print("Trop grand !")

print(f'Tu a réussi en {i} tentatives.')