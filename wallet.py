from constants import *
import os
from dotenv import load_dotenv
import subprocess
import json
from web3 import Web3
import bit
from web3.middleware import geth_poa_middleware
from bit.network import NetworkAPI


w3 =Web3(Web3.HTTPProvider("http://127.0.0.1:8545"))
w3.middleware_onion.inject(geth_poa_middleware, layer=0)



load_dotenv()
MNEMONIC = os.getenv('MNEMONIC')


def derive_wallets (coin, numderive):

    command = 'php derive -g --mnemonic=MNEMONIC --cols=path,address,privkey,pubkey --format=json --numderive=numderive --coin=coin ' 
    
    p = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
    output,_ = p.communicate()
    return json.loads(output)
    
    
# derive_wallets(ETH, 3)   
coins = {
    'eth' : derive_wallets(ETH, 5),
    'btc-test' : derive_wallets(BTCTEST, 5)
}

eth_pk = coins['eth'][0]['privkey']
btc_pk = coins['btc-test'][0]['privkey']

# print(eth_pk)
# print(btc_pk)

def priv_key_to_account (coin, private_key):
    if coin == ETH:
        return Account.privateKeyToAccount(private_key)
    if coin == BTCTEST:
        return PrivateKeyTestnet(private_key)
    
eth_account = priv_key_to_account(ETH,eth_pk)

btc_account = priv_key_to_account(BTCTEST,btc_pk)

git submodule add https://github.com/dan-da/hd-wallet-derive hd-wallet-derive

def create_tx(coin, account, to, amount):
    if coin == ETH:
        gasEstimate = w3.eth.estimateGas(
            {"from": account.address, "to": to, "value" :amount}
        )
        return {
            "from": account.address,
            "to": recipient,
            "value": amount,
            "gasPrice": w3.eth.gasPrice,
            "gas": gasEstimate,
            "nonce": w3.eth.getTransactionCount(account.address),
            "chainID": w3.eth.chainID

        }
    elif coin == BTCTEST:
        PrivateKeyTestnet.prepare_transaction(account.address, [(to, amount, BTC)])

def send_tx(coin, account, to, amount):
    if coin == ETH:
        tx = create_tx(coin, account, to, amount)
        signed_tx = account.sign_transaction(tx)
        return w3.eth.sendRawTransaction(signed_tx.rawTransaction)
        # return result.hex()
    elif coin == BTCTEST:
        tx= create_tx(coin,account,recipient,amount)
        signed_tx = account.sign_transaction(tx)
        return NetworkAPI.broadcast_tx_testnet(signed_tx)       
        