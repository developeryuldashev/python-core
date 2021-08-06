from conversation import *
from telegram.ext import Updater,CommandHandler,MessageHandler,ConversationHandler
def main():
    updater=Updater(token='1623960429:AAEMa2jvGlvFjDSygeO3ExGW_niabwdSR1E',use_context=True)
    dispatcher=updater.dispatcher
    handler=ConversationHandler(
        entry_points=[CommandHandler('start',start)],
        states={},
        fallbacks=[]
    )
    dispatcher.add_handler(handler)
    updater.start_polling()
main()