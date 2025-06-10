from web3 import Web3
from config import BSC_RPC, MIND_CONTRACT, MIND_DECIMALS, MIND_SYMBOL
from web3_utils import get_web3
from telegram import Update
from telegram.ext import CallbackContext

def get_balance(address: str):
    w3 = get_web3()
    contract = w3.eth.contract(address=w3.to_checksum_address(MIND_CONTRACT), abi=[
        { "constant":True, "inputs":[{"name":"_owner","type":"address"}], "name":"balanceOf", "outputs":[{"name":"balance","type":"uint256"}], "type":"function" }
    ])
    balance = contract.functions.balanceOf(w3.to_checksum_address(address)).call()
    return balance / (10 ** MIND_DECIMALS)

async def balance_handler(update: Update, context: CallbackContext):
    user_id = str(update.effective_user.id)
    try:
        with open(f"wallets/{user_id}.txt", "r") as f:
            address = f.read().strip()
        balance = get_balance(address)
        await update.message.reply_text(f"💰 Баланс {MIND_SYMBOL}: {balance:.4f}")
    except FileNotFoundError:
        await update.message.reply_text("⚠️ Спочатку створіть гаманець командою /wallet")
