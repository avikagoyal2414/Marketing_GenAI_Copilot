def analyse_performance(posts_data):
    high_performing = []
    low_performing = []

    for post in posts_data:
        likes = post.get("reactions", 0)

        if likes >= 2:
            high_performing.append(post)
        else:
            low_performing.append(post)

    return high_performing, low_performing


def improve_strategy(high, low):
    if not high:
        return "No high-performing posts found. Try new styles."

    return {
        "insight": "Focus on content similar to high-performing posts.",
        "tip": "Use engaging hooks, strong keywords, consistency.",
        "high_examples": high[:2],
        "low_examples": low[:2]
    }