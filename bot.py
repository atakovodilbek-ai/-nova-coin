
import os
import telebot

TOKEN = os.getenv("BOT_TOKEN")

if not TOKEN:
    raise RuntimeError("BOT_TOKEN sozlanmagan")

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=["start"])
def start(message):
    bot.reply_to(
        message,
        "🚀 NOVA COIN ULTRA+\n\n"
        "Xush kelibsiz!\n"
        "Bu virtual demo ballar loyihasi.\n\n"
        "/balance - Balans\n"
        "/bonus - Kunlik demo bonus\n"
        "/help - Yordam"
    )

@bot.message_handler(commands=["balance"])
def balance(message):
    bot.reply_to(message, "💎 Demo balans: 0 NOVA")

@bot.message_handler(commands=["bonus"])
def bonus(message):
    bot.reply_to(message, "🎁 Bu demo bot. Bonus funksiyasi hali ulanmagan.")

@bot.message_handler(commands=["help"])
def help_command(message):
    bot.reply_to(message, "Buyruqlar: /start /balance /bonus /help")

bot.infinity_polling()
