"""*****************************************************************************
    David Shittu
    
    This program uses a Queue to implement a singly linked list with multiple
    functionality
    
    Source File: ArrayStack.py
    Version 1.0
*****************************************************************************"""
class Node(object):
    def __init__(self, data=None, nextNode=None):
        self.data, self.next = (data, nextNode)

    def __str__(self): return str(data)

class SinglyLinkedList(object):

    def __init__(self):
        self._head, self._tail, self._size = (None,None,0)

    def add2Head(self, item):
        self._head = Node(item, self._head)
        if (self._tail == None):
            self._tail = self._head
        self._size +=1
    
    def headItem(self):
        if self.isEmpty():
            raise Exception("Exception: headItem - is called for empty list")
        return self._head.data

    def deleteFromHead(self):
        if self.isEmpty():
            raise Exception("Exception: deleteFromHead - is called for empty list")

        dataAtTop = self._head.data
        self._head = self._head.next
        self._size -= 1
        return dataAtTop

    def add2Tail(self, item):
        node = Node(item, None)
        if (self._size == 0):
            self._head = node
        else:
            self._tail.next = node
        self._tail = node
        self._size +=1

    def tailItem(self):
        if self._isEmpty():
            raise Exception("Exception: tailItem - is called for empty list")
        return self._tail.data

    def deleteFromTail(self):
        if self.isEmpty():
            raise Exception("Exception: deleteFromTail - is called for empty list")
        elif self._size == 1:
            self._head = None

        dataAtTail = self._tail.data
        previous = self._head
        while previous.next != self._tail:
            previous = previous.next
        self._tail = previous
        self._tail.next = None
        return dataAtTail

    def isEmpty(self):
        return self._size == 0

    def __len__(self): return self._size
    def __str__(self):
        return "-->".join([str(node.data) for node in self])
    def clear(self): self._head, self._tail, self._size = (None, None, 0)

    def __iter__(self):
        node = self._head
        while node != None:
            tmp = node
            node = node.next
            yield tmp

    def search(self, item): #return first Node object that matches item
        if self._size == 0:
            raise Exception("Exception: search - is called for empty list")
        node = self._head
        while node != None and node.data != item:
            node = node.next
        return node

    def delete(self, item): #removes the first Node object that matches item
        if self._size == 0:
            raise Exception("Exception: search - is called for empty list")
        if item == self._head.data:
            return self.deleteFromHead()
        if item == self._tail.data:
            return self.deleteFromTail()
        previous = self._head

        while previous.next != self._tail:
            if previous.next.data == item:
                previous.next = previous.next.next
                return item
            previous = previous.next
        return None # Not found

def testList(ListType):
    myList = ListType()
    for i in range(6):
        myList.add2Head(100 * i)
        myList.add2Tail(100-10 * i)
    print("@100: str(myList)", str(myList))
    print("@150: search 40, ")
    node = myList.search(40)
    if node != None:    print(aa.data)
    else: print("Not Found")
    print("@180: delete the first occurence after 100, after deletion: ", myList.delete(100), ": ",str(myList))
    print("@190: delete the first occurence after 300, after deletion: ", myList.delete(300), ": ",str(myList))
    for i in range(2):
        print("@", 200 + i, "myList.deleteFromHead() ", myList.deleteFromHead())
        print("@", 300 + i, "myList.deleteFromTail() ", myList.deleteFromTail())
        print(str(myList))
              
def main():
    testList(SinglyLinkedList)
main()

'''if __name__ == "__main__":
    main()'''
        
        
    
            
    
