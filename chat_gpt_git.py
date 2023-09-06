import telebot
import openai

telegram_key = 'key'
openai.api_key = 'api_key'

bot = telebot.TeleBot(telegram_key)


@bot.message_handler(commands=['start'])
def hello(message):
    bot.send_message(message.chat.id, 'Привіт! Я твій ChatGPT бот! Готовий тобі допомогти!')


@bot.message_handler(content_types=['text'])
def main(message):
    reply = ''
    response = openai.Completion.create(
        engine='gpt-3.5-turbo',
        prompt=message.text,
        max_tokens=150,
        temperature=0.7,
        n=1,
        stop=None
    )

    if response and response.choices:
        reply = response.choices[0].text.strip()
    else:
        reply = 'Упс, щось не так!'


    bot.send_message(message.chat.id, reply)


bot.polling(none_stop=True)