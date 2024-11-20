import logging
from telegram import Update
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, ConversationHandler
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters
import time
import random
from TOKEN import TOKEN

from footballer import Footballer

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
# set higher logging level for httpx to avoid all GET and POST requests being logged
logging.getLogger("httpx").setLevel(logging.WARNING)

logger = logging.getLogger(__name__)

available_players_pool = [
# Footballer(name="Philipp", start_rank=3),
# Footballer(name="Mormar", start_rank=3),
# Footballer(name="Sboben", start_rank=4),
# Footballer(name="Mic", start_rank=3),
# Footballer(name="Karim", start_rank=3),
# Footballer(name="Duccio", start_rank=1),

Footballer(name="Bonfa", start_rank=2),
Footballer(name="Karim", start_rank=3),
Footballer(name="Mor", start_rank=3),
Footballer(name="Akil", start_rank=3),
Footballer(name="Duccio", start_rank=1),
Footballer(name="Philipp", start_rank=3),
Footballer(name="Francesco collega", start_rank=3),
Footballer(name="Blallo", start_rank=2),
Footballer(name="Gio", start_rank=3),
Footballer(name="Pezzo", start_rank=3),
Footballer(name="Yarru", start_rank=3),
Footballer(name="Sboben", start_rank=4),
Footballer(name="Moataz", start_rank=3),
Footballer(name="Zebib", start_rank=2),
]

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")

async def add_player(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    await update.message.reply_text(
        "Insert player's name"
    )
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, input_text))

async def draw_teams(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    team_size=int(len(available_players_pool) / 2)
    
    team_a = random.sample(available_players_pool, team_size)
    team_b = [x for x in available_players_pool if x not in team_a]

    team_a_names = []
    team_b_names = []
    for pl in team_a:
        team_a_names.append(pl.name)
    for pl in team_b:
        team_b_names.append(pl.name)

    logger.info(team_a_names)
    logger.info(team_b_names)
    out_text = f"Sorting teams...\nTEAM A: {team_a_names}\nTEAM B: {team_b_names}\n"
    logger.info(out_text)
    await context.bot.send_message(chat_id=update.effective_chat.id, text=out_text)


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
   
    application.run_polling()

