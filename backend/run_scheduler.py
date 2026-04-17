from scheduler import start_scheduler, scheduled_job
import time

print("🚀 Starting scheduler...")

start_scheduler()

print("⏳ Scheduler running...")

# 🔥 Force run once
scheduled_job()

while True:
    time.sleep(1)