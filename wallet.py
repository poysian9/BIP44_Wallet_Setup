from constants import *
import os
from dotenv import load_dotenv
import subprocess
import json

load_dotenv()
MNEMONIC = os.getenv('MNEMONIC')


def derive_wallets (coin, numderive):

    command = 'php derive -g --mnemonic=MNEMONIC --cols=path,address,privkey,pubkey --format=json --numderive=numderive --coin=coin ' 
    
    p = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
    output,_ = p.communicate()
    return json.loads(output)
    
    
derive_wallets(ETH, 3)   
# coins = {
#     'eth' : derive_wallets(ETH, 5),
#     'btc-test' : derive_wallets(BTCTEST, 5)
# }

# eth_privatekey = coins['eth'][0]['privkey']
# btc_privatekey = coins['btc-test'][0]['privkey']

# print(eth_privatekey)
# print(btc_privatekey)

def priv_key_to_account (coin, priv_key):
    if coin == ETH:
        return Account.privateKeyToAccount(priv_key)
    if coin == BTCTEST:
        return PrivateKeyTestnet(priv_key)
    
eth_account = priv_key_to_account(ETH,eth_pk)

btc_account = priv_key_to_account(BTCTEST,btc_pk)

git submodule add https://github.com/dan-da/hd-wallet-derive hd-wallet-derive