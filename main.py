import os
import requests
import datetime

WEBHOOK_URL = os.getenv("WEBHOOK_URL")

today = datetime.date.today()

url = f"https://www.nytimes.com/svc/wordle/v2/{today:%Y-%m-%d}.json"
data = requests.get(url).json()

print("DEBUG API RESPONSE:", data)  # important

wordle_number = data["id"]
answer = data["solution"]

message = {
    "content": f"Today's Wordle #{wordle_number} answer is: {answer}"
}

requests.post(WEBHOOK_URL, json=message)
