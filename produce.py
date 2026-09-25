import json
import time

with open("queue.json", "r", encoding="utf-8") as f:
    queue = json.load(f)

print("OFFLINE PRODUCTION QUEUE STARTED")

for job in queue["jobs"]:
    print("Producing:", job)
    time.sleep(1)

print("All jobs finished.")
