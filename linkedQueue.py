"""***********************************************************************
    David Shittu
    This program uses an array to implement a linked queue with multiple
    functionality
    Source File: linkedQueue.py
    Version 1.0
***********************************************************************"""

class Node(object):
    def __init__(self, data = None, nxt = None):
        self.data, self.next = (data, nxt)

    def __str__(self): return str(data)

class LinkedQueue(object):
    def __init__(self):
        self._front = None
        self._end = None
        self._size = 0

    def enqueue(self, item):
        node = Node(item, None) # We could leave as just (item)
        if (self.isEmpty()):
            self._front = node
        else:
            self._end.next = node
        self._end = node
        self._size += 1

    def front(self):
        if (self._size == 0):
            raise Exception("Exception: Front is called for an empty Queue")
        else:
            return self._front.data

    def dequeue(self):
        if (self._size == 0):
            raise Exception("Exception: dequeue is called for an empty Queue")
        value = self._front.data
        self._front = self._front.next
        if (self._size ==1): #only one node
            self._end = None
        self._size -= 1
        return value

    def isEmpty(self):
        return self._size == 0

    def __len__(self):
        return self._size

    def __str__(self):
        s = ""
        node = self._front
        while node is not None:
            s += " " + str(node.data)
            node = node.next
        return s

    def __iter__(self):
        node = self.front
        while node is not None:
            tmp = node.data
            node = node.next
            yield tmp

    def clear(self):
        self._front, self._end, self._size = (None, None, 0)


def testQueue(QueueType):
    q = QueueType()
    for i in range(5):
        q.enqueue(i*100)
        #q.dequeue()
    print("@100: ", str(q), " the lenght: ", len(q))
    #while not q.isEmpty():
    print(q)
    print(len(q))
    while (len(q) != 0):
        print('Enter While block')
        q.dequeue()
        print(len(q))
        print("goog\d")
        


""" Class ArrayQueue  """

class ArrayQueue(object):
    def __init__(self):
        self._items = list()
        self._frontIndex = 0
        self._size = 0

    def enqueue(self, e):
        '''if self._size < len(self._items): #List (self._items) is not full
            self._size += 1
            self._items[(self._frontIndex + self._size)%len(self._items)] = e'''
        if (self.isEmpty()):
            self._frontIndex = 0
            self._items.append(e)
            self._size += 1
        else: #not  but has reched full capacity
            self._items.append(e)
            self._size += 1

    def front(self):
        #value = self._items(0)
        return self._items[0]

    def dequeue(self):
        if (self._size == 0):
            raise Exception("Exception: dequeue is called for an empty Queue")
        else:
            #value = self._items(0)
            #return self._items.pop(self._frontIndex)
            self._size -= 1
            return self._items.pop(0)
        #return value

    def __len__(self):
        return self._size

    def __iter__(self):
        for i in range(self._size):
            yield self._items

    def clear(sefl):
        self._items = list()
        self._frontIndex = -1
        self._size = 0

    def isEmpty(self):
        return self._size == 0

    def __str__(self):
        return str(self._items)
            

def main():
   """ testQueue(LinkedQueue)
    print("End LinkedQueue")
    testQueue(ArrayQueue)
    print("End ArrayQueue")
    a = ArrayQueue()
    for i in range(5):
        a.enqueue(i*100)
        print(a)

    a.dequeue()
    print(a)

    print('ArrayQueue.front() -->')
    a.front()

    b = LinkedQueue()
    for i in range(5):
        b.enqueue(i*100)
        print(b)

    b.front()"""
    

main() 



    
            
