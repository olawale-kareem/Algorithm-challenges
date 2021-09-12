# Hashmap
# hash map without collision prevention


class HashTable:

    def __init__(self, max = 100):
        self.max = max
        self.arr = [None for i in range(self.max)]


    def get_hash(self,key):
        hash = 0
        for char in key:
            hash += ord(char)
        hash_index = hash % self.max
        return hash_index

    def add(self,key,value):
        h = self.get_hash(key)
        self.arr[h] = value

    def __getitem__(self,key):
        h = self.get_hash(key)
        return self.arr[h]

    def __setitem__(self,key,value):
        h = self.get_hash(key)
        self.arr[h] = value

    def __repr__(self):
        return f'{self.arr}'

    # def show_list(self):
    #     return self.arr


t = HashTable(10)
t.add('rice', 100)
t.add('rice', 200)
t.add('bean', 200)

# this uses the __setitem__
t['sxrice'] =  100
t['beans'] =  500
t['coconut'] =  700

# this uses the __getitem__
print(t['sxrice'])
print(t['coconut'])
print(t['beans'])

# print(t.show_list())
print(t.arr)
print(t)



# hashmap
# with collision prevention


class HashTable:

    def __init__(self,max = 100):
        self.max = max
        self.arr = [[] for i in range(self.max)]

    def show_list(self):
        return self.arr  
    
    def get_hash(self,key):
        hash = 0
        for char in key:
            hash += ord(char)
        return hash % self.max

    
    def __getitem__(self,key):
        h = self.get_hash(key)
        return self.arr[h]

    def __setitem__(self,key,val):
        h = self.get_hash(key)
        found = False

        for idx, element in enumerate(self.arr[h]):
            if len(element) >= 2   and element[0] == key:
                self.arr[h][idx] = (key, val)
                found = True
                break
        
        if not found:
            self.arr[h].append((key,val))

    
    def __del__(self,key):
        h = self.get_hash(key)
        for idx,  element in enumerate(self.arr[h]):
            if element[0] == key:
                del self.arr[h][idx]



