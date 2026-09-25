import json

with open("queue.json", "r", encoding="utf-8") as f:
    queue = json.load(f)

print("Online Preparation Queue is ready!")
print("Batch:", queue["batch"])
print("Jobs:", len(queue["jobs"]))
