from content_generator import generate_content
from telegram_bot import send_telegram_message

tone = "casual, witty"
topic = "AI marketing"

content = generate_content(tone, topic, "Telegram")

# Send first message
send_telegram_message(content[0])