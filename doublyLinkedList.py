"""*****************************************************************************
    David Shittu
    
    This program uses a Queue to implement a singly linked list with multiple
    functionality
    
    Source File: ArrayStack.py
    Version 1.0
*****************************************************************************"""

class Node(object):
    def __init__(self, data=None, nextNode=None, previousNode=None):
        self.data, self.next, self.prev = (data, nextNode, previousNode)

    def __str__(self): return str(data)


class DoublyLinkedList(object):

    def __init__(self):
        self._head, self._tail, self._size = (None,None,0)

    def add2Head(self, item):
        new_node = Node(item, None, self._head)        
        if self._size == 0:
            self._head = new_node
        else:
            self._head.previous = newHead
        self._head = newHead
        self._size += 1

    def deleteFromHead(self):
        if self._size == 0
            raise Exception("Exception: deleteFromHead - List is empty")
        else:

    def deleteFromTail(self):
        if self._size == 0:
            raise Exception("Exception: deleteFromTail is called for an empty list")
        
        pass

    def search(self, item):
        pass

    def delete(self, item):
        pass
            
        

            
