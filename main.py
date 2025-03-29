import os
import pygame
import time
from my_lib.qr_code import QrCode
from my_lib.sound import Sound
from my_lib.screen import Screen
from my_lib.api import ApiClient
from dotenv import load_dotenv


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
        time.sleep(0.1)
