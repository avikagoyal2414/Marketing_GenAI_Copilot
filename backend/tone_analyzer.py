def analyze_tone(posts):
    """
Analyze tone of given posts and return a tone string.
    """

    if not posts:
        return "neutral"

    text = " ".join(posts).lower()

# Simple keyword-based tone detection
    positive_words = ["love", "great", "amazing", "awesome", "happy", "excited"]
    negative_words = ["bad", "hate", "terrible", "sad", "angry"]

    positive_score = sum(word in text for word in positive_words)
    negative_score = sum(word in text for word in negative_words)

def analyze_sentiment(positive_score, negative_score):
    if positive_score > negative_score:
        return "positive"
    elif negative_score > positive_score:
        return "negative"
    else:
        return "neutral"