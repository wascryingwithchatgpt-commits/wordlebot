import requests
import datetime

WEBHOOK_URL = "PASTE_WEBHOOK_HERE"

today = datetime.date.today()

url = f"https://www.nytimes.com/svc/wordle/v2/{today:%Y-%m-%d}.json"

data = requests.get(url).json()

answer = data["solution"]

message = {
    "content": f"Today's Wordle answer is: **{answer}**"
}

requests.post(WEBHOOK_URL, json=message)
