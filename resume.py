import json

with open("./resume.json") as f:
    resume = json.load(f)

print(resume)
