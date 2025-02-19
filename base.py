statut = False
if statut == False: 
    print("Je suis pas là")
else: # elif statut == True:
    print("Je suis là")


y = 3.1
x = 1
print(type(y))
print(x + y)


dep = 99
if dep == 100:
    print("égal à 100")
elif dep < 100:
    print("Inférieur à 100")
else:
    print("Supérieur à 100")



for i in range(6): # Commence de 0 et pas 1
    print(i)

zero = 0
while zero < 6:
     print(zero)
     zero += 1


try:
    x = 10 / 0 
except ZeroDivisionError:
    print("Erreur : division par zéro !")

prénom = "Jean" 
def salut(nom):
    return f"Salut, mon ami {nom}"
print(salut(prénom))



def power(x, y=2):
    return x ** y

print(power(3))  # 3^2 = 9
print(power(3, 3))  # 3^3 = 27



print(len("Python"))  # Longueur : 6
print(abs(-10))       # Valeur absolue : +10
print(max(3, 7, 1))   # Plus grand : 7
print(min(3, 7, 1))   # Plus petit: 1
print(sum([1, 2, 3])) # Addition : 1+2+3 = 6



fruits = ["Banane", "Pomme"]
fruits.append("Poire") 

quantite = (2, 3, 1)
unique = {1, 2, 3, 3, 4}
print(unique) # {1, 2, 3, 4} - Pas de doublon

print("Tu voudrais une " + fruits[0] + " et en prendre " + str(quantite[0]))



fruit = {"1": "Pomme", "Statut": "Pourris"} 
print("Tiens une " + fruit["1"] + " qui est " + fruit["Statut"])
fruit["Statut"] = "Très bon"
print("Tiens une " + fruit["1"] + " qui est " + fruit["Statut"])
