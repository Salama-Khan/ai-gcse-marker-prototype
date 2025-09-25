import json

with open("credentials.json", "r") as f:
    creds = json.load(f)

safe_string = json.dumps(creds).replace("\\", "\\\\").replace("\n", "\\n")
print(safe_string)
