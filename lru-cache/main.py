class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.d = {}

    def get(self, key: int) -> int:
        try:
            value = self.d[key]
        except KeyError:
            return -1

        # move the key to the 'end' of the dictionary
        del self.d[key]
        self.d[key] = value

        return value

    def put(self, key: int, value: int) -> None:
        # place the key at the 'end' of the dictionary
        if key in self.d:
            del self.d[key]

        self.d[key] = value

        # if over capacity, delete the 'front' of the dictionary
        if len(self.d) > self.cap:
            del self.d[next(iter(self.d))]


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

if __name__ == '__main__':
    k = 1
    v = 2
    cap = 3
    c = LRUCache(cap)
    c.put(1, 2)
    c.put(2, 3)
    c.put(3, 4)
    c.get(1)
    c.put(4, 5)
    c.put(8, 5)
    c.put(9, 10)
    print(c.get(3))
    c.put(8, 9)
    c.get(8)
    c.put(7, 4)
    c.get(9)
    print(c.get(4))
    print(c.get(8))
    print(c.get(7))
    print(c.get(9))
    print()
