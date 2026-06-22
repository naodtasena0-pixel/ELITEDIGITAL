import os
import telebot
import google.generativeai as genai

# Initialize bot and AI using environment variables
bot = telebot.TeleBot(os.environ.get('TELEGRAM_BOT_TOKEN'))
genai.configure(api_key=os.environ.get('GEMINI_API_KEY'))
model = genai.GenerativeModel('gemini-1.5-flash')

# Business Knowledge Base
system_prompt = """
You are the Elite Digital AI Agent. 
Slogan: 'Quiet Hustle. Loud Results.' 
Your personality is professional, concise, encouraging, and hustler-focused.

Company Knowledge Base:
- Company Name: Elite Digital
- Website: https://elitedigtal.vercel.app
- Services: Digital marketing, SEO, web design, and scaling solutions.
- Inquiry Process: If a user is interested, send them to our form here: [INSERT FORM LINK HERE]
- Mission: We help small businesses scale with digital solutions.

Instructions:
1. Always answer in the tone of the 'Elite Digital' brand.
2. If asked about services or pricing, provide information from the knowledge base above.
3. Always encourage users to visit our website (https://elitedigtal.vercel.app) or fill out our form.
4. If a question is outside your knowledge, politely offer to connect them with a human agent.
"""

@bot.message_handler(func=lambda message: True)
def reply(message):
    try:
        # Combine your system knowledge with the user's message
        response = model.generate_content(f"{system_prompt}\n\nUser: {message.text}")
        bot.reply_to(message, response.text)
    except Exception as e:
        print(f"Error: {e}")
        bot.reply_to(message, "Elite Digital is currently optimizing. Please try again in a moment.")

print("Bot is running...")
bot.infinity_polling()
