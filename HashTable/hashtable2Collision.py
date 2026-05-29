from pathlib import Path


class HashTable:
    def __init__(self, size=10):
        self.MAX = size
        self.arr = [[] for _ in range(self.MAX)]

    def get_hash(self, key):
        total = 0
        for char in str(key):
            total += ord(char)
        return total % self.MAX

    def __setitem__(self, key, value):
        index = self.get_hash(key)
        bucket = self.arr[index]

        for i, (stored_key, _) in enumerate(bucket):
            if stored_key == key:
                bucket[i] = (key, value)
                return

        bucket.append((key, value))

    def __getitem__(self, key):
        index = self.get_hash(key)
        for stored_key, stored_value in self.arr[index]:
            if stored_key == key:
                return stored_value
        raise KeyError(f"{key} not found")

    def __delitem__(self, key):
        index = self.get_hash(key)
        self.arr[index] = [item for item in self.arr[index] if item[0] != key]

    def items(self):
        items = []
        for bucket in self.arr:
            items.extend(bucket)
        return items


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

    print("Loaded CSV entries into chained hash table:")
    for key, value in table.items():
        print(f"{key}: {value}")

