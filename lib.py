import os
from revChatGPT.V1 import Chatbot   # импортируем библиотеку
from dotenv import load_dotenv


load_dotenv()

accesstoken= os.getenv('TELEGRAM_TOKEN')  # задаем переменную токена

chatbot = Chatbot(config={"access_token":accesstoken})  # инициализируем чатбота

while True:
    message = input("Вы:")          # создаем ввод текста
    output = chatbot.ask(message)   # даем запрос ChatGPT с набранным текстом
    print(f"ChatGPT:{output.__dir__()}")      # выводим ответ ChatGPT