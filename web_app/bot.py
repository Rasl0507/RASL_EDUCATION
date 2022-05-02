from telegram.ext import CommandHandler
import logging
from telegram.ext import Updater, MessageHandler, Filters
import time

months = {'Jan': 1, 'Feb': 2, 'Mar': 3, 'Apr': 4, 'May': 5, 'Jun': 6, 'Jul': 7, 'Aug': 8, 'Sep': 9, 'Oct': 10, 'Nov': 11,
          'Dec': 12}

# Запускаем логгирование
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG
)

logger = logging.getLogger(__name__)

TOKEN = 'BOT_TOKEN'


def echo(update, context):
    text = update.message.text
    ttext = ''
    if text == 'Windows 11':
        with open('data/Windows 11.txt', 'r', encoding='utf-8') as W:
            ttext = W.read()
    if text == 'Windows 8.1':
        with open('data/Windows 8.1.txt', 'r', encoding='utf-8') as W:
            ttext = W.read()
    if text == 'Windows 10':
        with open('data/Windows 10.txt', 'r', encoding='utf-8') as W:
            ttext = W.read()
    if text == 'Windows 7':
        with open('data/Windows 7.txt', 'r', encoding='utf-8') as W:
            ttext = W.read()
    if text == 'Office':
        with open('data/Office.txt', 'r', encoding='utf-8') as W:
            ttext = W.read()
    if text == 'Zona':
        with open('data/Zona.txt', 'r', encoding='utf-8') as W:
            ttext = W.read()
    if text == 'DriverPack':
        with open('data/DriverPack.txt', 'r', encoding='utf-8') as W:
            ttext = W.read()
    if text == 'PyCharm':
        with open('data/PyCharm.txt', 'r', encoding='utf-8') as W:
            ttext = W.read()
    if text == 'uFiler':
        with open('data/uFiler.txt', 'r', encoding='utf-8') as W:
            ttext = W.read()
    if text == 'uTorrent':
        with open('data/uTorrent.txt', 'r', encoding='utf-8') as W:
            ttext = W.read()
    if text == 'Яндекс.Диск':
        with open('data/Яндекс.Диск.txt', 'r', encoding='utf-8') as W:
            ttext = W.read()
    if text == 'Облако Mail.Ru':
        with open('data/Облако Mail.Ru.txt', 'r', encoding='utf-8') as W:
            ttext = W.read()
    if text == 'Skype':
        with open('data/Skype.txt', 'r', encoding='utf-8') as W:
            ttext = W.read()
    if text == 'Zoom':
        with open('data/Zoom.txt', 'r', encoding='utf-8') as W:
            ttext = W.read()
    if text == 'Яндекс.Телемост':
        with open('data/Яндекс.Телемост.txt', 'r', encoding='utf-8') as W:
            ttext = W.read()
    update.message.reply_text(ttext)


def start(update, context):
    update.message.reply_text(
        "Привет! Я бот, который знает о приложениях.")


def help(update, context):
    update.message.reply_text(
        "Введите название программы и я расскажу о ней подробнее!")


def main():

    updater = Updater("5363155554:AAErsdvom2sPmFpGkGNpImSUqpDMMFs2oaw")

    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    text_handler = MessageHandler(Filters.text & ~Filters.command, echo)

    dp.add_handler(text_handler)
    updater.start_polling()

    updater.idle()


# Напишем соответствующие функции.
# Их сигнатура и поведение аналогичны обработчикам текстовых сообщений.


# Запускаем функцию main() в случае запуска скрипта.
if __name__ == '__main__':
    main()