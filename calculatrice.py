
print("Bienvenue sur mon projet calculatrice pour arrêter le programme Ctrl + C")
while True:
    try:
        operation = input("Vous voulez * / + ou - : ")
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
    except ValueError:
        print(" Attention, il faut entrer un nombre ou un signe en fonction de ce qui vous est demandé.")
    except KeyboardInterrupt :
        print(" Vous avez subitement arrêté le programme.")
        break
    except:
        print(" Une erreur est survenue.")
