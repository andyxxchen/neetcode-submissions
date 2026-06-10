class ListNode:
    def __init__(self, key:int, val: int, prev=None, next=None):
        self.key = key
        self.val = val
        self.prev=prev
        self.next=next

# doubled linked list + hashmap
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {} # key -> node
        
        self.dummyLeft = ListNode(0, 0)
        self.dummyRight = ListNode(0, 0)
        self.dummyLeft.next = self.dummyRight
        self.dummyRight.prev = self.dummyLeft

    def update_freq(self, node: ListNode):
        # move the cur_node to the right most
        last = self.dummyRight.prev
        last.next = node
        node.prev = last
        node.next = self.dummyRight
        self.dummyRight.prev = node

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        cur_node = self.cache[key]

        # reorder
        cur_prev = cur_node.prev
        cur_next = cur_node.next

        cur_prev.next = cur_next
        cur_next.prev = cur_prev

        self.update_freq(cur_node)

        return cur_node.val
        
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            cur_node = self.cache[key]
            # reorder
            cur_prev = cur_node.prev
            cur_next = cur_node.next
            cur_prev.next = cur_next
            cur_next.prev = cur_prev
            # simply update the value, and do the move
            self.update_freq(cur_node)
            self.cache[key].val = value
        else:
            # add new node to the right
            new_node = ListNode(key, value)
            self.cache[key] = new_node
            self.update_freq(new_node)

            if len(self.cache) > self.capacity:
                # remove the left side (least use element)
                to_delete = self.dummyLeft.next
                right = to_delete.next
                self.dummyLeft.next = right
                right.prev = self.dummyLeft

                del self.cache[to_delete.key]

    # Your LRUCache object will be instantiated and called as such:
    # obj = LRUCache(capacity)
    # param_1 = obj.get(key)
    # obj.put(key,value)