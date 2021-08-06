from telegram import ReplyKeyboardMarkup
main_keyboard=ReplyKeyboardMarkup([
    ['🛒 Buyurtma qilish'],
    ['🛍 Buyurtmalarim','⚙️ Sozlamalar'],
    ['✍️ Fikr bildirish']
    ],
     resize_keyboard=True)
def start(update,context):
    name=update.message.chat.first_name
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=f'''
        Assalomu alekum {name}. Marhamat buyurtma bering!
        ''',
        reply_markup=main_keyboard
    )
def main_menu(update,context):
    pass
def order(update,context):
    pass
def my_orders(update,context):
    pass
def settings(update,context):
    pass
def feedback(update,context):
    pass