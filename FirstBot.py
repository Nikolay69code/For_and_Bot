import telebot

bot = telebot.Telebot("7758040041:AAHbsuH1DPpbh4XH6VN2ZaTAqQTuzH-sE7g")

@bot.message_handler(commands = ["start","Start"])
def start(message):
    bot.send_message(message.chat.id, "Привет!")

@bot.message_handler(commands = ["help"])
def start(message):
    bot.send_message(message.chat.id, message)

@bot.message_handler(commands = ["myname"])
def start(message):
    bot.send_message(message.chat.id, message.from_user.first_name)
    
@bot.message_handler()
def some(message):
    if message.text.lower()== "привет":
        bot.send_message(message.chat.id, "И тебе не хворать")
    elif message.text.lower()== "id":
        bot.reply_to(message,f"ID: {message.from_user.id}")

bot.polling(none_stop=True)