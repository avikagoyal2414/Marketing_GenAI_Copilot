# Fix import path so backend can access your AI files
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from fastapi import FastAPI
from pydantic import BaseModel

# Import YOUR AI modules
from tone_analyzer import analyze_tone
from content_generator import generate_content
from auto_pivot import analyze_performance, improve_strategy

# Import backend helpers
from backend.telegram_bot import send_telegram_message
from backend.database import save_post, get_posts

app = FastAPI()

# -------------------------------
# Request Model
# -------------------------------
class CampaignRequest(BaseModel):
    topic: str
    platform: str


# -------------------------------
# Generate Content (USES YOUR AI)
# -------------------------------
@app.post("/generate")
def generate_campaign(data: CampaignRequest):

    # Sample past posts (can be dynamic later)
    posts = [
        "We build fast 🚀",
        "AI is the future",
        "Launch smarter, not harder"
    ]

    # 🧠 Step 1: Tone Learning (YOUR CODE)
    tone = analyze_tone(posts)

    # ✍️ Step 2: Content Generation (YOUR CODE)
    content = generate_content(tone, data.topic, data.platform)

    return {
        "tone": tone,
        "content": content
    }


# -------------------------------
# Post to Telegram
# -------------------------------
@app.post("/post")
def post_content(message: str):

    # Send message to Telegram
    send_telegram_message(message)

    # Save post with fake engagement
    save_post(message)

    return {"status": "Posted successfully ✅"}


# -------------------------------
# Analytics + Auto-Pivot (YOUR AI)
# -------------------------------
@app.get("/analytics")
def analytics():

    posts = get_posts()

    if not posts:
        return {"message": "No data yet"}

    # 📊 Step 3: Performance Analysis (YOUR CODE)
    high, low = analyze_performance(posts)

    # 🔥 Step 4: Improvement Strategy (YOUR CODE)
    strategy = improve_strategy(high, low)

    return {
        "posts": posts,
        "high_performing": high,
        "low_performing": low,
        "strategy": strategy
    }