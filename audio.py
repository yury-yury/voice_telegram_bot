# import necessary modules for the task
import os
from gtts import gTTS
from playsound import playsound
import speech_recognition as sr


def speak(string, ) -> None:
    """Function to speak a string out loud"""
    if string.strip()[0] in list('ЙйЦцУуКкЕеНнГгШшЩщЗзХхъФфыВвАаПпРрОоЛлДдЖжЭэЯяЧчСсМмИиТтьБбЮю'):
        lang = 'ru'
    else:
        lang = 'en'

    audio = gTTS(text=string, lang=lang)    # convert the string to audio lang='en'

    audio.save('string.mp3')    # save the audio file



    playsound('./string.mp3')   # play the audio file


def text_to_ogg(text) -> str:
    if text.strip()[0].lower() in list('йцукенгшщзхъфывапролджэячсмитьбю'):
        lang = 'ru'
    else:
        lang = 'en'
    # Создаем объект gTTS с нашим текстом в качестве параметра
    tts = gTTS(text=text, lang=lang)
    # Определяем имя файла для сохранения аудиофайла
    filename = 'audio.ogg'
    # Сохраняем аудиофайл в текущую директорию
    tts.save(filename)
    # Возвращаем путь к файлу
    return str(os.path.abspath(filename))


def ogg_to_text(file_path):
    # Создаем объект Recognizer
    r = sr.Recognizer()

    # Открываем файл с помощью библиотеки PyDub
    with sr.AudioFile(file_path) as source:
        # Читаем содержимое файла в объект AudioData
        audio_data = r.record(source)

    # Используем библиотеку для распознавания речи
    # и сохраняем результат в переменную text
    text = r.recognize_google(audio_data, language="ru-RU")  # Если запись на русском языке

    # Возвращаем распознанный текст
    return text


if __name__ == '__main__':
    audio = open('./audio.ogg', 'rb')
    print(ogg_to_text(audio))

    # string = 'How are you'
    # audio = text_to_ogg(string)
    # playsound(audio)  # play the audio file

    # string = 'Привет. Как дела?'
    # speak(string)
    #
    # string = 'Hello. How are you?'
    # speak(string)


