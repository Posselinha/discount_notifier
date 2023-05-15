import requests
from game import Game
import os
from dotenv import load_dotenv

load_dotenv()

sheet_username = os.getenv('USERNAME_AUTH')
sheet_password = os.getenv('PASSWORD_AUTH')
SHEETY_ENDPOINT = os.getenv('SHEETY_ENDPOINT')

response = requests.get(url=SHEETY_ENDPOINT, auth=(sheet_username, sheet_password))
sheet_data = response.json()["games"]

games = Game()
games.get_games_info(sheet_data)
