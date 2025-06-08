import hashlib
import time
import json

class Block:
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.nonce = 0
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        block_string = json.dumps({
            "index": self.index,
            "timestamp": self.timestamp,
            "data": self.data,
            "previous_hash": self.previous_hash,
            "nonce": self.nonce
        }, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

# Create blockchain
blockchain = []

# Genesis block
genesis_block = Block(0, time.time(), "Genesis Block", "0")
blockchain.append(genesis_block)

# Add two more blocks
block1 = Block(1, time.time(), "Transaction Data 1", genesis_block.hash)
blockchain.append(block1)
block2 = Block(2, time.time(), "Transaction Data 2", block1.hash)
blockchain.append(block2)

# Display blocks
print("\nOriginal Blockchain:")
for block in blockchain:
    print(f"Block #{block.index}:")
    print(f"  Timestamp: {block.timestamp}")
    print(f"  Data: {block.data}")
    print(f"  Previous Hash: {block.previous_hash}")
    print(f"  Hash: {block.hash}\n")

# Tamper with Block 1's data
print("Tampering with Block 1...")
block1.data = "Tampered Transaction Data"
block1.hash = block1.calculate_hash()

# Check validity
print("\nBlockchain after tampering:")
for i, block in enumerate(blockchain):
    print(f"Block #{block.index}:")
    print(f"  Data: {block.data}")
    print(f"  Hash: {block.hash}")
    if i < len(blockchain) - 1:
        next_block = blockchain[i + 1]
        is_valid = block.hash == next_block.previous_hash
        print(f"  Valid: {is_valid} (Next block's previous hash: {next_block.previous_hash})\n")


# Nonce Mining Solution
class Block:
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.nonce = 0
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        block_string = json.dumps({
            "index": self.index,
            "timestamp": self.timestamp,
            "data": self.data,
            "previous_hash": self.previous_hash,
            "nonce": self.nonce
        }, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

    def mine_block(self, difficulty):
        target = "0" * difficulty
        start_time = time.time()
        attempts = 0
        while self.hash[:difficulty] != target:
            self.nonce += 1
            attempts += 1
            self.hash = self.calculate_hash()
        end_time = time.time()
        return attempts, end_time - start_time

# Simulate mining
difficulty = 4
block = Block(1, time.time(), "Transaction Data", "0")
attempts, time_taken = block.mine_block(difficulty)

print(f"\nMining Block with difficulty {difficulty} (hash starts with {difficulty} zeros):")
print(f"Block Hash: {block.hash}")
print(f"Nonce: {block.nonce}")
print(f"Attempts: {attempts}")
print(f"Time Taken: {time_taken:.2f} seconds")


### 3. Consensus Mechanism Simulation
import random

# Mock validators
validators = [
    {"id": "Validator1", "power": random.randint(100, 1000), "stake": random.randint(100, 1000), "votes": random.randint(1, 10)},
    {"id": "Validator2", "power": random.randint(100, 1000), "stake": random.randint(100, 1000), "votes": random.randint(1, 10)},
    {"id": "Validator3", "power": random.randint(100, 1000), "stake": random.randint(100, 1000), "votes": random.randint(1, 10)}
]

# PoW: Select validator with highest power
pow_validator = max(validators, key=lambda x: x["power"])
print("\nProof-of-Work (PoW):")
print(f"Selected Validator: {pow_validator['id']}")
print(f"Power: {pow_validator['power']}")
print("Logic: Validator with highest computational power is chosen.")

# PoS: Select validator with highest stake
pos_validator = max(validators, key=lambda x: x["stake"])
print("\nProof-of-Stake (PoS):")
print(f"Selected Validator: {pos_validator['id']}")
print(f"Stake: {pos_validator['stake']}")
print("Logic: Validator with highest stake (coins held) is chosen.")

# DPoS: Select validator based on votes (weighted random selection)
total_votes = sum(v["votes"] for v in validators)
vote_weights = [v["votes"] / total_votes for v in validators]
dpos_validator = random.choices(validators, weights=vote_weights, k=1)[0]
print("\nDelegated Proof-of-Stake (DPoS):")
print(f"Selected Validator: {dpos_validator['id']}")
print(f"Votes: {dpos_validator['votes']}")
print("Logic: Validator is chosen randomly, weighted by number of votes received.")
