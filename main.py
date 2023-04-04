import os

import telebot
import openai

BOT_TOKEN = os.environ.get('TOKEN')

bot = telebot.TeleBot(BOT_TOKEN)

def OpenAi(prompt):
  openai.api_key = os.getenv("OPENAI_API_KEY")
  response = openai.ChatCompletion.create(
  model="gpt-3.5-turbo-0301",
   messages=[
        {"role": "system", "content": "You are Change Management expert working in a telecomunication company."},
        {"role": "user", "content": prompt}
    ],

  )
  return response.choices[0].message.content

@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    bot.reply_to(message, "You are ready now to start, please say hi to the bot")


@bot.message_handler(func=lambda msg: True)
def echo_all(message):  
    bot.reply_to(message, OpenAi(message.text))
    print(message.text)
bot.infinity_polling()