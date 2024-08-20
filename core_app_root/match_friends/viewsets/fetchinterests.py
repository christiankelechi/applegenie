import json

def fetch_human_interests(file_path):
    with open(file_path, 'r') as f:
        data = json.load(f)
    interests = []
    for i in range(1, 23+1):
        key = str(i)  # keys in the JSON are strings
        if key in data:
            interests.append(data[key])
    return interests



