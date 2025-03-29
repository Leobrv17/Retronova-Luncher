import requests
import os

class ApiClient:
    def __init__(self):
        self.base_url = os.getenv("API_URL")

    def get_machine_games(self, machine_id):
        url = f"{self.base_url}/arcade_machines/{machine_id}/games"
        headers = {'accept': 'application/json'}
        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()  # Lève une exception en cas de code erreur (4xx, 5xx)
            return response.json()  # Retourne la réponse sous forme de dictionnaire
        except requests.exceptions.RequestException as e:
            print(f"Erreur lors de la requête : {e}")
            return None