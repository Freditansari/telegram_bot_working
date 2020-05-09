from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, Dispatcher
import logging
logging.basicConfig(format='%(levelname)s - %(message)s',
                    level=logging.DEBUG)
logger = logging.getLogger(__name__)
updater = None

def start(update, context):
    s = "Welcome I Am The Finxter Chat Bot! Your life has now changed forever."
    update.message.reply_text(s)

def start_bot():
    global updater
    updater = Updater(
        '1270470028:AAGitNmo6dBYzfatJ2bokXHCfL_AuMFfiiY', use_context=True)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler('start', start))
    updater.start_polling()
    updater.idle()


start_bot()


