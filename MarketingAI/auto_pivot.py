def analyze_performance(posts):
    high = [p for p in posts if p["likes"] > 50]
    low = [p for p in posts if p["likes"] <= 50]
    return high, low


def improve_strategy(high, low):
    return {
        "insights": "Posts with emojis perform better",
        "suggestions": "Use more engaging hooks and emojis"
    }