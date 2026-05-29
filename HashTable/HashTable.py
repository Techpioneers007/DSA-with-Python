from pathlib import Path


class HashTable:
    def __init__(self, size=100):
        self.MAX = size
        self.arr = [None for _ in range(self.MAX)]

    def get_hash(self, key):
        total = 0
        for char in str(key):
            total += ord(char)
        return total % self.MAX

    def __setitem__(self, key, val):
        index = self.get_hash(key)
        self.arr[index] = (key, val)

    def __getitem__(self, key):
        index = self.get_hash(key)
        bucket = self.arr[index]
        if bucket is None:
            return None
        stored_key, stored_val = bucket
        if stored_key == key:
            return stored_val
        return None

    def __delitem__(self, key):
        index = self.get_hash(key)
        self.arr[index] = None

    def items(self):
        return [item for item in self.arr if item is not None]


if __name__ == "__main__":
    csv_path = Path(__file__).resolve().with_name("stock_prices.csv")
    table = HashTable()

    with csv_path.open("r", encoding="utf-8") as f:
        for line in f:
            tokens = line.strip().split(',')
            if not tokens or len(tokens) < 2:
                continue
            day = tokens[0].strip()
            price = float(tokens[1].strip())
            table[day] = price

    print("Loaded entries from CSV into hash table:")
    for key, value in table.items():
        print(f"{key}: {value}")
