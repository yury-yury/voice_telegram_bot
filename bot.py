import os
from dotenv import load_dotenv
from telegram.constants import ChatAction
from telegram.ext import Updater, CommandHandler, MessageHandler, filters
from revChatGPT.V1 import Chatbot


load_dotenv()

TOKENTG = os.getenv("TELEGRAM_TOKEN")
TOKENGPT = os.getenv("CHATGPT_TOKEN")

updater = Updater(TOKENTG)
chatbot = Chatbot(config={"access_token":TOKENGPT})


def chatgpt_reply(update, context):
    context.bot.send_chat_action(chat_id=update.effective_chat.id, action=ChatAction.TYPING)
    text = update.message.text
    reply = chatbot.ask(text)
    update.message.reply_text(reply)


echo_handler = MessageHandler(filters.text & (~filters.command), chatgpt_reply)
updater.dispatcher.add_handler(echo_handler)

updater.start_polling()
updater.idle()