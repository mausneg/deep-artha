from dotenv import load_dotenv
import telebot
import os

from main import DeepArtha

load_dotenv()

agent = DeepArtha()
bot = telebot.TeleBot(os.getenv("TELEBOT_TOKEN"), parse_mode="MARKDOWN")
    
@bot.message_handler(content_types=["text"])
def handle_text(message):
    response = agent.ask(question=message.text)
    bot.reply_to(message, response)

if __name__ == "__main__":
    bot.infinity_polling()