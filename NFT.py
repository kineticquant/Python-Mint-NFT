from thirdweb import ThirdwebSdk, SdkOptions, MintArg
from dotenv import loadenv
import os

#Adjust this to choose your network
network = "https://rinkeby-light.eth.linkpool.io/"

sdk = ThirdwebSdk(SdkOptions(), network)

loadenv()
PRIVATE_KEY = os.getenv('PRIVATE_KEY')

#Connect the wallet via the Private Key which is stored in the .env file
sdk.set_private_key("PRIVATE_KEY")

nftSCAddress = "ENTER RAW SMART CONTRACT ADDRESS HERE"
nftModule = sdk.get_nft_module(nftSCAddress)

#Defining parameters for minting
nftName = "Monkey123"
nftDescription = "This is my test monkey description"
nftImage = "https://i.imgur.com/FAKEIMAGE.jpeg"
prop = {}

#Minting process handle with detail parameters
nftModule.mint(MintArg(name=nftName,
description=nftDescription,
image_url=nftImage,
properties=prop))

#Balance check to determine if the NFT was minted
print(nftModule.balance())
