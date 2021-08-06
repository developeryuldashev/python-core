from telegram.ext import Updater,CommandHandler,MessageHandler,Filters
from own_filter import *
def start(update,context):
    context.bot.send_message(chat_id=update.effective_chat.id,text='Bot ishladi!')
def matn(update,context):
    context.bot.send_message(chat_id=update.effective_chat.id,text="Matn ko'rinishidagi habar!")
def audio(update,context):
    context.bot.send_message(chat_id=update.effective_chat.id,text="Audio ko'rinishidagi habar!")
def foto(update,context):
    context.bot.send_message(chat_id=update.effective_chat.id,text='Rasm xabar!')
def hujjat(update,context):
    context.bot.send_message(chat_id=update.effective_chat.id,text="hujjat ko'rinishidagi xabar")
updater=Updater(token='1703590801:AAEgbRMujjbmHi2uQMEGJenGvhoI1_1-r0E',use_context=True)
###use_context bu har bitta foydaluvchiga alohida alohida javob beradi, aralashtirib yubormaydi

dispatcher=updater.dispatcher
## yo'l ko'rsatuvchi, boshqaruvchi,Nazoratchi

start_handler=CommandHandler('start',start)
matn_handler=MessageHandler(Filters.text,matn)
audio_handler=MessageHandler(Filters.audio,audio)
foto_handler=MessageHandler(Filters.photo,foto)
doc_handler=MessageHandler(Filters.document,hujjat)

dispatcher.add_handler(start_handler)
dispatcher.add_handler(matn_handler)
dispatcher.add_handler(audio_handler)
dispatcher.add_handler(foto_handler)
dispatcher.add_handler(doc_handler)

updater.start_polling()














































# from telegram.ext import Updater,CommandHandler,MessageHandler
# """endi start degan metod yozamiz"""
# def start(update,context):
#     context.bot.send_message(chat_id=update.effective_chat.id,text="Assalomu alekum!")
# updater=Updater(token='1703590801:AAEgbRMujjbmHi2uQMEGJenGvhoI1_1-r0E',use_context=True)
# dispatcher=updater.dispatcher
# start_handler=CommandHandler("start",start)
# dispatcher.add_handler(start_handler)
# updater.start_polling()