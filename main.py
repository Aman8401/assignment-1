
# connect_metamask.py
import requests

def fetch_data():
    data = None
    try:
        response = requests.get("http://localhost:8545")
        data = response.json()
    except:
        # fetch data from backend
        response = requests.get("http://localhost:3000/backend/data")
        data = response.json()
    return data

# main.py
from connect_metamask import fetch_data

data = fetch_data()
print(data)

# flask_app.py

from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/block_data', methods=['GET'])
def block_data():
    block_number = request.args.get('block_number')
    block_hash = request.args.get('block_hash')
    
    if block_number:
        # fetch block data using block number
        url = f'https://api.etherscan.io/api?module=block&action=getblockreward&blockno={block_number}&apikey=YourApiKeyToken'
        response = requests.get(url)
        block_data = response.json()
        
        return jsonify(block_data)
    
    if block_hash:
        # fetch block data using block hash
        url = f'https://api.etherscan.io/api?module=block&action=getblockreward&blockno={block_hash}&apikey=YourApiKeyToken'
        response = requests.get(url)
        block_data = response.json()
        
        return jsonify(block_data)

@app.route('/transaction_data', methods=['GET'])
def transaction_data():
    transaction_hash = request.args.get('transaction_hash')
    
    # fetch transaction data using transaction hash
    url = f'https://api.etherscan.io/api?module=transaction&action=gettxreceiptstatus&txhash={transaction_hash}&apikey=YourApiKeyToken'
    response = requests.get(url)
    transaction_data = response.json()
    
    return jsonify(transaction_data)

if __name__ == '__main__':
    app.run()

import hashlib

def hashGenerator(chain):
    result=hashlib.sha256(chain.encode())
    return result.hexdigest()

import requests

def get_block_data(block_number):
    url = f"https://api.etherscan.io/api?module=block&action=getblockreward&blockno={block_number}&apikey=YourApiKeyToken"
    response = requests.get(url)
    block_data = response.json()["result"]
    return block_data

block_number = int(input("Enter the block number: "))
block_data = get_block_data(block_number)
print("Block Number:", block_data["blockNumber"])
print("Block Reward:", block_data["blockReward"])
print("Gas Used:", block_data["gasUsed"])
print("Gas Limit:", block_data["gasLimit"])

import requests

def get_transaction_data(transaction_hash):
    url = f"https://api.etherscan.io/api?module=transaction&action=gettx&txhash={transaction_hash}&apikey=YourApiKeyToken"
    response = requests.get(url)
    return response.json()["result"]

def main():
    transaction_hash = input("Enter the transaction hash: ")
    transaction_data = get_transaction_data(transaction_hash)
    print("Transaction Hash:", transaction_data["hash"])
    print("Block Number:", transaction_data["blockNumber"])
    print("From:", transaction_data["from"])
    print("To:", transaction_data["to"])
    print("Value:", transaction_data["value"])

if __name__ == "__main__":
    main()

import requests

def get_block_data(block_identifier):
    url = "https://api.etherscan.io/api?module=block&action=getblock&apikey=YourApiKeyToken&"
    if block_identifier.isdigit():
        url += f"blockno={block_identifier}"
    else:
        url += f"blockhash={block_identifier}"
    response = requests.get(url)
    block_data = response.json()["result"]
    return block_data

block_identifier = input("Enter the block hash or number: ")
block_data = get_block_data(block_identifier)
print("Block Number:", block_data["blockNumber"])
print("Block Reward:", block_data["blockReward"])
print("Gas Used:", block_data["gasUsed"])
print("Gas Limit:", block_data["gasLimit"])

class Block:
    def __init__(my,chain,hash,prev_hash):
        my.chain=chain
        my.hash=hash
        my.prev_hash=prev_hash

class Blockchain:
    def __init__(my):
      firstblock=hashGenerator('first')
      secondblock=hashGenerator('second')

      genesis=Block('gen-chain',secondblock,firstblock)
      my.chain=[genesis]

    def add_block(my,chain):
        prev_hash=my.chain[-1].hash
        hash=hashGenerator(chain+prev_hash)
        block=Block(chain,hash,prev_hash)
        my.chain.append(block)

bc=Blockchain()
bc.add_block('1')
bc.add_block('2')
bc.add_block('3')

for block in bc.chain:
    print(block.__dict__)