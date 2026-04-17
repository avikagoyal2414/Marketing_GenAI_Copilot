from apscheduler.schedulers.background import BackgroundScheduler
import requests
WEBHOOK_URL = "https://discord.com/api/webhooks/1494434963603587152/o2tbHoG_tfnOHcXthR-bTZ-pYtpUCKM2vaXYYR3_ZFYPtTdLMZBHih5KokhzLrLYdRDQ"
API_URL = "http://127.0.0.1:8000/generate"


def scheduled_job():
    import random

    print("🔥 Job triggered!")

    topics = [
        "AI marketing",
        "Startup growth",
        "Content strategy",
        "Automation tools"
    ]

    platforms = ["Twitter", "LinkedIn"]

    topic = random.choice(topics)
    platform = random.choice(platforms)

    payload = {
        "posts": ["AI is powerful"],
        "topic": topic,
        "platform": platform
    }

    try:
        response = requests.post(API_URL, json=payload)
        data = response.json()

        content = data.get("content", [])

        if isinstance(content, list):
            message = "\n\n".join(content)
        else:
            message = str(content)

        final_message = f"""
🚀 Scheduled Post

📌 Topic: {topic}
📱 Platform: {platform}

{message}
"""

        requests.post(WEBHOOK_URL, json={"content": final_message})

        print("✅ Sent to Discord!")

    except Exception as e:
        print("❌ Error:", e)


def start_scheduler():
    scheduler = BackgroundScheduler()

    # Run every 10 seconds (faster testing)
    scheduler.add_job(scheduled_job, 'interval', minutes=10)

    scheduler.start()
    print("✅ Scheduler started")