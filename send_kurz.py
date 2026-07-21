import os
import requests

TOKEN = os.environ["BOT_TOKEN"]
CHAT_ID = os.environ["CHAT_ID"]

url = "https://api.frankfurter.app/latest?from=EUR&to=CZK"

response = requests.get(url)

if response.status_code == 200:
    kurz = response.json()["rates"]["CZK"]

    text = f"""💶 Aktuální kurz

1 EUR = {kurz} CZK
"""

    requests.post(
        f"https://api.telegram.org/bot{TOKEN}/sendMessage",
        json={
            "chat_id": CHAT_ID,
            "text": text
        }
    )
