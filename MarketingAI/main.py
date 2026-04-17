from tone_analyzer import analyze_tone
from content_generator import generate_content
from auto_pivot import analyze_performance, improve_strategy

# Step 1: Tone Learning
posts = [
    "AI is changing everything 🚀",
    "Build fast. Fail faster.",
    "We just launched something BIG 👀"
]

tone = analyze_tone(posts)
print("TONE:\n", tone)

# Step 2: Content Generation
content = generate_content(tone, "AI marketing tools", "Twitter")
print("\nGENERATED CONTENT:\n", content)

# Step 3: Fake Engagement Data (for demo)
posts_data = [
    {"content": "Post 1", "likes": 100},
    {"content": "Post 2", "likes": 20}
]

high, low = analyze_performance(posts_data)

# Step 4: Improvement Strategy
strategy = improve_strategy(high, low)
print("\nIMPROVEMENT STRATEGY:\n", strategy)