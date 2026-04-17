import discord
import requests
import json
from datetime import datetime

intents = discord.Intents.all()
client = discord.Client(intents=intents)

# -------------------------
# EXISTING EVENT
# -------------------------
@client.event
async def on_ready():
    print(f"🤖 Logged in as {client.user}")


# -------------------------
# EXISTING EVENT
# -------------------------
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    # -------------------------
    # !gen COMMAND
    # -------------------------
    if message.content.startswith("!gen"):
        topic = message.content.replace("!gen ", "")

        payload = {
            "posts": ["AI is powerful"],
            "topic": topic,
            "platform": "Twitter"
        }

        try:
            # 🔹 Step 1: Generate content
            response = requests.post("http://127.0.0.1:8000/generate", json=payload)
            data = response.json()

            content = data.get("content", [])

            if isinstance(content, list):
                generated_text = "\n\n".join(content)
            else:
                generated_text = str(content)

            # 🔹 Step 2: Get improvement strategy
            improve_res = requests.get("http://127.0.0.1:8000/improve")
            improve_data = improve_res.json()

            strategy = improve_data.get("strategy", {})

            # 🔹 Step 3: Combine response
            final_reply = f"""
✨ Generated Content:

{generated_text}

📊 AI Improvement Tip:
💡 {strategy.get('tip')}
"""

            await message.channel.send(final_reply)

        except Exception as e:
            await message.channel.send(f"❌ Error: {str(e)}")

    # -------------------------
    # !improve COMMAND
    # -------------------------
    elif message.content.startswith("!improve"):
        response = requests.get("http://127.0.0.1:8000/improve")
        data = response.json()

        strategy = data.get("strategy", {})

        reply = f"""
📊 Content Strategy

💡 Insight: {strategy.get('insight')}
🚀 Tip: {strategy.get('tip')}
"""

        await message.channel.send(reply)

    # your existing logic here


# -------------------------
# ✅ ADD IT HERE
# -------------------------
@client.event
async def on_raw_reaction_add(payload):
    print("👀 RAW EVENT TRIGGERED")

    try:
        with open("engagement_data.json", "r") as f:
            data = json.load(f)

        for post in data:
            if post["message_id"] == payload.message_id:
                post["reactions"] += 1
                print("✅ Reaction added!")

        with open("engagement_data.json", "w") as f:
            json.dump(data, f, indent=4)

    except Exception as e:
        print("❌ Error:", e)
        
client.run("MTQ5NDMzMDMyNjQ0MzQ5MTQyOQ.G-excn.Nxqdl9e3IxzeYRESa8EplzORZXINUyA8RnTNkI")