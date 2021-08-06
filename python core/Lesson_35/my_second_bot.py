from telegram.ext import Updater,CommandHandler,MessageHandler,Filters
from telegram import ReplyKeyboardMarkup
from own_filter import filter_awesome, filter_raxmat
keyboard=ReplyKeyboardMarkup([['Bosh sahifa'],
          ['chapga','unga'],
          ['ortga']
          ], resize_keyboard=True)

def start(update,context):
    context.bot.send_message(chat_id=update.effective_chat.id,text=f"Assalomu alekum, {update.message.chat.first_name} Hush kelibsiz, qanday yordam bera olaman!",reply_markup=keyboard)
def text(update, context):
    if update.message.text=='unga':
        print(update)
        print(update.message.date)
        print(update.message.chat)
        print(update.message.chat.username)
        context.bot.send_message(chat_id=update.effective_chat.id,text="siz 'unga' tugmasini bosdingiz ")
def raxmat(update,context):
    context.bot.send_message(chat_id=update.effective_chat.id,text=f"Barakalla, {update.messsage.chat.username}  sizga Raxmat aytishdi!")
def Audio(update,context):
    context.bot.send_message(chat_id=update.effective_chat.id,text="Audio Xabar!")
def foto(update,context):
    context.bot.send_message(chat_id=update.effective_chat.id,text="Rasmli Xabar!")
def hujjat(update,context):
    context.bot.send_message(chat_id=update.effective_chat.id,text="hujjat ko'rinishidagi  Xabar!")
def joylashuv(update,context):
    context.bot.send_message(chat_id=update.effective_chat.id,text="Locatsiya ko'rinishidagi Xabar!")
def voice(update,context):
    context.bot.send_message(chat_id=update.effective_chat.id,text="Voic(audio) Xabar!")
def emoj(update,context):
    context.bot.send_message(chat_id=update.effective_chat.id,text="sticer xabar")
def vidio(update,context):
    context.bot.send_message(chat_id=update.effective_chat.id,text="vidio xabar!")
def echo(update,context):
    context.bot.send_message(chat_id=update.effective_chat.id,text=update.message.text)
def poll(update,context):
    context.bot.send_message(chat_id=update.effective_chat.id,text="So'rovnoma jo'natildi")
def contact(update,context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Contact jo'natildi")
def yozuv(update,context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Sen 'Dilshod' deb yozding")


updater=Updater(token='1691206810:AAGnp25_bR6KqKtusXbPotsYD3Rqdg4Qx_s', use_context=True)

dispatcher=updater.dispatcher

raxmat_handler=MessageHandler(filter_raxmat,raxmat)
start_handler=CommandHandler('start',start)
text_handler=MessageHandler(Filters.text,text)
audio_handler=MessageHandler(Filters.audio,Audio)
foto_handler=MessageHandler(Filters.photo,foto)
hujjat_handler=MessageHandler(Filters.document,hujjat)
joylashuv_handler=MessageHandler(Filters.location,joylashuv)
voice_handler=MessageHandler(Filters.voice,voice)
emoj_handler=MessageHandler(Filters.sticker,emoj)
vidio_handler=MessageHandler(Filters.video,vidio)
echo_handler=MessageHandler(Filters.text,echo)
poll_handler=MessageHandler(Filters.poll,poll)
contact_handler=MessageHandler(Filters.contact,contact)
yozuv_handler=MessageHandler(filter_awesome,yozuv)


dispatcher.add_handler(start_handler)
#dispatcher.add_handler(text_handler)
dispatcher.add_handler(audio_handler)
dispatcher.add_handler(foto_handler)
dispatcher.add_handler(hujjat_handler)
dispatcher.add_handler(joylashuv_handler)
dispatcher.add_handler(poll_handler)
dispatcher.add_handler(voice_handler)
dispatcher.add_handler(emoj_handler)
dispatcher.add_handler(vidio_handler)
#dispatcher.add_handler(echo_handler)
dispatcher.add_handler(contact_handler)
dispatcher.add_handler(yozuv_handler)
dispatcher.add_handler(raxmat_handler)

updater.start_polling()
