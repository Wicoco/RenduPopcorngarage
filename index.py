from PIL import Image

"""films = ["Matrix", "Dracula", "Scream", "Saw", "Hook", "Zorro", "Batman", "Watchmen", "Avatar", "ET"]"""

films_trouves = []

tentatives = 0
max_erreurs = 3
score = 0

def afficher_image():
    try:
        image = Image.open("popcorn_garage.jpg")
        image.show()
    except FileNotFoundError:
        print("Image non trouvée. Assurez-vous que le fichier existe dans le répertoire.")

def jouer():
    global tentatives, score
    
    afficher_image()
    
    while tentatives < max_erreurs:
        proposition = input("Devinez un film : ").strip().title()
        if proposition in films_trouves:
            print("Déjà trouvé !")
        elif proposition in films:
            print("Bravo, vous avez trouvé un film !")
            films_trouves.append(proposition)
            score += 1
        else:
            print("Mauvaise réponse.")
            tentatives += 1
        if len(films_trouves) == len(films):
            print("Félicitations, vous avez trouvé tous les films !")
            break

        print(f"Score : {score}")
        print(f"Erreurs restantes : {max_erreurs - tentatives}")

    if tentatives == max_erreurs:
        print("Game Over ! Vous avez épuisé vos tentatives.")

jouer()

def charger_films(fichier):
    try:
        with open(fichier, 'r') as f:
            return [ligne.strip() for ligne in f]
    except FileNotFoundError:
        print("Fichier non trouvé.")
        return []

films = charger_films("films.txt")
