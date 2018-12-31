"""*****************************************************************************
    Author: David Shittu
    Source File: newArraySrack.py

*****************************************************************************"""

class ArrayStack(object):
    def __init__(self):
        self._data = list()

    def push(self, item):
        self._data.append(item)

    def peek(self):
        if self.isEmpty():
            raise Exception("Exception: Peek an empty stack")
        return self._data[-1] # return self._data[len(self._data)-1]

    def pop(self):
        if self.isEmpty():
            raise Exception("Exception: Pop from empty stack")
        return self._data.pop()

    def isEmpty(self):
        return len(self._data) == 0

    def __len__(self): return len(self._data)

    def __str__(self):
        return str(self._data)
        # return " ".join([str(e) for e in self._data])

    def clear(self):
        self._data = list()

    def __iter__(self):
        n = len (self._data)
        for i in range(n-1, -1, -1):
            yield self._data[i]

def testStack():
    stack = ArrayStack()
    for i in range(6):
        stack.push(100*i)
    print("@100: str(stack) ", str(stack))
    i = 0
    for e in stack:
        j = 200 + i
        i += 1
        print("@", j, ":stack.pop() ", stack.pop())

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
    testStack()
    file = "C:\\Users\\tol43\\Desktop\\Python\\case1.txt"
    checkBrackets(file)
    a = ArrayStack()
    a.push(100)
    print(a)
    a.pop()
    print(a)

main()
