import requests
import datetime

WEBHOOK_URL = "https://discordapp.com/api/webhooks/1502328479167938660/jZFidBzl81eZU7ZltZECHSKZAOEkZnABM8uizdSsE5C16ZhLPp01KwKuEOu6G4H0caP1"

today = datetime.date.today()

url = f"https://www.nytimes.com/svc/wordle/v2/{today:%Y-%m-%d}.json"

data = requests.get(url).json()

answer = data["solution"]

message = {
    "content": f"Today's Wordle answer is: **{answer}**"
}

requests.post(WEBHOOK_URL, json=message)
