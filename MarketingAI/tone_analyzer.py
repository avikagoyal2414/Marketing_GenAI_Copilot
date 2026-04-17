import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("sk-proj-2GZB4QErprirtjR3mZ_6nhDQpq0JBsKhmSjlZBDQ-gRVGWcOVQ7mZ83BBc-8IyvHS66WPlnDywT3BlbkFJ6UQypq-Hle_DignrGYLyZaMgm--MXCjx6cdRZX1NgregkSsKmozgPBzm7weX4aRtp2OD07qZMAj"))

def analyze_tone(posts):
    print("🔥 analyze_tone is being called")
    return "casual, witty, emoji-heavy"