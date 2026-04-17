from fastapi import FastAPI
from engagement_analyzer import analyze_engagement
from tone_analyzer import analyze_tone
from content_generator import generate_content
from auto_pivot import analyse_performance, improve_strategy
import json

app = FastAPI()

# -------------------------
# Health Check Route
# -------------------------
@app.get("/improve")
def improve_content():
    try:
        with open("engagement_data.json", "r") as f:
            data = json.load(f)
    except:
        return {"message": "No data available"}

    high, low = analyse_performance(data)
    strategy = improve_strategy(high, low)

    return {
        "high_performing": high,
        "low_performing": low,
        "strategy": strategy
    }

# -------------------------
# AI CONTENT GENERATION
# -------------------------
@app.post("/generate")
def generate(data: dict):
    try:
        posts = data.get("posts", [])
        topic = data.get("topic", "")
        platform = data.get("platform", "")

        # Step 1: Analyze tone from past posts
        tone = analyze_tone(posts)

        # Step 2: Generate content using tone + topic
        content = generate_content(tone, topic, platform)

        return {
            "status": "success",
            "tone": tone,
            "content": content
        }

    except Exception as e:
        return {
            "status": "error",
            "message": str(e)
        }


# -------------------------
# PERFORMANCE ANALYSIS (AUTO-PIVOT)
# -------------------------
@app.post("/improve")
def improve(data: dict):
    try:
        posts_data = data.get("posts_data", [])

        # Step 1: Split high/low performing posts
        high, low = analyse_performance(posts_data)

        # Step 2: Generate improvement strategy
        strategy = improve_strategy(high, low)

        return {
            "status": "success",
            "high_performing": high,
            "low_performing": low,
            "strategy": strategy
        }

    except Exception as e:
        return {
            "status": "error",
            "message": str(e)
        }