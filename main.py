import telebot
import constants
import random
import pyowm


bot = telebot.TeleBot(constants.token)


greetings = ["Привет", "Мяу", "Здравствуй",]
how_are_you = ["Отлично", "Ужасно", "Хорошо","Супер!"]
thanks = ["Всегда рад помочь!", "Не за что", "Пожалуйста"]
how_are_you_question = ["У тебя как?", "Как сам(-а) поживаешь?", "Как твои успехи?"]


@bot.message_handler(commands=["weather"])
def weather(message):
    city = bot.send_message(message.chat.id, "В каком городе Вам показать погодку?")
    bot.register_next_step_handler(city, weath)


def weath(message):
    owm = pyowm.OWM("1a115174f1d6212efaf1390c09260d2e")
    city = message.text
    weather = owm.weather_at_place(city)
    w = weather.get_weather()
    temperature = w.get_temperature("celsius")["temp"]
    wind = w.get_wind()["speed"]
    hum = w.get_humidity()
    desc = w.get_detailed_status()
    bot.send_message(message.chat.id, "Сейчас в городе " + str(city) + " " + str(desc) + ", температура - " + str(temperature) + "°C, влажность - " + str(hum) + "%, скорость ветра - " +str(wind) + "м/с.")


@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id, "Привет, " + message.chat.first_name)


@bot.message_handler(content_types=["text"])
def main(message):
    if message.text == "Привет" or message.text == "привет":
        bot.send_message(message.chat.id, random.choice(greetings) + ", " + message.chat.first_name)
    elif message.text == "Как дела?":
        bot.send_message(message.chat.id, random.choice(how_are_you) + ". " + random.choice(how_are_you_question))
    elif message.text == "Спасибо" or message.text == "спасибо":
        bot.send_message(message.chat.id, random.choice(thanks) + ", " + message.chat.first_name)
    elif message.text == "Отлично" or message.text == "отлично" or message.text == "Хорошо" or message.text == "хорошо":
        bot.send_message(message.chat.id, "Я рад за тебя!")
    elif message.text == "Ужасно" or message.text == "ужасно" or message.text == "Плохо" or message.text == "плохо":
        bot.send_message(message.chat.id, "Держись, мой друг!")


@bot.message_handler(commands=["weather"])
def weather(message):
    city = bot.send_message(message.chat.id, "В каком городе Вам показать погодку?")
    bot.register_next_step_handler(city, weath)


def weath(message):
    owm = pyowm.OWM("1a115174f1d6212efaf1390c09260d2e", language="ru")
    city = message.text
    weather = owm.weather_at_place(city)
    w = weather.get_weather()
    temperature = w.get_temperature("celsius")["temp"]
    wind = w.get_wind()["speed"]
    hum = w.get_humidity()
    desc = w.get_detailed_status()
    bot.send_message(message.chat.id, "Сейчас в городе " + str(city) + " " + str(desc) + ", температура - " + str(temperature) + "°C, влажность - " + str(hum) + "%, скорость ветра - " +str(wind) + "м/с.")


if __name__ == "__main__":
    bot.polling(none_stop=True)
