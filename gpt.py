import os
import openai
from dotenv import load_dotenv
import telebot

from audio import speak, text_to_ogg


load_dotenv()

openai.api_key = os.getenv('OPENAI_API_KEY')

bot = telebot.TeleBot(os.getenv('TELEGRAM_TOKEN'))


@bot.message_handler(func=lambda _: True)
def handle_message(message):

    response = openai.Completion.create(
        model='text-davinci-003',
        prompt=message.text,
        temperature=0.8,
        max_tokens=1000,
        top_p=1.0,
        frequency_penalty=0.5,
        presence_penalty=0.0
    )
    answer = response['choices'][0]['text']

    bot.send_message(chat_id=message.from_user.id, text=answer)

    audio: str = text_to_ogg(answer)

    bot.send_voice(chat_id=message.from_user.id, voice=open(audio, 'rb'))


bot.polling()
