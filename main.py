import logging
from telegram import Update
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, ConversationHandler
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters
import time
import random
from TOKEN import TOKEN

from footballer import *

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
# set higher logging level for httpx to avoid all GET and POST requests being logged
logging.getLogger("httpx").setLevel(logging.WARNING)

logger = logging.getLogger(__name__)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")

async def add_player(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    await update.message.reply_text(
        "Insert player's name"
    )
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, input_text))

async def draw_teams(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    team_a, team_b = make_teams(available_players_pool)
    print_teams_and_stats(team_a, team_b)
    answer = print_teams_and_stats(team_a, team_b)
    await context.bot.send_message(chat_id=update.effective_chat.id, text=answer)

async def new_match(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    await update.message.reply_text("Insert players' names")
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, input_text))

async def input_text(update: Update, context: ContextTypes.DEFAULT_TYPE):
    pl_name = update.message.text
    await update.message.reply_text(f"What is {pl_name}'s initial rank? (1 to 5)?")
    pl_rank = update.message.text
    logger.info(f"Inserting {pl_name} with initial rank {pl_rank}")
    players_pool.append(Footballer(name=pl_name, start_rank=pl_rank))
    print(f"player:{players_pool[0].name}rank:{players_pool[0].start_rank}")


if __name__ == '__main__':
    application = ApplicationBuilder().token(TOKEN).build()
    
    start_handler = CommandHandler('start', start)
    application.add_handler(start_handler)

    application.add_handler(CommandHandler('add_player', add_player))
    application.add_handler(CommandHandler('draw_teams', draw_teams))
    application.add_handler(CommandHandler('new_match', new_match))
   
    application.run_polling()

