import requests
import smtplib
from email.message import EmailMessage
import os
from dotenv import load_dotenv

load_dotenv()

SENDER = os.getenv('YOUR_EMAIL')
PASSWORD = os.getenv('EMAIL_PASSWORD')
EMAIL_SMTP = os.getenv('EMAIL_SMTP')
RECEIVER_EMAIL = os.getenv('RECEIVER_EMAIL')


class Game:
    def __init__(self):
        self.game_id = None

    def get_game_info(self, game_id):
        self.game_id = game_id
        params = {
            "appids": self.game_id,
            "cc": "brl"
        }

        response = requests.get(url="http://store.steampowered.com/api/appdetails/", params=params)
        game_data = response.json()[str(self.game_id)]["data"]
        game_price = game_data["price_overview"]

        if game_price["discount_percent"] != 0:
            game_info = f"O jogo \"{game_data['name']}\" está com " \
                        f"{game_price['discount_percent']}% de desconto!\n" \
                        f"Preço Inicial: {game_price['initial_formatted']}\n" \
                        f"Preço com desconto: {game_price['final_formatted']}\n\n"

            return game_info
        else:
            return ""

    def get_games_info(self, sheet_data):
        final_msg = ""
        for game in sheet_data:
            final_msg += self.get_game_info(game["gameId"])

        if final_msg != "":
            with smtplib.SMTP("smtp-mail.outlook.com") as connection:
                connection.starttls()
                connection.login(user=SENDER, password=PASSWORD)

                msg = EmailMessage()
                msg.set_content(final_msg)
                msg["Subject"] = "Jogos em promoção!"
                msg["From"] = SENDER
                msg["To"] = RECEIVER_EMAIL

                connection.send_message(msg)
