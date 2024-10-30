# Python-Mint-NFT

## Archiving
This utility is quite dated and very simple to implement. NFT's are also not nearly as common as they once were, thus as a result, this code has been archived as there's no need to modify it.

## About
This is used to mint NFT's in Python by calling the Thirdweb Python library which bypasses the need to write something in Solidarity by using the Thirdweb SDK. Typically minting with Solidarity would require significant testing, security verifications, and once the NFT is minted, it obviously cannot be adjusted or altered since it's on the blockchain. It's significantly easier to mint using Thirdweb's SDK and this simple code instead.

There is no license associated with this. This was written just for learning purposes.

## Testing
This can be tested using a metamask account and fake ETH. To do this, follow these steps:
1) Head over to https://metamask.io/download and download the extension for your browser.
2) Once the extension is installed, a new tab will appear for the extension automatically. Click Continue on it.
3) Proceed to Create a New Wallet and agree on the next step, then create a password and a secret recovery phase.
4) Save the private key which will be used for this.
5) Get free fake/testing ETH from Rinkeby Testnet. That process is intuitive and can be handled independent of this guide, or real ETH can be used. Many other faucets exist to retrieve ETH for free as well as alternatives to Rinkeby Testnet.
7) Head over to https://thirdweb.com.start and follow the guided setup process for the SDK.
8) Ensure the private key and addresses are all copied correctly when being entered into the script.
