import os
import pygame
import time
from my_lib.qr_code import QrCode
from my_lib.sound import Sound
from my_lib.screen import Screen
from my_lib.api import ApiClient
from dotenv import load_dotenv
import importlib
import sys

sys.path.append(os.path.dirname(os.path.abspath(__file__)))


def launch_game(game_name, window, twoPlayer):
    # Déterminez le chemin du dossier du jeu (par exemple game1 ou game2)
    game_path = os.path.abspath(f"./games/{game_name}")

    # Ajoutez ce dossier au sys.path pour pouvoir importer les fichiers de ce jeu
    sys.path.insert(0, game_path)

    try:
        # Importez les modules nécessaires à partir du jeu
        # Assurez-vous que les fichiers nécessaires sont bien présents dans le dossier du jeu
        game_module = importlib.import_module("main")  # Import du main.py de chaque jeu

        # Exécutez la logique du jeu
        score_p1, score_p2, = game_module.main(window, twoPlayer)  # Remplacez par la fonction principale du jeu
    except ModuleNotFoundError:
        print(f"Erreur : Le module pour {game_name} n'a pas été trouvé.")
    finally:
        # Retirer le chemin ajouté à sys.path après utilisation
        sys.path.pop(0)
        return score_p1, score_p2, score_p1 + score_p2

    return score_p1, score_p2, score_p1 + score_p2


if __name__ == "__main__":
    load_dotenv()
    pygame.init()
    music = Sound()

    machine_id = os.getenv("ID_BORNE")

    screen = Screen()
    qrCode = QrCode()
    apiclient = ApiClient()

    background_image = pygame.image.load("./assets/img.png").convert()

    music.load_music("./sounds/menuMusic.mp3")
    music.play_music()

    while screen.running:
        machine_data = apiclient.get_machine_games(machine_id)
        screen.screen.blit(background_image, (0, 0))
        screen.display_machine_info(machine_data)
        qrCode.run(screen.screen)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                screen_running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:  # Si l'utilisateur appuie sur "1"
                    score_p1, score_p2, total_score = launch_game("game1", screen.screen, 1)
                    print(score_p1, score_p2,total_score)
                    screen_running = False  # Quitter le menu après avoir joué

                if event.key == pygame.K_2:  # Si l'utilisateur appuie sur "2"
                    score_p1, score_p2, total_score = launch_game("game2", screen.screen, 2)
                    screen_running = False  # Quitter le menu après avoir joué

        time.sleep(1)
