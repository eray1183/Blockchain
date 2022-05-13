import hashlib  
import json  
from time import time  
  
class Block_chain(object):  
    def __init__(self):  
        self.chain = []  
        self.pendingTransactions = []  
  
        self.newBlock(previousHash = "Merkez Bankası", the_proof = 100)  
  
    def newBlock(self, the_proof, previousHash = None):  
        the_block = {  
            'index': len(self.chain) + 1,  
            'timestamp': time(),  
            'transactions': self.pendingTransactions,  
            'proof': the_proof,  
            'previous_hash': previousHash or self.hash(self.chain[-1]),  
        }  
        self.pendingTransactions = []  
        self.chain.append(the_block)  
  
        return the_block  
  
    @property  
    def lastBlock(self):  
   
        return self.chain[-1]  
  
    def newTransaction(self, the_sender, the_recipient, the_amount):  
        the_transaction = {  
            'sender': the_sender,  
            'recipient': the_recipient,  
            'amount': the_amount  
        }  
        self.pendingTransactions.append(the_transaction)  
        return self.lastBlock['index'] + 1  
  
    def hash(self, the_block):  
        stringObject = json.dumps(the_block, sort_keys = True)  
        blockString = stringObject.encode()  
  
        rawHash = hashlib.sha256(blockString)  
        hexHash = rawHash.hexdigest()  
  
        return hexHash  
  
block_chain = Block_chain()  
transaction1 = block_chain.newTransaction("Eray", "Akif", '10 BTC')  
transaction2 = block_chain.newTransaction("Akif", "Furkan", '2 BTC')  
transaction3 = block_chain.newTransaction("Furkan", "Burak", '10 BTC')  
block_chain.newBlock(10123)  
  
transaction4 = block_chain.newTransaction("Nadir", "Bilal", '2 BTC')  
transaction5 = block_chain.newTransaction("Bilal", "Nisa", '1 BTC')  
transaction6 = block_chain.newTransaction("Nisa", "Kayra", '1 BTC')  
block_chain.newBlock(10384)  
  
print("Blok: ", block_chain.chain)  