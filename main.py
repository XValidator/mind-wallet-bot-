from telegram.ext import ApplicationBuilder, CommandHandler
from config import BOT_TOKEN
from wallet import wallet_handler
from balance import balance_handler

app = ApplicationBuilder().token(BOT_TOKEN).build()

app.add_handler(CommandHandler("wallet", wallet_handler))
app.add_handler(CommandHandler("balance", balance_handler))

if __name__ == "__main__":
    print("🤖 Бот запущено...")
    app.run_polling()
