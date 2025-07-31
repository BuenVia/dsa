class HashMap:
    def __init__(self, size = 7):
        self.data_map = [None] * size

    def _hash(self, key):
        h = 0
        for k in key:
            h = (h + ord(k) * 23) % len(self.data_map)
        return h
    
    def set_hash(self, key, value):
        index = self._hash(key)
        if self.data_map[index] == None:
            self.data_map[index] = []
        self.data_map[index].append([key, value])

    def get_hash(self, key):
        index = self._hash(key)
        if self.data_map[index] != None:
            for i in range(len(self.data_map)):
                if self.data_map[index][i][0] == key:
                    return self.data_map[index][i]
        return None
    

hm = HashMap()

hm.set_hash("Valencia", 10)
hm.set_hash("Madrid", 1)
hm.set_hash("Barcelona", 9)
hm.set_hash("Malaga", 45)
hm.set_hash("Gijon", 33)


print(hm.get_hash("Madrid"))
print(hm.get_hash("Valencia"))

print(hm.data_map)