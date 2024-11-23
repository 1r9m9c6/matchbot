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

async def add_new_player(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    await update.message.reply_text(
        "Insert player's name"
    )
    application.add_handler(handle_new_player_name_insertion)

async def new_player_name_insertion(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    application.remove_handler(handle_new_player_name_insertion)
    pl_name = update.message.text
    if (is_player_new(pl_name)):
        await update.message.reply_text(f"What is {pl_name}'s initial rank? (1 to 5)?")
        insert_new_players_name(pl_name)
        application.add_handler(handle_new_player_rank_insertion)
    else:
        await update.message.reply_text(f"{pl_name} is not a new player")

async def new_player_rank_insertion(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    try:
        pl_rank = int(update.message.text)
    except:
        pl_rank = 0
    application.remove_handler(handle_new_player_rank_insertion)
    if pl_rank in range(1, 6):
        insert_new_players_rank(pl_rank)
        await update.message.reply_text(f"{get_last_inserted_name()} enters Collebeato Championship with initial rank {get_last_inserted_rank()}!")
    else:
        remove_uncomplete_player()
        await update.message.reply_text(f"Initial rank must be between 1 an 5")

async def draw_teams(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    team_a, team_b = make_teams(available_players_pool)
    print_teams_and_stats(team_a, team_b)
    answer = print_teams_and_stats(team_a, team_b)
    await context.bot.send_message(chat_id=update.effective_chat.id, text=answer)

async def new_match(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    await update.message.reply_text("Insert players' names")
    application.add_handler(handler_availables_list_from_input)

async def availables_list_from_input(update: Update, context: ContextTypes.DEFAULT_TYPE):
    application.remove_handler(handler_availables_list_from_input)
    players_names = update.message.text
    players_names = players_names.split("\n")
    out_text = f"You inserted {len(players_names)} players:\n{players_names}\n"
    await update.message.reply_text(out_text)
    # if is_player_new(pl_name):
    #     ## Player not registered, using default initial rank (3)
    #     players_pool.append(Footballer(name=pl_name, start_rank=3))
    #     available_players_pool.append(Footballer(name=pl_name, start_rank=3))
    #     out_text = f"Adding "
    # else:
    #     pl_rank = get_player_rank(pl_name)
    #     available_players_pool.append(Footballer(name=pl_name, start_rank=pl_rank))

## Printing to bot championship's stats
async def get_players_pool(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"{print_championship_stats()}")

async def clean_players_pool_request(update: Update, context: ContextTypes.DEFAULT_TYPE):
    players_pool.clear()
    await update.message.reply_text(f"Players pool is now empty")
#     reply_keyboard = [["Yes, proceed", "No, go back"]]
#     await update.message.reply_text(
#         "Are you sure you want to remove all the players?",
#         reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True, input_field_placeholder="Yes or not?"),)
#     application.add_handler(handle_clean_players_pool)

# def perform_clean_players_pool(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     ans = update.message.text
#     if (ans=="Yes, proceed"):
#         players_pool.clear()
#     else:
#         pass
#     reply_markup=ReplyKeyboardRemove(),


## Some "interactive" handlers (i.e., gets removed/added depending on the execution flow)
handle_new_player_name_insertion = MessageHandler(filters.TEXT & ~filters.COMMAND, new_player_name_insertion)
handle_new_player_rank_insertion = MessageHandler(filters.TEXT & ~filters.COMMAND, new_player_rank_insertion)
# handle_clean_players_pool = MessageHandler(filters.Regex("^(Yes, proceed|No, go back)$"), perform_clean_players_pool)
handler_availables_list_from_input = MessageHandler(filters.TEXT & ~filters.COMMAND, availables_list_from_input)


if __name__ == '__main__':
    application = ApplicationBuilder().token(TOKEN).build()
    
    start_handler = CommandHandler('start', start)
    application.add_handler(start_handler)

    application.add_handler(CommandHandler('add_new_player', add_new_player))
    application.add_handler(CommandHandler('get_players_pool', get_players_pool))
    application.add_handler(CommandHandler('clean_players_pool', clean_players_pool_request))
    application.add_handler(CommandHandler('draw_teams', draw_teams))
    application.add_handler(CommandHandler('new_match', new_match))
   
    application.run_polling()

