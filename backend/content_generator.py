def generate_content(tone, topic, platform):
    """
Generate simple AI-style content based on tone and topic.
    """

    if tone == "positive":
        return [ 
        f"🔥 {topic} is changing the game!",
        f"💡 Here's why {topic} matters more than ever.",
        f"🚀 Level up your strategy with {topic}."
    ]

    elif tone == "negative":
        return [
        f"⚠️ Common mistakes people make with {topic}.",
        f"❌ Why {topic} often fails (and how to fix it).",
        f"🛑 Stop doing this if you're using {topic}."
    ]

    else:
        return [
        f"📊 Let's talk about {topic}.",
        f"🤔 What you should know about {topic}.",
        f"📢 Insights on {topic} you can't ignore."
    ]
