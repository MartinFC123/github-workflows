import requests

TOKEN = "..."
CHAT_ID = "..."

kurz = requests.get(
    "https://api.frankfurter.app/latest?from=EUR&to=CZK"
).json()["rates"]["CZK"]

requests.post(
    f"https://api.telegram.org/bot{TOKEN}/sendMessage",
    json={
        "chat_id": CHAT_ID,
        "text": f"1 EUR = {kurz} CZK"
    },
)