import time

CM = 2.54
POUCE = 0.394


def convertisseur(valeur, valeur1):
    while True:
        print("Options : ")
        print(f"1- Souhaitez-vous convertir pouce en {valeur} ?")
        print(f"2- Souhaitez-vous convertir cm en {valeur1} ?")
        print("3- Terminé \n")
        try:
            option = int(input("Choisissez parmi les options : /1/2/3/ : "))

            if 1 <= option <= 3:
                if option == 1:
                    choix = float(input(f"Entrez le nombre de {valeur1} que vous souhaitez convertir : "))
                    print(f"{choix} pouces équivaut à {round(choix * CM, 2)} {valeur}\n ")

                elif option == 2:
                    choix1 = float(input(f"Entrez le nombre de {valeur} que vous souhaitez convertir : "))
                    print(f"{choix1} cm équivaut à {round(choix1 * POUCE, 2)} {valeur1}\n  ")

                elif option == 3:
                    print("Merci, au revoir !")
                    break

                input("Apluyer enter pour contionue au /1/ pour sortir\n")
                if input == 1:
                    print("Merci au voir")
                    break
                else:
                    print("Parfait on recommence!\n")
                    time.sleep(3)
                    continue

            else:
                print("Option invalide. Veuillez choisir parmi les options valides.")
        except ValueError:
            print("Erreur, vous devez entrer un nombre pour votre option! \n")


convertisseur("cm", "pouce")
