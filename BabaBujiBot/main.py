from typing import Final

from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes


TOKEN: Final = '6764309262:AAFLIOeGXRN5XJlKkPEfN9Bua8pDblVAGk4'
BOT_USERNAME: Final = 'bababuji_bot'

#komande

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Hoces Hentai?!')


async def help_command(update: Update, context: ContextTypes):
    await update.message.reply_text('Sta te zanima?!')


#odgovori na poruke

def handle_response(text: str) -> str:

    if text == 'hentai' or text == 'Hentai':
        return 'https://www.youtube.com/watch?v=YFNtiA1T4MM&ab_channel=FeFe'


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):

    message_type = update.message.chat.type
    text: str = update.message.text

    if message_type == 'group':

        response: str = handle_response(text)

    print('Bot', response)
    await update.message.reply_text(response)

#error logovi
async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} caused error {context.error}')

if __name__ == '__main__':
    app = Application.builder().token(TOKEN).build()
    #komande
    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('help', help_command))

    app.add_handler(MessageHandler(filters.Text, handle_message))

    app.add_error_handler(error)

    app.run_polling(poll_interval=3)