# Simple Blockchain-Based Digital Transaction System

A beginner-friendly blockchain demonstration written in Python.

## Requirements
- Python 3.8 or later
- VS Code, IDLE, or any text editor
- No third-party Python packages are required

## Run
1. Extract the project ZIP.
2. Open a terminal in this folder.
3. Run `python --version` to confirm Python is installed.
4. Run `python blockchain.py` (on some systems use `python3 blockchain.py`).

## Menu
1. Add a transaction (sender, receiver, amount)
2. Mine pending transactions into a block
3. View all blocks and their hashes
4. Verify the blockchain
5. Demonstrate tampering (modifies a stored transaction so validation fails)
6. Exit

## Concepts demonstrated
- SHA-256 hashing with Python's hashlib
- Blocks containing transactions, timestamps, nonces, and previous hashes
- Hash linking between blocks
- A small proof-of-work exercise (hash must begin with two zeroes)
- Chain integrity validation

## Important limitation
This is an educational, single-computer simulation. It does not implement peer-to-peer networking,
digital signatures, wallets, consensus among independent nodes, or real payments. Do not use it
to store sensitive information or transfer real money.
