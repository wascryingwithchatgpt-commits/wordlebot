import os
import requests
import datetime

WEBHOOK_URL = os.getenv("WEBHOOK_URL")

today = datetime.date.today()

# Wordle started on 2021-06-19
start_date = datetime.date(2021, 6, 19)

wordle_number = (today - start_date).days + 1

url = f"https://www.nytimes.com/svc/wordle/v2/{today:%Y-%m-%d}.json"
data = requests.get(url).json()

answer = data["solution"]

message = {
    "content": f"Today's Wordle #{wordle_number} answer is: {answer}"
}

requests.post(WEBHOOK_URL, json=message)
