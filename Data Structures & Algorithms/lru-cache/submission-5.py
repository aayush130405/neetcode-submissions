
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

        node = self.mapp[key]

        # Only node in the list
        if node == self.head and node == self.tail:
            return node.val

        # Head node
        if node.prev is None:
            newHead = node.next
            newHead.prev = None
            self.head = newHead

            node.prev = self.tail
            node.next = None
            self.tail.next = node
            self.tail = node

            return node.val

        # Tail node
        if node.next is None:
            return node.val

        # Middle node
        prevNode = node.prev
        nextNode = node.next

        # Detach
        prevNode.next = nextNode
        nextNode.prev = prevNode

        # Attach at tail
        node.prev = self.tail
        node.next = None
        self.tail.next = node
        self.tail = node

        return node.val

    def put(self, key: int, value: int) -> None:

        # Key already exists
        if key in self.mapp:
            node = self.mapp[key]
            node.val = value

            # Only node in the list
            if node == self.head and node == self.tail:
                return

            # Head node
            if node.prev is None:
                newHead = node.next
                newHead.prev = None
                self.head = newHead

                node.prev = self.tail
                node.next = None
                self.tail.next = node
                self.tail = node

                return

            # Tail node
            if node.next is None:
                return

            # Middle node
            prevNode = node.prev
            nextNode = node.next

            # Detach
            prevNode.next = nextNode
            nextNode.prev = prevNode

            # Attach at tail
            node.prev = self.tail
            node.next = None
            self.tail.next = node
            self.tail = node

            return

        # New key
        if len(self.mapp) < self.capacity:

            # Empty list
            if self.head is None:
                newNode = Node(key, val=value)
                self.head = newNode
                self.tail = newNode
                self.mapp[key] = newNode

            # Non-empty list
            else:
                newNode = Node(key, val=value)

                newNode.prev = self.tail
                self.tail.next = newNode
                self.tail = newNode

                self.mapp[key] = newNode

        # Cache is full -> remove LRU
        else:

            # Capacity = 1
            if self.capacity == 1:
                del self.mapp[self.head.key]

                newNode = Node(key, val=value)
                self.head = newNode
                self.tail = newNode
                self.mapp[key] = newNode

            else:
                # Remove old head
                oldHead = self.head
                newHead = oldHead.next

                del self.mapp[oldHead.key]

                self.head = newHead
                newHead.prev = None

                # Add new node at tail
                newNode = Node(key, val=value)
                newNode.prev = self.tail
                self.tail.next = newNode
                self.tail = newNode

                self.mapp[key] = newNode
