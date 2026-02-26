import telebot
import os

# Your Bot Token
API_TOKEN = '8753484200:AAFaazuIxBdXfH_Q-EkdVPGFLcLjnm5zrNo'
bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Welcome to StudyUnism! 📚\n\nI'm your AI brain. Send me any study notes, and I'll summarize them for you!")

@bot.message_handler(func=lambda message: True)
def handle_notes(message):
    user_input = message.text
    # This is a placeholder for the AI logic
    response = f"🧠 **Smart Study Analysis:**\n\nI've received your notes ({len(user_input)} letters).\n\n**Key Concept:** Detected topic from your text.\n**Question:** Based on this, what is the main goal?\n\nKeep studying! 🔥"
    bot.reply_to(message, response, parse_mode="Markdown")

print("Bot is starting...")
bot.infinity_polling()
