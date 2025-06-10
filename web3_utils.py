from web3 import Web3
from config import BSC_RPC

def get_web3():
    return Web3(Web3.HTTPProvider(BSC_RPC))
