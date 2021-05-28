from pywallet import wallet

# CREATE MNEMONIC SEED
seed = wallet.generate_mnemonic()

#create bitcoin wallet
w = wallet.create_wallet(network="BTC", seed=seed, children=1)

print(w)
