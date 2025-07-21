import telebot
import requests

bot = telebot.TeleBot("8121802177:AAH6mPuzn8Zrt6u_wzTWdlTXBMtCUzhdQYc")


WEATHER_API_KEY = "d4da12eaa1ae472196d200724252107"
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привіт, як справи? Введи назву міста, щоб отримати прогноз погоди")

@bot.message_handler(commands=['help'])
def send_help(message):
    bot.reply_to(message, "Надішліть назву міста і я розкажу, яка там зараз погода.")

def get_weather(city):
    url = f"http://api.weatherapi.com/v1/current.json?key={WEATHER_API_KEY}&q={city}&lang=uk"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if "error" in data:
            return "Місто не знайдено або сталася якась помилка"
        temp_c = data["current"]["temp_c"]
        condition = data["current"]["condition"]["text"]
        return f"Погода в {city}:\n🌡 Температура: {temp_c}°C\n Опис: {condition}"
    else:
        return "Не вдалося отримати дані, спробуйте пізніше."

@bot.message_handler(func=lambda message: True)
def send_city_weather(message):
    city = message.text.strip()
    print(f"Отримано запит на погоду в місті: {city}")
    weather_info = get_weather(city)
    bot.reply_to(message, weather_info)

print("Бот запущено. Очікування повідомлень...")
bot.infinity_polling()
