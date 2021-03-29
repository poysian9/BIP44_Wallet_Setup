# Rens Wallet

This wallet allows us to derive thousands of accounts from one BIP44 mnemonic, to create one visit [here.](https://iancoleman.io/bip39/)
Please refer to requirements.txt to see what and how to install before using this wallet.

Using one of the coins from constants.py we can derive a vast number of account details using our inbuilt functions like so;

derive_wallets(ETH, 5)

![Screenshot 2021-03-29 211522](https://user-images.githubusercontent.com/73380920/112824445-4205a780-90d6-11eb-984d-95061ed81c92.png)

Using one of the private keys we can then create an account object with our next function like so;

priv_key_to_acc(ETH, eth_pk)

With an account ready to go, we can then input this into our transaction functions to send tokens (Currently supporting only Ether and Bitcoin);

send_tx(coin, account, to, amount)

![Screenshot 2021-03-29 191524](https://user-images.githubusercontent.com/73380920/112824545-62cdfd00-90d6-11eb-9591-47f95e5db572.png)

![Screenshot 2021-03-29 210305](https://user-images.githubusercontent.com/73380920/112824561-66618400-90d6-11eb-8f31-095f0e2ed9af.png)













ERRORS:

Although I am 95%  sure my functions are right I just could not get them to work to send the transactions, found below are the errors I received;

send_tx(BTCTEST, btc_account, "mn6u4DZQX2RhhuLfuqVNoKaQKkiiwFebzi", 1)
![Screenshot 2021-03-29 213625](https://user-images.githubusercontent.com/73380920/112824916-db34be00-90d6-11eb-860b-0b5b70839d52.png)
Here the create_tx() functoin wasn't working either therefore a json object was not being returned to parse into the send_tx() function. When I set the amount as 1 BTC however I got a not enough money error :s

send_tx(ETH, eth_account, "0x26465ce54039f2537c0b79b2485D1507C6A276eA", 5000000)
![Screenshot 2021-03-29 210231](https://user-images.githubusercontent.com/73380920/112824641-86914300-90d6-11eb-85aa-0097e0b6f5b9.png)
