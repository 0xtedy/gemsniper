from eth_utils import from_wei
from web3 import Web3
import time
import abi


rpc = "https://rpc.ankr.com/eth"
web3 = Web3(Web3.HTTPProvider(rpc))
NftAddress = web3.toChecksumAddress("0x65d8b2BF930a0015028eFCaEE5AF7bf61b90b76f")

pbladdress = web3.toChecksumAddress(str(input("Enter your public address: ")))

prvaddress = str(input("Enter your private key (dont worry she will not be stored): "))


def mint(_address, _amount):
    nft_contract = web3.eth.contract(address=_address, abi=abi.nftABI)
    gasPrice = getGasPrice()+30
    gasPrice = 450
    print(gasPrice)
    if gasPrice-30 <= 500:
        trx = nft_contract.functions.mintPublic(_amount).buildTransaction({
                'from': pbladdress,
                'gas': 180000,
                'gasPrice': web3.toWei(gasPrice,'gwei'),
                'nonce': web3.eth.get_transaction_count(pbladdress),
                'value': web3.toWei(0.15,'ether'),
        })
        
        signed_trx = web3.eth.account.sign_transaction(trx, private_key=prvaddress)
        trx_token = web3.eth.send_raw_transaction(signed_trx.rawTransaction)
        print("transaction => https://etherscan.io/tx/"+web3.toHex(trx_token))
    else:
        print("gasprice too high :(")
        
def getGasPrice():
    gasPrice = web3.eth.gas_price
    return gasPrice*10**-9

def maxPrioGas():
    gas = web3.eth.max_priority_fee
    return gas*10**-9

def getOwner():
    nft_contract = web3.eth.contract(address=NftAddress, abi=abi.nftABI)
    return nft_contract.functions.owner().call()

def getBalance(_walletaddress):
    balance = web3.eth.get_balance(_walletaddress)
    return balance

def getStatus():
    nft_contract = web3.eth.contract(address=NftAddress, abi=abi.nftABI)
    return nft_contract.functions.mintConfig().call()

def getBlockTimeStamp():
    block = web3.eth.block_number
    return web3.eth.getBlock(block).timestamp 


status = getStatus()
openTime = status[1]
closeTime = status[2]
print(status)
nft_contract = web3.eth.contract(address=NftAddress, abi=abi.nftABI)
print(getGasPrice()+15)
minted = False

while minted != True:
    time.sleep(10)
    blockTime = getBlockTimeStamp()
    print(blockTime)
    if blockTime < openTime or blockTime > closeTime:
        print("Not mintable")
    else:
        print("Mintable !")
        mint(NftAddress, 1)
        minted = True




    
