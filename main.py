cm = 2.54
pouce = 0.394
def converseur():
    while True:

        print("Option : ")
        print("1- Souhaitez vous convertir pouce a cm ?")
        print("2- Souhaitez vous convertir cm a pouce ?")
        print("3- Termmine ")
        try:
            option = int(input(" choisi entre les option : /1/2/3/ : "))
            if 1 <= option <= 3:
                if option == 1:
                    try:
                        choix = float(input("Rentre le nombre de pouce que vous souhaitez convertir : "))
                        print(f"{choix} pouce equivaut a {round(choix * cm)} cm ")
                        break
                    except ValueError:
                        print("Erreur vous doit rentre un nombre pour vos valeur ")

                if option == 2:
                    try:
                        choix1 = float(input("Rentre le nombre de cm que vous souhaitez convertir : "))
                        print(f"{choix1} cm equivaut a {round(choix1 * pouce)} pouce  ")
                        break
                    except ValueError:
                        print("Erreur vous doit rentre un nombre pour vos valeur ")

                elif option == 3:
                    print("Merci au revoir !")
                    break
            else:
                print("Option invaide choisir parmis les option valide.")
        except ValueError:
            print("Erreur vous doit rentre un nombre pour votre option!")
        print()


converseur()
