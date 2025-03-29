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

def launch_game(game_name, screen, nb_players):
    """ Fonction pour lancer un jeu donné en fonction du nom du jeu """

    if nb_players == 1:
        twoPlayers = False
    else:
        twoPlayers = True

    try:
        game_module = importlib.import_module(f"games.{game_name}.main")  # Importer le jeu (ex. 'games.game1.main')
    except ModuleNotFoundError:
        print(f"Erreur : Le module pour {game_name} n'a pas été trouvé.")
        return 0, 0, 0

    # Lancer la fonction main du jeu en passant le Screen
    score_p1, score_p2, total_score = game_module.main(screen,twoPlayers)

    return score_p1, score_p2, total_score

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
                    score_p1, score_p2, total_score = launch_game("game1", screen.screen,1)
                    screen_running = False  # Quitter le menu après avoir joué

                if event.key == pygame.K_2:  # Si l'utilisateur appuie sur "2"
                    score_p1, score_p2, total_score = launch_game("game2", screen.screen,2)
                    screen_running = False  # Quitter le menu après avoir joué

        time.sleep(0.1)
