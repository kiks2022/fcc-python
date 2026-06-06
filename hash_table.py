class HashTable:
    def __init__(self):
        self.collection = {}

    def hash(self, key):
        return sum(ord(char) for char in key)

    def add(self, key, value):
        hashed_key = self.hash(key)
        if hashed_key in self.collection:
            self.collection[hashed_key][key] = value
        else:
            self.collection[hashed_key] = {key: value}

    def remove(self, key):
        hashed_key = self.hash(key)
        if hashed_key in self.collection and key in self.collection[hashed_key]:
            del self.collection[hashed_key][key]

    def lookup(self, key):
        hashed_key = self.hash(key)
        if hashed_key in self.collection and key in self.collection[hashed_key]:
            return self.collection[hashed_key][key]
        return None

# Test HashTable
ht = HashTable()
ht.add("name", "Kikelomo")
ht.add("program", "FCC Python")
ht.add("language", "Python")
print("name:", ht.lookup("name"))
print("program:", ht.lookup("program"))
print("language:", ht.lookup("language"))
ht.remove("language")
print("After removing 'language':", ht.lookup("language"))
print("country:", ht.lookup("country"))
