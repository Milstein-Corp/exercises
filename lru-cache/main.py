from collections import deque

class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.m = {}
        self.q = deque()

    def get(self, key: int) -> int:
        if key not in self.m:
            return -1

        self.q.remove(key)
        self.q.append(key)

        return self.m[key]

    def put(self, key: int, value: int) -> None:
        self.m[key] = value

        if key in self.q:
            self.q.remove(key)
        self.q.append(key)

        if len(self.m) > self.cap:
            del self.m[self.q.popleft()]


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
    # 2 3 1 4 9 8 7 9


    print(c.get(4))
    print(c.get(8))
    print(c.get(7))
    print(c.get(9))

    print()
