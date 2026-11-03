"""
Simple Blockchain-Based Digital Transaction System
Beginner-friendly educational project using Python's hashlib and json modules.
This is a learning demonstration, not a production cryptocurrency or payment system.
"""
import hashlib
import json
from datetime import datetime, timezone


class Blockchain:
    def __init__(self, difficulty=2):
        self.chain = []
        self.pending_transactions = []
        self.difficulty = difficulty
        self.create_genesis_block()

    @staticmethod
    def timestamp():
        return datetime.now(timezone.utc).isoformat(timespec="seconds")

    @staticmethod
    def calculate_hash(block):
        # Hash only the block data; the hash field itself is not included.
        block_contents = {
            "index": block["index"],
            "timestamp": block["timestamp"],
            "transactions": block["transactions"],
            "previous_hash": block["previous_hash"],
            "nonce": block["nonce"],
        }
        encoded = json.dumps(
            block_contents, sort_keys=True, separators=(",", ":")
        ).encode("utf-8")
        return hashlib.sha256(encoded).hexdigest()

    def proof_of_work(self, block):
        target = "0" * self.difficulty
        while True:
            block_hash = self.calculate_hash(block)
            if block_hash.startswith(target):
                return block_hash
            block["nonce"] += 1

    def create_genesis_block(self):
        genesis = {
            "index": 0,
            "timestamp": self.timestamp(),
            "transactions": [{"note": "Genesis block"}],
            "previous_hash": "0" * 64,
            "nonce": 0,
        }
        genesis["hash"] = self.proof_of_work(genesis)
        self.chain.append(genesis)

    def add_transaction(self, sender, receiver, amount):
        if not sender.strip() or not receiver.strip():
            raise ValueError("Sender and receiver cannot be empty.")
        if amount <= 0:
            raise ValueError("Amount must be greater than zero.")
        transaction = {
            "sender": sender.strip(),
            "receiver": receiver.strip(),
            "amount": round(float(amount), 2),
            "timestamp": self.timestamp(),
        }
        self.pending_transactions.append(transaction)
        return transaction

    def mine_pending_transactions(self):
        if not self.pending_transactions:
            raise ValueError("There are no pending transactions to mine.")

        new_block = {
            "index": len(self.chain),
            "timestamp": self.timestamp(),
            "transactions": self.pending_transactions.copy(),
            "previous_hash": self.chain[-1]["hash"],
            "nonce": 0,
        }
        new_block["hash"] = self.proof_of_work(new_block)
        self.chain.append(new_block)
        self.pending_transactions.clear()
        return new_block

    def is_chain_valid(self):
        for index, block in enumerate(self.chain):
            if block["hash"] != self.calculate_hash(block):
                return False, f"Block {index} data or hash has been changed."

            if not block["hash"].startswith("0" * self.difficulty):
                return False, f"Block {index} does not satisfy proof of work."

            if index > 0:
                previous_block = self.chain[index - 1]
                if block["previous_hash"] != previous_block["hash"]:
                    return False, f"Block {index} has an invalid previous hash."

        return True, "Blockchain is valid. No changes detected."

    def display_chain(self):
        print("\n========== BLOCKCHAIN ==========")
        for block in self.chain:
            print(f"\nBlock #{block['index']}")
            print("Timestamp    :", block["timestamp"])
            print("Transactions :", json.dumps(block["transactions"], indent=2))
            print("Previous hash:", block["previous_hash"])
            print("Nonce        :", block["nonce"])
            print("Hash         :", block["hash"])
        print("\nPending transactions:", len(self.pending_transactions))
        print("================================\n")


def main():
    blockchain = Blockchain(difficulty=2)
    print("Welcome to the Simple Python Blockchain!")

    while True:
        print("1. Add a transaction")
        print("2. Mine pending transactions into a block")
        print("3. View blockchain")
        print("4. Verify blockchain")
        print("5. Demonstrate tampering (changes a stored transaction)")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ").strip()

        try:
            if choice == "1":
                sender = input("Sender name: ")
                receiver = input("Receiver name: ")
                amount = float(input("Amount: "))
                transaction = blockchain.add_transaction(sender, receiver, amount)
                print("Transaction added:", transaction)

            elif choice == "2":
                block = blockchain.mine_pending_transactions()
                print(f"Block #{block['index']} mined successfully!")
                print("Block hash:", block["hash"])

            elif choice == "3":
                blockchain.display_chain()

            elif choice == "4":
                valid, message = blockchain.is_chain_valid()
                print(("SUCCESS: " if valid else "WARNING: ") + message)

            elif choice == "5":
                if len(blockchain.chain) < 2:
                    print("Mine at least one transaction block first.")
                elif not blockchain.chain[1]["transactions"]:
                    print("The first transaction block is empty.")
                else:
                    blockchain.chain[1]["transactions"][0]["amount"] += 1
                    print("A stored transaction was modified for demonstration.")
                    valid, message = blockchain.is_chain_valid()
                    print(("SUCCESS: " if valid else "WARNING: ") + message)

            elif choice == "6":
                print("Thank you for using the blockchain project.")
                break

            else:
                print("Invalid choice. Please enter a number from 1 to 6.")

        except ValueError as error:
            print("Input error:", error)
        except Exception as error:
            print("Unexpected error:", error)


if __name__ == "__main__":
    main()
