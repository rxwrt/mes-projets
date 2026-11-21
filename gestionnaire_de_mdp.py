
print("Bienvenue dans mon gestionaire de mot de passe vous pouvez sauvegarder seulment 2 mdp en attendant la future mise a jour !")
création_mdp = input("crée votre mot de passe maitre : ")
while True:
    print("enregister un mot de passe (entrer 1)")
    print("voir mdp enregistrer (entrer 2)")
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
        



    
        

