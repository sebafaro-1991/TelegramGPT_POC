import os

import telebot
import openai

#Get the telegram token that we saved in the secrets
BOT_TOKEN = os.environ.get('TOKEN')

bot = telebot.TeleBot(BOT_TOKEN)


def OpenAi(prompt):
  #Get the OpenAI token that we saved in the secrets
  openai.api_key = os.getenv("OPENAI_API_KEY")

  #OpenAI doc https://platform.openai.com/docs/api-reference/chat/create
  response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo-0301",
    messages=[{
      "role":
      "system",
      "content":
      "You are a virtual assistant working for a telecomunication company."
    }, {
      "role": "user",
      "content": prompt
    }],
  )
  return response.choices[0].message.content


#Messages for the start commands
@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
  bot.reply_to(message, "You are ready now to start, please say hi to the bot")


#Reply from openAI api
@bot.message_handler(func=lambda msg: True)
def echo_all(message):
  bot.reply_to(message, OpenAi(message.text))
  print(message.text)


bot.infinity_polling()