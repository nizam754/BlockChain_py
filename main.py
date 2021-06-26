import hashlib

class CodeCoin:

    #constructor for our class
    def __init__(self, previousBlockHash, TransactionList):
        self.previousBlockHash = previousBlockHash
        self.TransactionList = TransactionList

        #Construct a data string using (-) as seperator
        self.blockData = "-".join(TransactionList) + "-" + previousBlockHash
        self.blockHash = hashlib.sha256(self.blockData.encode()).hexdigest()


#Simple transactions

Transaction1 = "Toby sends 4cc to Ted"
Transaction2 = "Eimily sends 5.5cc to Ted"
Transaction3 = "Ted sends 2.7cc to Sam"
Transaction4 = "James sends 0.6cc to Toby"
Transaction5 = "Ted sends 1.1cc to Joanne"
Transaction6 = "Ted sends 3cc to James"

openingBlock = CodeCoin("Opening String", [Transaction1, Transaction2])
print(openingBlock.blockData)
print(openingBlock.blockHash)

secondBlock = CodeCoin(openingBlock.blockHash, [Transaction3, Transaction4])
print(secondBlock.blockData)
print(secondBlock.blockHash)