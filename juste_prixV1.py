import random
debut = input("bravo vous avez trouver l'easter egg voulez vous jouez au jeu du juste prix oui/non : ")

if debut == "oui":
    nombre = random.randint(1, 100)

while True:
    try:
            if debut not in ["oui","non"]:
                debut = input(" repondez oui ou non : ")

            if debut == "non":
                print("veiller relancer le programme")
                exit()

            if debut == "oui":
                nombre_deviner = int(input("essayer de trouver le nombre entre 0 et 100 : "))
            
                if nombre_deviner > nombre:
                    print("le nombre est plus petit")

                if nombre_deviner < nombre:
                    print("le nombre est plus grand")

                if nombre_deviner == nombre:
                    print("bravo vous avez trouvez le bon nombre", nombre )
                    break
    except ValueError:
        print("rentrer un nombre ")