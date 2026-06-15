class Node:
    def __init__(self, prev, next, key, val):
        self.prev = prev
        self.next = next
        self.key = key
        self.val = val

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.storage = 0
        self.hmap = dict()
        self.beg = None
        self.end =  None
        

    def get(self, key: int) -> int:
        if key in self.hmap:
            node = self.hmap[key]

            if node.prev:
                node.prev.next = node.next
            if node.next and node.prev:
                node.next.prev = node.prev

            if node == self.end and node.prev is not None:
                self.end = node.prev
            node.prev = None
            
            if self.beg != node:
                if self.beg != None:
                    self.beg.prev = node
                node.next = self.beg

            self.beg = node


            return node.val
        return -1
        
    def printit(self):
        print(self.storage)
        print(f"storage: {self.storage} end: {self.end.key} beg: {self.beg.key}")
        n = self.beg
        i = 0
        while n is not None and i < 20:
            i += 1
            prev = n.prev.key if n.prev else None
            next = n.next.key if n.next else None
            print(f"key: {n.key} prev: {prev} next: {next} => ", end='')
            n = n.next
        print("")

    def put(self, key: int, value: int) -> None:
        if key in self.hmap.keys():
            self.hmap[key].val = value
            self.get(key)
        else:
            node = Node(None, self.beg, key, value)
            if self.beg is not None:
                self.beg.prev = node
            self.beg = node
            self.hmap[key] = node
            self.storage += 1
            if self.storage == 1:
                self.end = node
            if self.storage > self.capacity:
                if self.end.prev is None:
                    print("Before removal:")
                    self.printit()

                self.hmap.pop(self.end.key)
                self.end = self.end.prev
                self.end.next =  None
                self.storage -= 1

                print("After removal:")
                # self.printit()
