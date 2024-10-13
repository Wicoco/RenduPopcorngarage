def jeu_pendu():
    mot_a_deviner = input("Entrez le mot à deviner : ").lower()
    lettres_trouvees = set()
    tentatives = 6

    while tentatives > 0:
        etat = ''.join([lettre if lettre in lettres_trouvees else '_' for lettre in mot_a_deviner])
        print("Mot à deviner :", etat)
        print(f"Tentatives restantes : {tentatives}")
        lettre = input("Proposez une lettre : ").lower()

        if lettre in lettres_trouvees:
            print("Lettre déjà proposée.")
        elif lettre in mot_a_deviner:
            lettres_trouvees.add(lettre)
            print("Bien joué !")
        else:
            tentatives -= 1
            print("Dommage !")

        if all(l in lettres_trouvees for l in mot_a_deviner):
            print("Félicitations, vous avez deviné le mot :", mot_a_deviner)
            return

    print("Vous avez perdu. Le mot était :", mot_a_deviner)

jeu_pendu()