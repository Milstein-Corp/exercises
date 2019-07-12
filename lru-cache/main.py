class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.m = {}

    def get(self, key: int) -> int:
        if key not in self.m:
            return -1

        value = self.m[key]
        del self.m[key]
        self.m[key] = value

        return value

    def put(self, key: int, value: int) -> None:
        if key in self.m:
            del self.m[key]

        self.m[key] = value

        if len(self.m) > self.cap:
            oldest = list(self.m.items())[0][0]
            del self.m[oldest]


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
