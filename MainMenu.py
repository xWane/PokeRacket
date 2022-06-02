# Main Menu --> Créer une game
#           --> Lancer une sauvegarde
#           --> Paramètre
#           --> Exit

from os import system
from time import sleep
from keyboard import *


from random import randint
from Fonctions_RPG_2_0 import *
import time
import pickle
import sys


def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.02)
    return ""


def create_game():
    print()
    word_Yes_No = ["1", "2"]

    i = 0

    while i < 10000:
        choice = input(delay_print(""" 
        Voulez-vous lancer une nouvelle partie ? (Vous risquez de supprimer une partie précédement sauvegardée) 
                                            1 - Oui        2 - Non

        """))

        choice_lower = choice.lower()
        clear = system('cls')

        if word_Yes_No[0] == choice_lower:
            print()
            delay_print("Vous voici dans une nouvelle sauvegarde :")
            print()
            print()
            name = input(delay_print("Choissisez un pseudo : "))
            print()

            delay_print("Votre partie va se lancer {}".format(name))
            time.sleep(3)
            pickle_out = open("name.pickle", "wb")
            pickle.dump(name, pickle_out)
            pickle_out.close()
            clear = system('cls')
            return True
        elif word_Yes_No[1] == choice_lower:
            return False

        elif choice_lower != word_Yes_No[0] and choice_lower != word_Yes_No[1]:
            delay_print("Erreur")

        i = i + 1


def setting():
    print()
    setting_choice = ["1", "2", "3", "4"]
    clear = system('cls')

    i = 0
    while i < 1000:

        choice = input(delay_print("""
    1 - Régles du jeux
    2 - Crédits
    3 - Commandes
    4 - Retour
    """))

        clear = system('cls')

        if choice == setting_choice[0]:
            delay_print("""
                1 - Régles du jeux
                
                        Les règles sont simples. Vous êtes le héros de cette aventure. Let's go mgl ! Vous devrez vaincre les ennemis pour sauver quelqu'un qui vous est cher..
            
            """)
            input(delay_print("\n"" <  Appuyez sur Entrée pour Quitter >"))
            clear = system('cls')

        elif choice == setting_choice[1]:

            delay_print("""
                2 - Crédits
                        Ce superbe jeu a été développé par Billy l'ultime boss, Anthony The master, Ewan le Président et Louis Le Dieu des Dieux !! 
            
            """)
            input(delay_print("press any key to return to settings"))
            clear = system('cls')

        elif choice == setting_choice[2]:
            delay_print("""
                3 - Commandes
                        Les commandes sont exclusivement liées à votre clavier (pour le moment.... A l'avenir, on souhaite vous proposer une expérience liée à la Kinect lol) :
                        - Avancer devant : ↑
                        - Avancer en arrière : ↓
                        - Avancer vers la droite : → 
                        - Avancer vers la gauche : ←
                        - Valider : a 
                        - Retour : b
                        - Inventaire : x
                        - Statistiques joueur : y 
            """)
            input(delay_print("\n"" <  Appuyez sur Entrée pour Quitter >"))
            clear = system('cls')

        elif choice == setting_choice[3]:
            return delay_print("Vous avez quitté les paramètres")

        elif choice != setting_choice[0] or choice != setting_choice[1] or choice != setting_choice[2] or choice != setting_choice[3]:
            delay_print(
                "Erreur, séléctionner une option comprise entre 1 et 4 !")
            input(delay_print("\n"" <  Appuyez sur Entrée pour Quitter >"))
            clear = system('cls')


def let():

    i = 0

    while i < 1000:
        print()
        delay_print(
            "Bonjour jeune aventurier ! Te voila dans un nouveau jeu dément.""\n")

        choice = input(("""
        1 -- Créer une partie
        2 -- Charger une partie
        3 -- Paramètres
        4 -- Quitter

        """))

        clear = system('cls')

        choice_game_list = ["1", "2", "3", "4"]
        if choice == choice_game_list[0]:

            game = create_game()
            print(game)
            while game == True:
                # Stats de base du joueur qui change en fonction du niveau

                niveau_joueur = 80
                xp_joueur = 0
                xp_prochain_niveau = 100 + ((100//10) * niveau_joueur)
                stats_attaque_joueur_base = 100
                stats_attaque_joueur = stats_attaque_joueur_base + \
(stats_attaque_joueur_base * (niveau_joueur//10))

                stats_defense_joueur_base = 100
                stats_defense_joueur = stats_defense_joueur_base + \
(stats_defense_joueur_base * (niveau_joueur//10))

                stats_vie_total_joueur_base = 100
                stats_vie_total_joueur = stats_vie_total_joueur_base + \
                    (stats_vie_total_joueur_base * (niveau_joueur//10))
                stats_vie_joueur = stats_vie_total_joueur

                # valeur qui permet de sauvegarder l'état du cooldown de l'attaque chargée (attaque1)
                cooldown = 1

                attaque1 = "Jackpot"
                # dégats de l'attaque augmenter par la stat d'attaque du joueur
                effet1 = 20 + (20//10 * (stats_attaque_joueur//10))

                attaque2 = "Griffe"
                effet2 = 10 + (10//10 * (stats_attaque_joueur//100))

                #  Stats d'un ennemi témoin , on en aura besoin plus tard

                stats_vie_ennemi = 0
                stats_attaque_ennemi = 0
                stats_defense_ennemi = 0
                nom_ennemi = 0
                niveau_ennemi = 0
                attaque_ennemi_1 = 0
                attaque_ennemi_2 = 0
                effet_attaque_ennemi1 = 0
                effet_attaque_ennemi2 = 0
                xp_ennemi = 0
                cooldown_ennemi = 0

                zone = 1  # la zone 1 est la zone de départ , savoir dans quelle zone on se trouve change les Pokémon rencntrable

                list_item = []  # liste de nos objets
                ListPokemonInBag = []  # liste des Pokémon capturés
                bank_account = 1000  # Compte en banque

                X = 7            # coordonnées de spawn du joueur
                Y = 7

                zone = 1
                map_ville = [["■", "■", "■", "■", "■", "■", "■", "F", "F", "■", "■", "■", "■", "■", "■", "■"],
                             ["■", " ", " ", " ", " ", " ", "■", " ",
                              " ", " ", " ", "■", " ", " ", "R", "■"],
                             ["■", " ", " ", " ", " ", " ", "■", " ",
                                 " ", "■", " ", "■", " ", "■", "■", "■"],
                             ["■", "■", "■", " ", "■", "■", "■", " ",
                                 " ", "■", " ", " ", " ", "■", "H", "■"],
                             ["■", "H", "H", " ", "H", "H", "H", " ",
                              " ", "■", "■", "■", "■", "■", "H", "■"],
                             ["■", "H", "H", " ", "H", "H", "H", " ",
                              " ", "H", "H", "H", "H", "D", "H", "■"],
                             ["F", " ", " ", " ", " ", " ", " ", " ",
                              " ", " ", " ", " ", " ", " ", " ", "Z"],
                             ["F", " ", " ", " ", " ", " ", " ", " ",
                              " ", " ", " ", " ", " ", " ", " ", "Z"],
                             ["F", " ", " ", " ", " ", " ", " ", " ",
                              " ", " ", " ", " ", " ", " ", " ", "Z"],
                             ["■", "H", "D", "H", "H", "H", " ", " ",
                              " ", "H", "H", "H", "H", "H", "H", "■"],
                             ["■", "■", "■", "H", "H", "H", " ", " ",
                              " ", "H", "H", "H", "H", "H", "H", "■"],
                             ["■", " ", "■", " ", " ", " ", " ", " ",
                              " ", "H", "H", "H", "H", "T", "T", "■"],
                             ["■", " ", "■", " ", " ", " ", " ", " ",
                              " ", "H", "■", "■", "■", "■", "■", "■"],
                             ["■", "■", "■", "■", "■", " ", "H", " ",
                              " ", " ", " ", " ", " ", " ", "D", "■"],
                             ["■", "E", " ", " ", " ", " ", "H", " ",
                              " ", "H", "■", " ", " ", " ", " ", "■"],
                             ["■", "■", "■", "■", "■", "■", "■", "P", "P", "■", "■", "■", "■", "■", "■", "■"]]

                map_foret = [["■", "■", "■", "■", "■", "■", "■", "■", "■", "■", "■", "■", "■", "■", "■", "■"],
                             ["■", "H", "H", "H", "H", "H", "H", "H",
                              "H", "■", "H", "H", "H", "H", "H", "■"],
                             ["■", "H", "H", "H", "H", "H", "H", "H",
                              "H", "■", "H", "H", "H", "H", "H", "■"],
                             ["■", "H", "H", "■", "■", "■", "■", "■",
                              "H", "■", "H", "H", "H", "H", "H", "■"],
                             ["■", "H", "H", "■", "L", "L", "L", "■",
                              " ", " ", " ", " ", " ", " ", "D", "■"],
                             ["■", "H", "H", "■", "L", "L", "L", "■",
                              " ", " ", " ", " ", " ", " ", " ", "■"],
                             ["■", "H", "H", "■", "■", "L", "■", "■",
                              " ", " ", " ", " ", " ", " ", " ", "V"],
                             ["■", "H", "H", "H", "■", "L", "■", "■",
                              "■", "■", "■", " ", " ", " ", " ", "V"],
                             ["■", " ", " ", " ", "■", "L", "■", " ",
                              " ", " ", "■", " ", " ", " ", " ", "V"],
                             ["■", " ", " ", " ", "■", "L", "■", "D",
                              " ", "■", "■", " ", " ", " ", " ", "■"],
                             ["■", "D", "■", " ", "■", "L", "■", " ",
                              " ", "■", "■", " ", "H", "■", "■", "■"],
                             ["■", "■", "■", " ", "■", "■", "■", " ",
                              " ", " ", " ", " ", "H", "H", "H", "■"],
                             ["C", " ", " ", " ", "H", "H", "■", "H",
                              "■", "H", "H", "H", "H", "H", "H", "■"],
                             ["C", " ", " ", " ", "■", "H", "■", "H",
                              "■", "H", "H", "H", "H", "H", "H", "■"],
                             ["C", " ", " ", " ", "■", "H", "H", "H",
                              "■", "H", "H", "H", "H", "H", "H", "■"],
                             ["■", "■", "■", "■", "■", "■", "■", "■", "■", "■", "■", "■", "■", "■", "■", "■"]]

                map_plage = [["■", "■", "■", "■", "■", "■", "■", "V", "V", "■", "■", "■", "■", "■", "■", "■"],
                             ["■", " ", " ", " ", " ", " ", " ", " ",
                                 " ", " ", " ", " ", "H", "H", "H", "■"],
                             ["■", " ", " ", "D", " ", " ", " ", " ",
                                 " ", " ", " ", "H", "H", "H", "H", "■"],
                             ["■", " ", " ", " ", " ", " ", " ", "H",
                                 "H", "H", " ", " ", "H", "H", "H", "■"],
                             ["■", "H", "H", " ", " ", " ", "H", "H",
                              "H", "H", " ", " ", " ", "H", " ", "■"],
                             ["■", "H", "H", " ", " ", " ", "H", "H",
                              " ", " ", " ", " ", " ", "D", " ", "■"],
                             ["■", "H", "H", "H", " ", " ", " ", " ",
                              " ", " ", "H", "H", " ", " ", " ", "■"],
                             ["■", "H", "H", "H", " ", " ", "H", "H",
                              "H", " ", "H", "H", "H", " ", " ", "■"],
                             ["■", "H", "H", " ", " ", " ", "H", "H",
                              "H", " ", "H", "H", "H", " ", " ", "■"],
                             ["■", " ", "H", " ", " ", "H", "H", "H",
                              "H", " ", " ", "H", "H", "H", " ", "■"],
                             ["■", " ", " ", " ", " ", "H", "H", "H",
                              " ", " ", " ", " ", "H", "H", " ", "■"],
                             ["■", " ", "D", " ", " ", " ", " ", " ",
                              " ", " ", " ", " ", " ", " ", " ", "■"],
                             ["■", " ", " ", " ", " ", " ", " ", " ",
                              "O", "O", " ", " ", " ", " ", " ", "■"],
                             ["■", " ", " ", "O", "O", " ", "O", "O",
                              " ", " ", "O", " ", "O", "O", " ", "■"],
                             ["■", " ", "O", " ", " ", "O", " ", " ",
                              " ", " ", " ", "O", " ", " ", "O", "■"],
                             ["■", "O", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "■"], ]

                map_ocean = [["■", "P", "P", "P", "P", "P", "P", "P", "P", "P", "P", "P", "P", "P", "P", "■"],
                             ["■", " ", " ", " ", " ", " ", " ", " ",
                                 " ", " ", " ", " ", " ", " ", " ", "■"],
                             ["■", "H", "H", " ", " ", " ", " ", " ",
                                 " ", " ", " ", " ", " ", " ", " ", "■"],
                             ["■", "H", "H", " ", " ", " ", " ", " ",
                                 " ", " ", " ", " ", " ", " ", " ", "■"],
                             ["■", "H", "H", "H", " ", " ", "D", " ",
                              " ", "H", "H", " ", " ", "D", " ", "■"],
                             ["■", " ", "H", "H", " ", " ", " ", " ",
                              "H", "H", "H", "H", " ", " ", " ", "■"],
                             ["■", " ", "H", "H", " ", " ", " ", " ",
                              " ", "H", "H", " ", " ", " ", " ", "■"],
                             ["■", " ", " ", " ", " ", " ", " ", " ",
                              " ", " ", " ", " ", " ", " ", " ", "■"],
                             ["■", " ", " ", "D", " ", " ", " ", " ",
                              " ", " ", " ", " ", " ", "H", " ", "■"],
                             ["■", "H", " ", " ", " ", " ", " ", "H",
                              "H", "H", " ", " ", "H", "H", "H", "■"],
                             ["■", "H", "H", " ", " ", "H", "H", "H",
                              "H", "H", "H", " ", "H", "H", "H", "■"],
                             ["■", "H", "H", " ", " ", "H", "H", "H",
                              "H", "H", "H", "H", " ", "H", " ", "■"],
                             ["■", "H", "h", "H", " ", " ", "H", "H",
                              "H", "H", "H", "H", "H", " ", " ", "■"],
                             ["■", "H", "H", "H", " ", " ", " ", "H",
                              "H", "H", "H", "H", " ", " ", " ", "■"],
                             ["■", " ", "H", "H", " ", " ", " ", " ",
                              " ", " ", " ", " ", " ", " ", " ", "■"],
                             ["■", "■", "■", "■", "■", "■", "■", "■", "■", "■", "■", "■", "■", "■", "■", "■"], ]

                map_campagne = [["■", "S", "S", "■", "■", "■", "■", "■", "■", "■", "■", "■", "■", "■", "■", "■"],
                                ["■", " ", " ", "■", "H", "H", "H", " ",
                                    " ", " ", "H", "H", "H", "H", "D", "■"],
                                ["■", " ", " ", "■", "H", "H", "H", " ",
                                    " ", " ", "H", "H", "H", "■", "■", "■"],
                                ["■", " ", " ", "■", "H", "H", "H", " ",
                                    " ", "■", "H", "H", "H", "■", "M", "■"],
                                ["■", " ", " ", " ", "H", "H", "H", " ",
                                 " ", "■", "H", "H", "H", "■", "■", "■"],
                                ["■", " ", " ", " ", "H", "H", "H", " ",
                                 " ", "■", "H", "H", "H", "H", "H", "■"],
                                ["■", "■", "■", "■", "■", "■", "■", " ",
                                 " ", "■", "■", "■", "■", "■", "■", "■"],
                                ["■", " ", " ", " ", " ", " ", "D", " ",
                                 " ", " ", " ", " ", " ", "H", "H", "■"],
                                ["■", " ", " ", " ", " ", " ", " ", " ",
                                 " ", " ", " ", " ", " ", "H", "H", "■"],
                                ["■", " ", " ", " ", "H", "H", "H", "H",
                                 "H", "■", "■", "■", " ", "H", "H", "■"],
                                ["■", " ", " ", " ", "H", "H", "H", "H",
                                 "H", "■", "M", "■", " ", "H", "H", "■"],
                                ["■", "■", "■", " ", "■", "■", "■", "■",
                                 "■", "■", "■", "■", " ", " ", "■", "■"],
                                ["■", "H", "H", " ", " ", " ", " ", " ",
                                 " ", " ", " ", " ", " ", " ", " ", "F"],
                                ["■", "H", "H", "H", " ", " ", " ", " ",
                                 " ", " ", " ", " ", " ", " ", " ", "F"],
                                ["■", "H", "H", "H", "H", " ", " ", " ",
                                 " ", "D", " ", " ", " ", " ", " ", "F"],
                                ["■", "■", "■", "■", "■", "■", "■", "■", "■", "■", "■", "■", "■", "■", "■", "■"]]

                map_safari = [["■", "■", "■", "■", "■", "■", "■", "■", "■", "■", "■", "■", "■", "■", "■", "■"],
                              ["■", "H", " ", "H", "■", "H", "H", "H",
                                  "H", "H", "H", "H", "H", "H", " ", "■"],
                              ["■", "H", " ", "H", "■", "H", " ", "H",
                                  "H", "H", "H", "H", "H", "H", "H", "■"],
                              ["■", "H", " ", "H", "■", "H", " ", "H",
                               "H", "H", "H", "H", "H", "H", "H", "■"],
                              ["■", "H", " ", "H", "■", "H", " ", " ",
                               " ", " ", " ", " ", " ", "H", "H", "■"],
                              ["■", "H", " ", "H", "■", "H", " ", "■",
                               "■", "■", "■", " ", " ", "H", "H", "■"],
                              ["■", "H", " ", "H", "H", "H", " ", "■",
                               "L", "L", "■", " ", " ", "H", "H", "■"],
                              ["■", "H", " ", " ", " ", " ", " ", "■",
                               "■", "■", "■", "■", " ", "H", "H", "■"],
                              ["■", "H", "H", "H", "H", "H", " ", " ",
                               " ", " ", " ", " ", " ", " ", "H", "■"],
                              ["■", "■", "■", "■", "■", "■", "H", "H",
                               "H", "H", "H", "H", "H", " ", "H", "■"],
                              ["■", "H", "H", "H", "H", "■", "■", "■",
                               "H", "H", "H", "H", "H", " ", "H", "■"],
                              ["■", "H", "H", "H", "H", "■", "H", "H",
                               "H", "H", "H", " ", " ", " ", "H", "■"],
                              ["■", " ", " ", "■", "H", "■", "H", "H",
                               "H", "H", "H", " ", "H", "H", "H", "■"],
                              ["■", " ", " ", "■", "H", "H", " ", " ",
                               " ", " ", " ", " ", "H", "H", "H", "■"],
                              ["■", " ", " ", "■", "H", "H", " ", " ",
                               "H", "H", "H", "H", "H", "H", "H", "■"],
                              ["■", "C", "C", "■", "■", "■", "■", "■", "■", "■", "■", "■", "■", "■", "■", "■"]]

                map_desert = [["■", "■", "■", "■", "■", "■", "■", "■", "■", "■", "■", "■", "■", "■", "■", "■"],
                              ["■", "H", "H", " ", " ", " ", "H", "H",
                                    "H", "H", "H", " ", " ", " ", "D", "■"],
                              ["■", "H", "H", " ", " ", " ", "H", "H",
                                  "H", "H", "H", "■", "■", " ", " ", "■"],
                              ["■", "H", "H", " ", " ", " ", " ", " ",
                                  " ", " ", " ", "■", "■", " ", " ", "■"],
                              ["■", "H", "H", "■", "■", "H", "H", " ",
                               " ", " ", " ", " ", " ", "H", "H", "■"],
                              ["■", "H", "H", "■", "■", "H", "H", " ",
                               "H", "H", " ", " ", " ", "H", "H", "■"],
                              ["V", " ", " ", "■", "■", "H", "H", " ",
                               "H", "H", " ", " ", " ", "H", "H", "■"],
                              ["V", " ", " ", "■", "■", "H", "H", " ",
                               "H", "H", " ", " ", " ", "H", "H", "■"],
                              ["V", " ", " ", "H", "H", "H", "H", " ",
                               " ", " ", "■", "■", "■", " ", " ", "■"],
                              ["■", " ", " ", " ", " ", " ", " ", " ",
                               " ", "D", "■", "■", "■", " ", " ", "■"],
                              ["■", " ", " ", " ", " ", " ", " ", " ",
                               " ", " ", "■", "■", "■", " ", " ", "■"],
                              ["■", "H", "H", "H", " ", " ", "■", "■",
                               " ", " ", " ", " ", " ", "■", "■", "■"],
                              ["■", "H", "H", "H", " ", " ", "■", "■",
                               " ", "H", "H", "H", "H", "H", "H", "■"],
                              ["■", "H", "H", "■", " ", " ", " ", " ",
                               " ", "H", "H", "H", "H", "■", " ", "■"],
                              ["■", "H", "H", "■", "D", " ", " ", " ",
                               " ", "H", "H", "H", "H", "■", " ", "G"],
                              ["■", "■", "■", "■", "■", "■", "■", "■", "■", "■", "■", "■", "■", "■", "■", "■"]]

                map_grotte = [["■", "■", "■", "■", "■", "■", "■", "■", "■", "■", "■", "■", "■", "■", "■", "■"],
                              ["■", "H", "D", "■", "■", "H", "H", "H",
                                    " ", " ", " ", "H", "H", "H", "H", "■"],
                              ["■", "H", "H", "■", "H", "H", "H", "H",
                                  " ", " ", " ", "H", "H", "H", "H", "■"],
                              ["■", "H", "H", "■", "H", "H", "H", "■",
                                  "■", "■", "■", "■", "H", "H", "H", "■"],
                              ["■", "H", "H", "H", "H", "H", "H", "■",
                               "H", "H", "H", "■", "■", "■", "H", "■"],
                              ["■", " ", " ", "■", " ", " ", " ", "■",
                               "H", "H", "H", " ", " ", " ", " ", "■"],
                              ["■", " ", " ", "■", " ", " ", " ", "■",
                               "H", "H", "H", "■", "■", " ", " ", "■"],
                              ["■", " ", " ", "■", "H", "H", "H", "■",
                               "■", " ", " ", "■", "■", " ", " ", "■"],
                              ["■", "H", "H", "■", "■", "H", "H", "H",
                               "■", " ", "D", "■", "■", "H", "H", "■"],
                              ["■", "H", "H", "H", "■", "H", "H", "H",
                               "■", " ", " ", "■", "■", "H", "H", "■"],
                              ["■", "H", "H", "H", "H", "H", "H", "H",
                               "■", " ", " ", " ", " ", " ", " ", "■"],
                              ["■", "H", "■", "■", "■", " ", "■", "■",
                               "■", "H", "H", "■", "H", "H", "H", "■"],
                              ["■", "H", "■", "H", "H", " ", " ", " ",
                               " ", "H", "H", "■", "■", "■", "H", "■"],
                              ["■", " ", "■", "H", "H", " ", " ", " ",
                               " ", " ", "H", "H", "H", "■", " ", "■"],
                              ["D", " ", "■", "H", "H", " ", " ", " ",
                               " ", " ", "H", "H", "H", " ", "D", "■"],
                              ["■", "■", "■", "■", "■", "■", "■", "■", "■", "■", "■", "■", "■", "■", "■", "■"]]

                map_foret_2 = [["■", "■", "■", "■", "■", "■", "■", "M", "M", "■", "■", "■", "■", "■", "■", "■"],
                               ["■", "H", "D", "H", "H", "■", " ", " ",
                                " ", "■", "H", "H", "H", " ", "D", "■"],
                               ["■", "H", "H", "H", "H", "H", " ", " ",
                                   " ", "H", "H", "H", "H", " ", " ", "■"],
                               ["■", "H", "H", "H", "H", "H", " ", " ",
                                   " ", "■", "■", "■", "■", "■", "■", "■"],
                               ["■", "H", "H", "H", "H", "H", " ", " ",
                                " ", " ", " ", " ", " ", " ", " ", "■"],
                               ["■", "H", "H", "H", "H", "■", "■", "■",
                                "■", "■", "■", "■", "■", "H", "H", "■"],
                               ["■", "■", "■", "■", "■", "■", "■", "■",
                                "■", "■", "H", "H", "H", "H", "H", "■"],
                               ["■", "D", " ", " ", "H", "H", "H", "H",
                                "■", "■", "H", "H", "H", "H", "H", "■"],
                               ["■", " ", " ", " ", "■", "H", "H", "H",
                                "H", "■", "H", "H", "H", "H", "H", "■"],
                               ["■", " ", " ", " ", "■", "■", "H", "H",
                                "H", "■", "H", "H", "H", "H", "H", "■"],
                               ["■", " ", " ", " ", " ", "■", "H", "H",
                                "H", " ", " ", " ", " ", " ", " ", "■"],
                               ["■", "■", "H", "H", "■", "■", "■", "■",
                                "H", " ", " ", " ", " ", " ", " ", "■"],
                               ["■", "H", "H", "H", "H", "H", "■", "■",
                                "■", "■", "H", "H", "H", "H", "H", "■"],
                               ["■", "H", "H", "H", "H", "H", " ", " ",
                                " ", "■", "H", "H", "H", "H", "H", "■"],
                               ["■", "H", "H", "H", "H", "H", "■", " ",
                                " ", "■", "H", "H", "H", "H", "H", "■"],
                               ["■", "■", "■", "■", "■", "■", "■", "V", "V", "■", "■", "■", "■", "■", "■", "■"]]

                map_montagne = [["■", "■", "P", "■", "■", "■", "■", "■", "■", "■", "■", "■", "■", "■", "■", "■"],
                                ["■", " ", " ", " ", "■", "■", " ", " ",
                                    " ", " ", " ", " ", " ", " ", " ", "■"],
                                ["■", " ", " ", " ", "■", "■", " ", " ",
                                    " ", "■", "■", "■", "■", "H", "H", "■"],
                                ["■", "H", "H", "H", "■", "■", "D", " ",
                                    " ", "■", "■", "■", "■", "H", "H", "■"],
                                ["■", "H", "H", "H", "H", "H", " ", " ",
                                 " ", "H", "H", "■", "■", "H", "H", "■"],
                                ["■", "H", "H", "H", "H", "H", " ", " ",
                                 " ", "H", "H", "■", "■", "H", "H", "■"],
                                ["■", "■", "■", "■", "H", "H", " ", " ",
                                 " ", "H", "H", "■", "■", "H", "D", "■"],
                                ["■", "■", "■", "■", " ", " ", "■", "■",
                                 " ", "H", "H", "■", "■", "■", "■", "■"],
                                ["■", "■", "■", "■", " ", " ", "■", "■",
                                 " ", "H", "H", "■", "■", "■", "■", "■"],
                                ["■", "H", "H", "H", " ", "D", "■", "■",
                                 " ", " ", " ", " ", " ", "H", "H", "■"],
                                ["■", "H", "H", "H", " ", " ", " ", " ",
                                 " ", " ", " ", " ", " ", "H", "H", "■"],
                                ["■", "■", "■", "H", "■", "■", "■", "■",
                                 "■", "■", "■", "■", "■", "H", "■", "■"],
                                ["■", "H", "H", "H", "■", "■", " ", " ",
                                 " ", " ", "■", "■", "■", "H", "H", "■"],
                                ["■", "H", "H", "■", "■", " ", " ", " ",
                                 " ", " ", " ", "H", "H", "H", "H", "■"],
                                ["■", "H", "H", "H", "H", " ", " ", " ",
                                 " ", " ", " ", "■", "■", "H", "H", "■"],
                                ["■", "■", "■", "■", "■", "■", "■", "F", "F", "■", "■", "■", "■", "■", "■", "■"]]

                map_pic = [["■", "■", "■", "■", "■", "■", "■", "■", "■", "■", "■", "■", "■", "■", "■", "■"],
                           ["■", "H", "H", "H", "■", " ", " ", "■",
                            "■", "■", "■", "A", "■", "■", "■", "■"],
                           ["■", "H", "■", " ", "■", " ", " ", "■",
                               "H", "H", "H", " ", "■", " ", " ", "R"],
                           ["■", "H", "■", "S", "■", " ", "H", "H",
                               "H", "■", "■", "■", "■", "H", "■", "■"],
                           ["■", "H", "■", "■", "■", "■", "H", "H",
                            "H", "■", " ", " ", "■", "H", "H", "■"],
                           ["■", " ", " ", " ", " ", "■", "H", "H",
                            "■", "■", " ", " ", "■", "■", "H", "■"],
                           ["■", " ", " ", " ", " ", "■", "H", "H",
                            "H", " ", " ", " ", "■", "H", "H", "■"],
                           ["■", " ", " ", " ", " ", "■", "H", "H",
                            "H", " ", " ", " ", "■", "H", "■", "■"],
                           ["■", "H", "H", "■", "■", "■", "■", "■",
                            "■", " ", " ", " ", "■", "H", "H", "■"],
                           ["■", "H", "H", "H", "H", "H", " ", "E",
                            "■", " ", " ", " ", "■", "■", "H", "■"],
                           ["■", "H", "H", "H", "H", "■", "■", "■",
                            "■", "H", "H", "H", "■", "H", "H", "■"],
                           ["■", "H", "H", "H", "■", "■", " ", " ",
                            " ", "H", "H", "H", "■", "H", "■", "■"],
                           ["■", " ", " ", " ", "H", "H", " ", " ",
                            " ", "H", "H", "H", "■", "H", "H", "■"],
                           ["■", " ", " ", " ", "■", "■", "■", " ",
                            " ", " ", " ", " ", "■", "■", "H", "■"],
                           ["■", " ", " ", " ", "■", "■", "■", "■",
                            " ", " ", " ", " ", "H", "H", "H", "■"],
                           ["■", "■", "M", "■", "■", "■", "■", "■", "■", "■", "■", "■", "■", "■", "■", "■"]]

                map_egout = [["■", "■", "■", "■", "■", "■", "■"],
                             ["■", "D", " ", " ", " ", " ", "■"],
                             ["■", " ", " ", "■", "H", "H", "■"],
                             ["■", "■", "■", "■", "H", "H", "■"],
                             ["■", "H", "H", "H", "H", "H", "■"],
                             ["■", "H", "H", "H", "H", "H", "■"],
                             ["■", "H", "H", "■", "■", "■", "■"],
                             ["■", "H", "H", "H", " ", " ", "■"],
                             ["■", " ", " ", "■", " ", " ", "■"],
                             ["■", " ", " ", "■", " ", "V", "■"],
                             ["■", "■", "■", "■", "■", "■", "■"]]

                map_red = [["■", "■", "■", "■", "■", "■", "■", "■", "■", "■", "■", "■", "■", "■", "■", "■", "■", "■", "■", "■", "■", "■", "■", "■", "■", "■", "■", "■", "■", "■", "■", "■", "■"],
                           ["■", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ",
                               " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "R", " ", "■"],
                           ["P", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ",
                               " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "E", " ", "■"],
                           ["■", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ",
                            " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "D", " ", "■"],
                           ["■", "■", "■", "■", "■", "■", "■", "■", "■", "■", "■", "■", "■", "■", "■", "■", "■", "■", "■", "■", "■", "■", "■", "■", "■", "■", "■", "■", "■", "■", "■", "■", "■"]]

                qg_racket = [["■", "■", "■", "■", "■", "■", "■"],
                             ["■", " ", " ", " ", " ", " ", "■"],
                             ["■", " ", " ", " ", " ", " ", "■"],
                             ["■", " ", " ", " ", " ", " ", "■"],
                             ["V", " ", " ", " ", " ", "M", "■"],
                             ["V", " ", " ", " ", " ", " ", "■"],
                             ["V", " ", " ", " ", " ", "E", "■"],
                             ["■", " ", " ", " ", " ", " ", "■"],
                             ["■", " ", " ", " ", " ", " ", "■"],
                             ["■", " ", " ", "L", " ", " ", "■"],
                             ["■", "■", "■", "■", "■", "■", "■"],
                             ]

                X = 7
                Y = 7

                map = map_ville

                state_spawn_pkmn = 0  # valeur qui sauvegarde l'état de la case où nous sommes si c'est un buisson ou un endroit où un Pokémon peut apparaître
                fight = 0  # valeur qui permet de ne pas d'autre combat en changeant de case buisson

                let_game = map_fonction(zone, niveau_joueur, stats_vie_joueur, stats_vie_total_joueur, stats_attaque_joueur, stats_defense_joueur, attaque1, effet1, attaque2, effet2, stats_vie_ennemi, stats_attaque_ennemi, stats_defense_ennemi, nom_ennemi, niveau_ennemi,
                                        attaque_ennemi_1, attaque_ennemi_2, effet_attaque_ennemi1, effet_attaque_ennemi2, xp_joueur, xp_prochain_niveau, xp_ennemi, cooldown, cooldown_ennemi, map, X, Y, map_ville, map_foret, state_spawn_pkmn, fight, ListPokemonInBag, bank_account, list_item)
                print(let_game)

        elif choice == choice_game_list[2]:
            set = setting()
            print(set)

        # option load game : la partie précédement sauvegardée se lance.
        elif choice == choice_game_list[1]:

            pickle_in = open("name.pickle", "rb")
            name = pickle.load(pickle_in)
            print("Te revoila {}, nous allons te renvoyer dans le jeu !".format(name))
            input("\n press x")
            clear = system('cls')

            zone_in = open("zone_save.pickle", "rb")
            zone = pickle.load(zone_in)

            niveau_joueur_in = open("niveau_joueur_save.pickle", "rb")
            niveau_joueur = pickle.load(niveau_joueur_in)

            stats_vie_joueur_in = open("stats_vie_joueur_save.pickle", "rb")
            stats_vie_joueur = pickle.load(stats_vie_joueur_in)

            stats_vie_total_joueur_in = open(
                "stats_vie_total_joueur_save.pickle", "rb")
            stats_vie_total_joueur = pickle.load(stats_vie_total_joueur_in)

            stats_attaque_joueur_in = open(
                "stats_attaque_joueur_save.pickle", "rb")
            stats_attaque_joueur = pickle.load(stats_attaque_joueur_in)

            stats_defense_joueur_in = open(
                "stats_defense_joueur_save.pickle", "rb")
            stats_defense_joueur = pickle.load(stats_defense_joueur_in)

            attaque1_in = open("attaque1_save.pickle", "rb")
            attaque1 = pickle.load(attaque1_in)

            effet1_in = open("effet1_save.pickle", "rb")
            effet1 = pickle.load(effet1_in)

            attaque2_in = open("attaque2_save.pickle", "rb")
            attaque2 = pickle.load(attaque2_in)

            effet2_in = open("effet2_save.pickle", "rb")
            effet2 = pickle.load(effet2_in)

            xp_joueur_in = open("xp_joueur_save.pickle", "rb")
            xp_joueur = pickle.load(xp_joueur_in)

            xp_prochain_niveau_in = open(
                "xp_prochain_niveau_save.pickle", "rb")
            xp_prochain_niveau = pickle.load(xp_prochain_niveau_in)

            cooldown_in = open("cooldown_save.pickle", "rb")
            cooldown = pickle.load(cooldown_in)

            map_in = open("map_save.pickle", "rb")
            map = pickle.load(map_in)

            X_in = open("X_save.pickle", "rb")
            X = pickle.load(X_in)

            Y_in = open("Y_save.pickle", "rb")
            Y = pickle.load(Y_in)

            map_ville_in = open("map_ville_save.pickle", "rb")
            map_ville = pickle.load(map_ville_in)

            map_foret_in = open("map_foret_save.pickle", "rb")
            map_foret = pickle.load(map_foret_in)

            state_spawn_pkmn_in = open("state_spawn_pkmn_save.pickle", "rb")
            state_spawn_pkmn = pickle.load(state_spawn_pkmn_in)

            fight_in = open("fight_save.pickle", "rb")
            fight = pickle.load(fight_in)

            ListPokemonInBag_in = open("ListPokemonInBag_save.pickle", "rb")
            ListPokemonInBag = pickle.load(ListPokemonInBag_in)

            bank_account_in = open("bank_account_save.pickle", "rb")
            bank_account = pickle.load(bank_account_in)

            list_item_in = open("list_item_save.pickle", "rb")
            list_item = pickle.load(list_item_in)

            stats_vie_ennemi_in = open("stats_vie-ennemi_save.pickle", "rb")
            stats_vie_ennemi = pickle.load(stats_vie_ennemi_in)

            stats_attaque_ennemi_in = open(
                "stats_attaque_ennemi_save.pickle", "rb")
            stats_attaque_ennemi = pickle.load(stats_attaque_ennemi_in)

            stats_defense_ennemi_in = open(
                "stats_defense_ennemi_save.pickle", "rb")
            stats_defense_ennemi = pickle.load(stats_defense_ennemi_in)

            nom_ennemi_in = open("nom_ennemi_save.pickle", "rb")
            nom_ennemi = pickle.load(nom_ennemi_in)

            niveau_ennemi_in = open("niveau_ennemi_save.pickle", "rb")
            niveau_ennemi = pickle.load(niveau_ennemi_in)

            attaque_ennemi_1_in = open("attaque_ennemi_1_save.pickle", "rb")
            attaque_ennemi_1 = pickle.load(attaque_ennemi_1_in)

            attaque_ennemi_2_in = open("attaque_ennemi_2_save.pickle", "rb")
            attaque_ennemi_2 = pickle.load(attaque_ennemi_2_in)

            effet_attaque_ennemi1_in = open(
                "effet_attaque_ennemi1_save.pickle", "rb")
            effet_attaque_ennemi1 = pickle.load(effet_attaque_ennemi1_in)

            effet_attaque_ennemi2_in = open(
                "effet_attaque_ennemi2_save.pickle", "rb")
            effet_attaque_ennemi2 = pickle.load(effet_attaque_ennemi2_in)

            xp_ennemi_in = open("xp_ennemi_save.pickle", "rb")
            xp_ennemi = pickle.load(xp_ennemi_in)

            cooldown_ennemi_in = open("cooldown_ennemi_save.pickle", "rb")
            cooldown_ennemi = pickle.load(cooldown_ennemi_in)

            let_game1 = map_fonction(zone, niveau_joueur, stats_vie_joueur, stats_vie_total_joueur, stats_attaque_joueur, stats_defense_joueur, attaque1, effet1, attaque2, effet2, stats_vie_ennemi, stats_attaque_ennemi, stats_defense_ennemi, nom_ennemi, niveau_ennemi,
                                     attaque_ennemi_1, attaque_ennemi_2, effet_attaque_ennemi1, effet_attaque_ennemi2, xp_joueur, xp_prochain_niveau, xp_ennemi, cooldown, cooldown_ennemi, map, X, Y, map_ville, map_foret, state_spawn_pkmn, fight, ListPokemonInBag, bank_account, list_item)

            print(let_game1)

        elif choice == choice_game_list[3]:
            return delay_print("Au revoir mon ami")

        elif choice != choice_game_list[:]:
            delay_print("Séléctionner une autre option.")
            print()
            input(delay_print("\n"" <  Appuyez sur Entrée pour Quitter >"))
            clear = system('cls')
        i = i + 1


Start = let()
print(Start)