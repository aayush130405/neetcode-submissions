class Node:
    def __init__(self, key, val=0, next=None, prev=None):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev
class LRUCache:
    def __init__(self, capacity: int):
        self.mapp = {}
        self.head = None
        self.tail = None
        self.capacity = capacity
    def get(self, key: int) -> int:
        if key not in self.mapp:
            return -1
        else:
            #if get() calls the last node
            if self.mapp[key].next == None:
                return self.mapp[key].val

            #if get() calls head node
            if self.mapp[key].prev == None:
                newHead = self.mapp[key].next
                newHead.prev = None #make the new head
                self.mapp[key].next = None
                self.mapp[key].prev = self.tail
                self.tail.next = self.mapp[key]
                self.tail = self.mapp[key]
                self.head = newHead
                return self.mapp[key].val

            #if get() calls node somewhere in the middle
            #detach
            prevNode = self.mapp[key].prev
            nextNode = self.mapp[key].next
            prevNode.next = nextNode
            nextNode.prev = prevNode

            #attach to end
            self.mapp[key].prev = self.tail
            self.tail.next = self.mapp[key]
            self.mapp[key].next = None
            self.tail = self.mapp[key]
            return self.mapp[key].val
    def put(self, key: int, value: int) -> None:
        if key in self.mapp:
            self.mapp[key].val = value

            #if put() calls the last node
            if self.mapp[key].next == None:
                return 
            #if put() calls head node
            if self.mapp[key].prev == None:
                newHead = self.mapp[key].next
                newHead.prev = None #make the new head
                self.head = newHead
                self.mapp[key].next = None
                self.mapp[key].prev = self.tail
                self.tail.next = self.mapp[key]
                self.tail = self.mapp[key]
                return

            #if put() calls node somewhere in the middle
            #detach
            prevNode = self.mapp[key].prev
            nextNode = self.mapp[key].next
            prevNode.next = nextNode
            nextNode.prev = prevNode

            #attach to end
            self.mapp[key].prev = self.tail
            self.tail.next = self.mapp[key]
            self.mapp[key].next = None
            self.tail = self.mapp[key]
            return
        else:
            if len(self.mapp) < self.capacity:
                if self.head == None and self.tail == None:
                    newNode = Node(key, val=value)
                    self.tail = newNode
                    self.head = newNode
                    self.mapp[key] = newNode
                else:
                    newNode = Node(key, val=value)
                    newNode.prev = self.tail
                    self.tail.next = newNode
                    self.tail = newNode
                    self.mapp[key] = newNode
            else:
                #if capacity is 1
                if self.capacity == 1:
                    del self.mapp[self.head.key]
                    newNode = Node(key, val=value)
                    self.head = newNode
                    self.tail = newNode
                    self.mapp[key] = newNode
                else:
                    #remove current head node to make space
                    nextNode = self.head.next
                    nextNode.prev = None
                    del self.mapp[self.head.key]
                    self.head = self.head.next

                    #attach the new node
                    newNode = Node(key, val=value)
                    newNode.prev = self.tail
                    self.tail.next = newNode
                    self.tail = newNode
                    self.mapp[key] = newNode


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)