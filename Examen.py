import os
import telebot

bot = telebot.TeleBot('1802864810:AAEwzKG75j3t7621zNhUN4ukkB7j8XUpCBg') #anadimos el token

bot.send_message(1827863421, 'Bienvenido esta Conectado..... ;)')

@bot.message_handler(commands=['formula_cuadratica', 'Ecuacion cuadratica'])
def foto(mensaje):
    photo = open('formula.png', 'rb')
    bot.send_photo(1827863421, photo)

@bot.message_handler(commands=['Unidades', 'conversion de unidades','equivalencias'])
def foto2(mensaje):
    photo = open('unidades.png', 'rb')
    bot.send_photo(1827863421, photo)

@bot.message_handler(commands=['documento', 'pdf'])
def documento(mensaje):
    document = open('GIT.pdf', 'rb')
    bot.send_document(1827863421, document)

@bot.message_handler(commands=['gps','localizacion'])
def documento(mensaje):
    bot.send_location(1827863421, 15.49560, -87.99128)
bot.polling()
