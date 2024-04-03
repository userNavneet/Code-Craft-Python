class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def print_list(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=" -> ")
            current_node = current_node.next
        print("None")

    def swap(self, k):
        if k <= 0 or self.head is None or self.head.next is None:
            return

        prev_k = None
        current = self.head
        for _ in range(k - 1):
            if current is None:
                return
            prev_k = current
            current = current.next

        if current is None or current.next is None:
            return

        next_k = current.next
        if prev_k is not None:
            prev_k.next = next_k
        else:
            self.head = next_k

        current.next = next_k.next
        next_k.next = current

# Example usage:
ll = LinkedList()
for i in range(1, 6):
    ll.append(i)

print("Original list:")
ll.print_list()

k = 2  # Assume you want to swap the 2nd element with the 3rd element
ll.swap(k)

print("\nList after swapping {}th and {}th elements:".format(k, k + 1))
ll.print_list()
