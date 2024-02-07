import time

cm = 2.54
pouce = 0.394


def convertisseur():
    while True:
        print("Options : ")
        print("1- Souhaitez-vous convertir pouce en cm ?")
        print("2- Souhaitez-vous convertir cm en pouce ?")
        print("3- Terminé \n")
        try:
            option = int(input("Choisissez parmi les options : /1/2/3/ : "))
            print()
            if 1 <= option <= 3:
                if option == 1:
                    choix = float(input("Entrez le nombre de pouces que vous souhaitez convertir : "))
                    print(f"{choix} pouces équivaut à {round(choix * cm, 2)} cm\n ")
                    input("Apluyer enter pour contionue au /1/ pour sortir\n")
                    if input == 1:
                        print("Merci au voir")
                        break
                    else:
                        print("Parfait on recommence! \n")
                        time.sleep(3)
                        continue

                elif option == 2:
                    choix1 = float(input("Entrez le nombre de cm que vous souhaitez convertir : "))
                    print(f"{choix1} cm équivaut à {round(choix1 * pouce, 2)} pouces\n  ")
                    input("Apluyer enter pour contionue au /1/ pour sortir\n")
                    if input == 1:
                        print("Merci au voir")
                        break
                    else:
                        print("Parfait on recommence!\n")
                        time.sleep(3)
                        continue

                elif option == 3:
                    print("Merci, au revoir !")
                    break
            else:
                print("Option invalide. Veuillez choisir parmi les options valides.")
        except ValueError:
            print("Erreur, vous devez entrer un nombre pour votre option!")
        print()


convertisseur()
