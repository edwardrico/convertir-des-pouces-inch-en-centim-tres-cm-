cm = 2.54
pouce = 0.394


def convertisseur():
    while True:
        print("Options : ")
        print("1- Souhaitez-vous convertir pouce en cm ?")
        print("2- Souhaitez-vous convertir cm en pouce ?")
        print("3- Terminé ")
        try:
            option = int(input("Choisissez parmi les options : /1/2/3/ : "))
            if 1 <= option <= 3:
                if option == 1:
                    choix = float(input("Entrez le nombre de pouces que vous souhaitez convertir : "))
                    print(f"{choix} pouces équivaut à {round(choix * cm, 2)} cm ")
                    break

                if option == 2:

                    choix1 = float(input("Entrez le nombre de cm que vous souhaitez convertir : "))
                    print(f"{choix1} cm équivaut à {round(choix1 * pouce, 2)} pouces  ")
                    break

                elif option == 3:
                    print("Merci, au revoir !")
                    break
            else:
                print("Option invalide. Veuillez choisir parmi les options valides.")
        except ValueError:
            print("Erreur, vous devez entrer un nombre pour votre option!")
        print()


convertisseur()
