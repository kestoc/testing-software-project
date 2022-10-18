"""
Bot para tienda virtual en Telegram desarrollada por @kestoc y @rohaquinlop
"""

import json
import logging
from telegram import __version__ as TG_VER

try:
    from telegram import __version_info__
except ImportError:
    __version_info__ = (0, 0, 0, 0, 0)  # type: ignore[assignment]

if __version_info__ < (20, 0, 0, "alpha", 1):
    raise RuntimeError(
        f"This example is not compatible with your current PTB version {TG_VER}. To view the "
        f"{TG_VER} version of this example, "
        f"visit https://docs.python-telegram-bot.org/en/v{TG_VER}/examples.html"
    )
from telegram import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove, Update
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
    ConversationHandler,
    MessageHandler,
    filters,
    PicklePersistence
)

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)


db = json.load(open('db.json'))

EXIT, BUY = range(2)

async def start(update : Update, context: ContextTypes.DEFAULT_TYPE) -> int:
  """Starts the conversation and asks the type of product that the user will buy"""
  
  products_list = []
  
  await update.message.reply_text(
    "Hola! Bienvenido a KR-Shop, yo soy el bot que te estara atendiendo.\n"
    "Envia /cancel en cualquier momento para detener el proceso de compra.\n"
    "Que producto deseas comprar?",
    reply_markup=build_keyboard(products_list)
  )
  
  await update.message.reply_text(update.message)
  
  return BUY

def build_keyboard(current_list : list[str]) -> InlineKeyboardMarkup:
  print(db)
  return InlineKeyboardMarkup.from_column(
    [InlineKeyboardButton(producto, callback_data=(producto, current_list)) for producto in db['productos']]
  )

async def buy(update : Update, context: ContextTypes.DEFAULT_TYPE) -> int:
  user = update.message.from_user
  
  await update.message.reply_text(update.message)
  
  await update.message.reply_text(
    'Excelente, muchas gracias por comprar con nosotros'
  )
  
  return ConversationHandler.END

async def cancel(update : Update, context: ContextTypes.DEFAULT_TYPE) -> int:
  '''Cancels and sends the conversation.'''
  user = update.message.from_user.first_name
  
  await update.message.reply_text('Hasta luego %s!, gracias por considerar comprar aqui en KR-Shop, espero que vuelvas pronto' % user, reply_markup=ReplyKeyboardRemove())
  
  return ConversationHandler.END
