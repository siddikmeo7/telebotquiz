import psycopg2
from secret import *

# REGISTRATION TO TELEBOT
import telebot
from telebot import TeleBot
from io import BytesIO

bot = TeleBot(API_BOT)

def open_connection ():
    conn = psycopg2.connect(
        database = "TelegramDB",
        user = "postgres",
        host = "localhost",
        password = PASSWORD,
        port = 5432
    )
    return conn

def close_connection(conn,cur):
    conn.close()
    cur.close()
                            





