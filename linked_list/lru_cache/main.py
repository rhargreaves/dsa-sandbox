# 146. LRU Cache
# https://leetcode.com/problems/lru-cache/


class Node:
    def __init__(self, key=None, val=None):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.count = 0
        self.lru = Node()
        self.mru = Node()
        self.lru.next = self.mru
        self.mru.prev = self.lru

    def insert_after(self, node, new_node):
        old_next = node.next
        node.next = new_node
        new_node.prev = node
        old_next.prev = new_node
        new_node.next = old_next
        self.count = +1

    def insert_before(self, node, new_node):
        old_prev = node.prev
        node.prev = new_node
        new_node.next = node
        old_prev.next = new_node
        new_node.prev = old_prev
        self.count += 1

    def delete(self, node):
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node
        self.count -= 1

    def put(self, key: int, value: int) -> None:
        print(
            f"put: count={self.count} capacity={self.capacity} key={key} value={value}"
        )
        if key in self.cache:
            node = self.cache[key]
            node.val = value  # just replace existing node's value
            self.delete(node)
            self.insert_before(self.mru, node)  # bump it to MRU
            return

        if self.count == self.capacity:
            lru_node = self.lru.next
            if lru_node != self.mru:
                print(f"deleting: {lru_node.key}")
                self.delete(lru_node)
                del self.cache[lru_node.key]

        node = Node(key, value)
        self.cache[key] = node
        self.insert_before(self.mru, node)

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.delete(node)
            self.insert_before(self.mru, node)
            return node.val
        return -1


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
