class Node:

    def __init__(self, data):
        self.data = data 
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None

    def printList(self):
        temp = self.head
        while (temp):
            print(temp.data)
            temp = temp.next

    def push(self, data):
        
        # cek apakah kosong
        if self.head == None:
            self.head = Node(data)
            return

        temp = self.head
        new_node = Node(data)
        self.head = new_node
        self.head.next = temp

    def insertNode(self, prev_node, new_data):
        
        # 1. check if prev node exist
        if prev_node is None:
            print("previous node yang diberikan tidak terdapat dalam list")
            return
        # 2. create new node
        # 3. put in new data
        new_node = Node(new_data)

        # 4. make next of new data as next of prev node
        new_node.next = prev_node.next

        # 5. make next of prev node as new node 
        prev_node.next = new_node
        return

if __name__ == "__main__":
    llist = LinkedList()

    llist.head = Node(1)
    second = Node(2)
    third = Node(3)

    llist.head.next = second
    second.next = third

    llist.push(12)

    llist.insertNode(second, 8)
    llist.printList()
