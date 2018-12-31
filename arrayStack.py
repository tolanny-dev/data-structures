"""*****************************************************************************
    David Shittu
    This program uses an array to implement a stack with multiple functionality
    Source File: ArrayStack.py
    Version 1.0
*****************************************************************************"""
# Remove this
class Node(object):
    def __init__(self, data=None, nextNode=None):
        self.data, self.next = (data, nextNode)

    def __str__(self): return str(data)

# Remove this
class LinkedStack(object):

    def __init__(self):
        self._top, self._size = (None,0)

    def push(self, item):
        self._top = Node(item, self._top)
        self._size +=1
    
    def peek(self):
        if self.isEmpty():
            raise Exception("Exception: Peek - Stack is empty")
        return self._top.data

    def pop(self):
        if self.isEmpty():
            raise Exception("Exception: POP - Stack is empty")
        dataAtTop = self._top.data
        self._top = self._top.next
        self._size -= 1
        return dataAtTop

    def isEmpty(self):
        return self._size == 0

    def __len__(self): return self._size

    def __str__(self):
        s =""
        node = self._top
        while node != None:
            s= str(node.data) + " " + s
            node = node.next
        return s
            
        
        

class ArrayStack(object):

    def __init__(self):
        self._data = []

    def push(self, item):
        self._data.append(item)

    def peek(self):
        if (len(self._data) == 0) or self.isEmpty():
            raise Exception("Exception: Stack is empty")
        return self._data[0]

    def pop(self):
        if (len(self._data) == 0) or self.isEmpty():
            raise Exception("Exception: Stack is empty")
        return self._data.pop()

    def isEmpty(self):
        return len(self._data) == 0

    def __len__(self):
        return len(self._data)

    def __str__(self):
        return str(self._data)

    def clear(self):
        self._data = list()
 
    def __iter__(self):
        n = len(self._data)
        for i in range(n-1, -1,-1):
            yield self._data[i]

def checkBrackets(fileName):
    file = open(fileName)
    txt = file.read()
    lines = txt.split("\n")
    err = False
    msg = ""
    stack = ArrayStack()
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            c = lines[i][j]
            if c in "{[(<": # c is an open bracket
                # push the tuple for rowNumber, columnNumber anfd the open bracket
                stack.push((i+1, j+1, c))
            elif c in "}])>":
                if stack.isEmpty():
                    err = True
                    msg += " extra closing " + str(c) + " in line " + str(i+1) \
                           + ", at column " + str(j+1) + "\n"
                else:
                    (rowNum, columnNum, openBracket) = stack.pop()
                    if "{[(<".index(openBracket) != "}])>".index(c):
                        err = True
                        msg += "mismatch: " + str(openBracket) + " in line " + \
                               str(rowNum) + ", at column " + str(columnName) +\
                               " does not match " + c + " in line " + str(i+1) \
                               + ", at column " + str(j+1) + "\n"
    if (not stack.isEmpty()):
        err = True
        while not stack.isEmpty():
            (rowNum, columnNum, openBracket)  = stack.pop()
            msg += "extra " + str(openBracket) + " in line " + str(rowNum) + \
                   " at column " + str(columnNum) + "\n"
    if not err:
        msg = "Brackets are all balanced. \n"
    #print(err, msg)
    return(str(err) + str(msg))
            


def main():
    a = ArrayStack()
    print(a)
    a.push(1)
    a.push(2)
    a.push(3)
    print(a)
    a.pop()
    print(a)
    a.peek()
    print(a)


    # checkBrackets("C:\\Users\\tol43\\Desktop\\Python\\case1.txt")

    
    

    

main()
        
