import json

DATA_FILE = "engagement_data.json"


def analyze_engagement():
    try:
        with open(DATA_FILE, "r") as f:
            data = json.load(f)
    except:
        return [], []

    high = []
    low = []

    for post in data:
        if post["reactions"] >= 2:
            high.append(post)
        else:
            low.append(post)

    return high, low