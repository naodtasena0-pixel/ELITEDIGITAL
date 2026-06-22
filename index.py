import os
from flask import Flask, request
import telebot
import google.generativeai as genai

app = Flask(__name__)

# Load tokens from environment variables
bot = telebot.TeleBot(os.environ.get('TELEGRAM_BOT_TOKEN'))
genai.configure(api_key=os.environ.get('GEMINI_API_KEY'))
model = genai.GenerativeModel('gemini-1.5-flash')

@app.route('/api', methods=['POST'])
def webhook():
    # Receive update from Telegram
    json_string = request.get_data().decode('utf-8')
    update = telebot.types.Update.de_json(json_string)
    bot.process_new_updates([update])
    return 'OK', 200

@bot.message_handler(func=lambda message: True)
def reply(message):
    try:
        # Define the personality
        system_prompt = "You are the Elite Digital AI Agent. Slogan: 'Quiet Hustle. Loud Results.' Be professional, concise, and helpful."
        
        # Get AI response
        response = model.generate_content(f"{system_prompt}\n\nUser: {message.text}")
        bot.reply_to(message, response.text)
    except Exception as e:
        print(f"Error: {e}")
        bot.reply_to(message, "Elite Digital is currently optimizing. Please try again.")

if __name__ == '__main__':
    app.run()
