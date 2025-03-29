import pygame


class Screen():
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Retronova Luncher")

        self.screen = pygame.display.set_mode((1920, 1080), pygame.FULLSCREEN)
        self.running = True

    def draw_text(self, text, x, y, size=50, color=(255, 255, 255)):
        """ Affiche du texte sur l'écran """
        font = pygame.font.Font(None, size)
        text_surface = font.render(text, True, color)
        self.screen.blit(text_surface, (x, y))

    def display_machine_info(self, machine_data):
        """ Affiche les informations de la machine (jeux) """
        if machine_data:
            # Affichage du nom de la machine
            self.draw_text(f"{machine_data.get('name', 'Nom non défini')}", 140, 230, 100, (255, 0, 255))

            # Affichage des jeux
            game1 = machine_data.get('game1', 'Aucun jeu')
            game2 = machine_data.get('game2', 'Aucun jeu')
            self.draw_text(f"Jeu 1: {game1}", 600, 700, 100, (255, 0, 255))
            self.draw_text(f"Jeu 2: {game2}", 600, 800, 100, (255, 0, 255))
        else:
            # Affichage d'un message d'erreur si les données sont indisponibles
            self.draw_text("Erreur de récupération des données de la machine.", 100, 100, 50, (255, 0, 0))