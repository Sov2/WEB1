import telebot

bot = telebot.TeleBot('6715971982:AAGdcozmxAF5aOa4arwhcp5ryu9w0ak7oas')


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    f = open('db.txt', 'w')
    f.write(message.text)


bot.infinity_polling()
