from datetime import datetime
import random

messages = [
    "Daily learning update",
    "Worked on improving skills",
    "Consistency matters",
    "Learning something new today",
    "Small progress every day"
]

with open("daily_log.txt", "a") as f:
    f.write(f"{datetime.now()} - {random.choice(messages)}\n")
