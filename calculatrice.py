
print("Bienvenue sur mon projet calculatrice pour arrêter le programme Ctrl + C")
while True:
    try:
        operation = input("Vous voulez * / + ou - : ")
        premier_nombre = int(input("Entrez le premier nombre : "))
        deuxieme_nombre = int(input("Entrez le deuxième nombre : "))
        if operation == "easter egg":
            print("bravo vous avez trouvez l'easter egg")
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
# faire un autre scripte que
# se lancera quand on utilisera
# l'easter egg exemple un jeu



