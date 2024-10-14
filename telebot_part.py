from connection import * 
from database_settings import * 
from telebot import types
from telebot.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton

admin_user_id = 123456789
def is_admin (user_id):
    return user_id == admin_user_id


@bot.message_handler(commands=['start'])
def welcome (message):
    bot.send_message(message.chat.id,f"Welcome dear {message.chat.username}!")
    bot.send_message(message.chat.id,f"Your Telegram Id: {message.chat.id}!")
    create_T_users()
    is_registered(message)
    user_register(message)

def display_buttons (message):
    button1 = KeyboardButton("View_products")
    button2 = KeyboardButton("Add_to_carts")
    button3 = KeyboardButton("View_carts")
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row(button1)
    markup.row(button2)
    markup.row(button3)
    bot.send_message(message.chat.id,f"Hello dear {message.chat.username}",replymarkup = markup)
    























bot.infinity_polling() 

     



















bot.infinity_polling()
