from telegram.ext import Updater,CommandHandler,MessageHandler,Filters,ConversationHandler
from conversation import *
def main():
    updater = Updater(token = '1764688508:AAEznpu_JgW9HsR5-nzxqZEz9NOoxm7y93A',use_context = True)
    dispatcher = updater.dispatcher
    handler = ConversationHandler(
        entry_points=[CommandHandler('start',start)],
        states={
            'main_menu':[
                MessageHandler(Filters.text,main_menu)
            ],
            'feedback':[
                MessageHandler(Filters.text,feedback)
            ]
        },
        fallbacks = [MessageHandler(Filters.text,start)]
    )
    dispatcher.add_handler(handler)
    updater.start_polling()

main()