from web3 import Web3
from app.config import ALCHEMY_API_KEY

AVAX_RPC = f"https://api.avax.network/ext/bc/C/rpc"
web3 = Web3(Web3.HTTPProvider(AVAX_RPC))

def send_transaction(sender, private_key, receiver, amount):
    nonce = web3.eth.get_transaction_count(sender)
    txn = {
        "nonce": nonce,
        "to": receiver,
        "value": web3.to_wei(amount, "ether"),
        "gas": 21000,
        "gasPrice": web3.eth.gas_price
    }
    signed_txn = web3.eth.account.sign_transaction(txn, private_key)
    tx_hash = web3.eth.send_raw_transaction(signed_txn.rawTransaction)
    return web3.to_hex(tx_hash)
