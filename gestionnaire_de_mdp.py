import random


print("Bienvenue dans mon gestionaire de mot de passe vous pouvez sauvegarder seulment 1 mdp en attendant la future mise a jour !")
print("si vous essayez d'en créé un autre le prmier sera suprimer (se bug sera bientot réctifié)")
création_mdp = input("crée votre mot de passe maitre : ")
if création_mdp == "easter egg":
    print("test")
while True:
    print("enregister un mot de passe (entrer 1)")
    print("voir mdp enregistrer (entrer 2)")
    print("utiliser générateur de mot de passe (entrer 3)")
    print("pour arrter le scripte (entrer 4)")
    choix = input("entrer le nombre corespondant a votre demande : ")
    if choix == "1":
        mdp_saisi = input("entrer votre mot de passe maitre : ")
        mdp_saisi == création_mdp
        if création_mdp is not mdp_saisi:
            print("mot de passe erroné veuiller relancer le scripte")
            exit()
        mdp_1_url = input("entrer l'url du site : ")
        mdp_1 = input("entrer mot de passe : ")
    if choix ==  "2":
        mdp_saisi_2 = input("entrer votre mot de passe maitre : ")
        mdp_saisi_2 == création_mdp
        if création_mdp is not mdp_saisi:
            print("mot de passe erroné veuiller relancer le scripte")
            exit()
        print("url" ,mdp_1_url ,"mdp" , mdp_1)
    if choix == "3":
        mdp_saisi_3 = input("entrer votre mot de passe maitre : ")
        nombre_de_caractére = int(input("entrer le nombre de caractére que vous souaiter : "))
        mdp_saisi_3 == création_mdp
        caractéres = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%"
        mdp_généré =  ""
        for loop in range (nombre_de_caractére):
            mdp_généré += random.choice(caractéres)
        print("le mot de passe generer est " , mdp_généré )
        if création_mdp is not mdp_saisi_3:
            print("mot de passe erroné veuiller relancer le scripte")
            exit()
    if choix == "4":
        exit()
    
        


# pour la prochaine mise a jour:
# réctifier le bug dont on parle dans la ligne 3
# faire une option easter egg
# ou quand on mettrera easter
# egg dans mdp principale sa 
# lance le juste prix
        



    
        

