import random
print("Bienvenue sur mon projet calculatrice pour arrêter le programme Ctrl + C")
while True:
    
        operation = input("Vous voulez * / + ou - : ")
# debut du code easter egg
        if operation == "easter egg":
            print("bravo vous avez trouvez l'easter egg")
            debut = input("voulez vous jouez au jeu du juste prix oui/non : ")
          
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
# fin du code easter egg        
        premier_nombre = int(input("Entrez le premier nombre : "))
        deuxieme_nombre = int(input("Entrez le deuxième nombre : "))
        if operation == "+" :
            resultat_addition = premier_nombre + deuxieme_nombre
            print("Le résultat est ", resultat_addition)

        if operation == "/":
            resultat_division = premier_nombre / deuxieme_nombre
            print("Le résultat est ", resultat_division)

        if operation == "*":
            resultat_multiplication = premier_nombre * deuxieme_nombre
            print("Le résultat est ", resultat_multiplication)

        if operation == "-":
            resultat_soustraction = premier_nombre - deuxieme_nombre
            print("Le résultat est ", resultat_soustraction)

        if operation not in ["*","+","-","-","easter egg"]:
            print("merci de saisire une * + - ou +")

    except ValueError:
        print(" Attention, il faut entrer un nombre ou un signe en fonction de ce qui vous est demandé.")

    except KeyboardInterrupt :
        print(" Vous avez subitement arrêté le programme.")
        break

    except:
        print(" Une erreur est survenue.")

# pour prochaine mise a jour :
# corrigé tout les bug
# rendre le code plus propre et lisible



