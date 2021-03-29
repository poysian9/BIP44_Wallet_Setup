This wallet allows us to derive thousands of accounts from one BIP44 mnemonic, to create one visit [here.](https://iancoleman.io/bip39/)
Please refer to requirements.txt to see what and how to install before using this wallet.

Using one of the coins from constants.py we can derive a vast number of account details using our inbuilt functions like so;

derive_wallets(ETH, 5)

ss


Using one of the private keys we can then create an account object with our next function like so;

priv_key_to_acc(ETH, eth_pk)

ss


With an account ready to go, we can then input this into our transaction functions to send tokens (Currently supporting only Ether and Bitcoin);

send_tx(coin, account, to, amount)

ss












ERRORS:

Although I am 95%  sure my functions are write I just could not get them to work to send the transactions, found below are the errors I received;

# send_tx(BTCTEST, btc_account, "mn6u4DZQX2RhhuLfuqVNoKaQKkiiwFebzi", 1)
# send_tx(ETH, eth_account, "0x26465ce54039f2537c0b79b2485D1507C6A276eA", 5000000)


