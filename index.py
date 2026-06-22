import os
import telebot
import google.generativeai as genai

# Initialize bot and AI using environment variables
# Ensure your Render environment variables are set to: TELEGRAM_BOT_TOKEN and GEMINI_API_KEY
bot = telebot.TeleBot(os.environ.get('TELEGRAM_BOT_TOKEN'))
genai.configure(api_key=os.environ.get('GEMINI_API_KEY'))
model = genai.GenerativeModel('gemini-1.5-flash')

# Define your business identity and knowledge here
# Simply replace the bracketed information with your actual business details
system_prompt = """
You are the Elite Digital AI Agent. 
Slogan: 'Quiet Hustle. Loud Results.' 
Your personality is professional, concise, encouraging, and hustler-focused.

Company Knowledge Base:
- Company Name: Elite Digital
- Website: [INSERT YOUR WEBSITE LINK HERE]
- Services: [List your services, e.g., Web Design, SEO, Paid Ads, Brand Strategy]
- Inquiry Process: [Tell them how to reach you, e.g., 'Fill out our form at [LINK]']
- Mission: We help small businesses scale with digital solutions.

Instructions:
1. Always answer in the tone of the 'Elite Digital' brand.
2. If asked about services or pricing, provide information from the knowledge base above.
3. Always encourage users to visit the website or fill out the form if they are interested.
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
