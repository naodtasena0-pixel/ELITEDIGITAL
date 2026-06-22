import os
import telebot
import google.generativeai as genai

# Initialize bot and AI
bot = telebot.TeleBot(os.environ.get('TELEGRAM_BOT_TOKEN'))
genai.configure(api_key=os.environ.get('GEMINI_API_KEY'))
model = genai.GenerativeModel('gemini-1.5-flash')

@bot.message_handler(func=lambda message: True)
def reply(message):
    try:
        system_prompt = "You are the Elite Digital AI Agent. Slogan: 'Quiet Hustle. Loud Results.' Be professional, concise, and helpful."
        response = model.generate_content(f"{system_prompt}\n\nUser: {message.text}")
        bot.reply_to(message, response.text)
    except Exception as e:
        print(f"Error: {e}")
        bot.reply_to(message, "Elite Digital is currently optimizing. Please try again.")

print("Bot is running...")
bot.infinity_polling()
