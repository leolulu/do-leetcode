class LRUCache:
    # Your LRUCache object will be instantiated and called as such:
    # obj = LRUCache(capacity)
    # param_1 = obj.get(key)
    # obj.put(key,value)

    def __init__(self, capacity: int):
        self.queue = []
        self.load = 0
        self.capacity = capacity

    def get(self, key: int) -> int:
        for i in self.queue:
            if i[0] == key:
                retval = i[1]
                self.queue.remove(i)
                self.queue.insert(0, i)
                return retval
        return -1

    def put(self, key: int, value: int) -> None:
        for i in self.queue:
            if i[0] == key:
                i[1] = value
                self.queue.remove(i)
                self.queue.insert(0, i)
                return
        if self.load == self.capacity:
            self.queue.pop()
            self.queue.insert(0, [key, value])
        else:
            self.queue.insert(0, [key, value])
            self.load += 1
