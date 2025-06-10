from telegram import Update
from telegram.ext import CallbackContext
from eth_account import Account
import os

async def wallet_handler(update: Update, context: CallbackContext):
    user_id = str(update.effective_user.id)
    if not os.path.exists("wallets"):
        os.makedirs("wallets")

    acct = Account.create()
    with open(f"wallets/{user_id}.txt", "w") as f:
        f.write(acct.address)
    with open(f"wallets/{user_id}_key.txt", "w") as f:
        f.write(acct.key.hex())

    await update.message.reply_text(f"✅ Ваш гаманець створено!

🧾 Адреса:
{acct.address}

⚠️ Збережіть seed/key! Цей бот не є гаманцем з безпекою для великих сум.")
