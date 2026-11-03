
age = 20

if age < 18:
    print("vous êtes mineur")
elif age < 30:
    print("Vous êtes frais")
elif age < 40:
    print("Va falloir penser a aller chez le kiné")
else:
    print("Tic tac tic tac")

print("Fin")

jour = 2

match jour:
    case 1:
        print("Lundi des patates")
    case 2:
        print("Mardi des patates")
    case 3:
        print("Mercredi des patates aussi")
    case 7:
        print("Et le dimanche, jour du seigneur, a quel bonheur, des patates au beurre")


legume = "butternut"

match legume:
    case "brocolis":
        print(2.69)
    case "butternut" | "petitmarron":
        print(4.99)
    case "tomate":
        print(0.99)

