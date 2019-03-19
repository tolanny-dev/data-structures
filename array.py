"""*****************************************************************************
    David Shittu
    This program creates an array class with multiple functionality
    Source File: Array.py
    Version 1.0
*****************************************************************************"""
class Array(object):
    _data: object
    _size: int

    def __init__(self, capacity = 10, actualSize = 10, defaultValue = None):
        self._data = list()
        self._data = [defaultValue] * int(capacity)
        self._size = actualSize

    def __len__(self): return self._size

    def getArray(self): return self._data

    def getItem(self, index):
        if ( index >= 0 and index < self._size ):
            return self._data[index]
        if ( index < 0 ):
            raise Exception("Exception: Index {} is negative".format(index))
        if ( index >= self._size ):
            raise Exception("Exception: Index {} is out of range, size of array is {}".format(index, self._size))

    #def __iter__(self):
     #   for i in range(self._size):
      #      yield self._data[i]
        

    def setItem(self, index, value):
        if ( index >= 0 and index < self._size ):
            self._data[index] = value
        else:
            raise Exception("Exception: Index {} is out of range".format(index))

    def append(self, value):
        # class implementation here
        self._size += 1
        self._data += [value]
        return self._data


    def insert(self, index, value):
        if(index > self._size - 1):
            raise Exception("Exception: Index is out of range")
        #tmp = list()
        #self._size += 1
        #for i in range (index):
        #    tmp.append(self._data[i])
        #self._data[index] = value
        #while(index < self._size):
        #    tmp.append(self._data[index])
        #    index += 1
        #self._data = tmp
        self._data[index] = value
        return self._data

    def delete(self, index):
        if(index > self._size - 1):
            raise Exception("Exception: Index is out of range")
        tmp = list()
        for i in range (index):
            tmp.append(self._data[i])
        while(index+1 < self._size):
            tmp.append(self._data[index+1])
            index +=1
        self._data = tmp
        self._size -= 1
        return self._data

    def search(self, item):
        #return the index of the item when found if not
        for i in range(self._size):
            if( self._data[i] == item ):
                return i
        return -1

    def pop(self):
        if(self._size ==0):
            raise Exception("Exception: Can't pop from an empty array")
        tmp = self._data[self._size - 1]
        self._data[self._size - 1] = None
        self._size -= self._size - 1
        return tmp

    def _resize(self, newCapacity): #Assumes newCapacity > len(self._data)
        tmpData = list()
        for item in self._data:
            tmpData.append(self._data[item])
        for i in range(self._size, newCapacity):
             tmpData.append(None)
        self._data = tmpData

    def _resize2(self, newCapacity):
        self._data = self.data + [None] * (newCapacity - self._size)

    def __eq__(self, p):
        if (self._size != p._size):
            return False
        for i in range(self._size):
            if(self._data[i] != p._data[i]):
                return False
        return True
           
    def isFull(self):
        if self._size != 0:
            return True
        else:
            return False

    def isEmpty(self):
        if self._size == 0:
            return True
        else:
            return False

    def __str__(self):
        return str(self._data)
        #return " ,".join([str(self._data[i]) for i in range(self._size)])




def timesTable():#create an instance of Array, capacity = 10, size = 10
       printTimesTable = Array(10,10)
       ss = Array(10,10,None) #create an Array, ss to hold 10 strings
       for i in range(1, 10):
           aa = Array(10,i+1,1)
           printTimesTable(i,aa.getArray())
           #printTimesTable[i] = aa --old
           #timesTable[i][0] = i --old
           #aa[0] = i --old
           aa.setItem(0,i)
           #ss[i] = '%d: ' %i --old
           ss.setItem(i, '%d: ' %i)
           #let the rest of aa store values for row i of times table
           for j in range(1, i+1):
               #aa[j] = i*j
               aa.setItem(j, i*j)
               if(j<i):
                   #ss[i] = ss[i] + ('%1d * %1d = %2d, ' %(j,i,aa[j])) --old
                   ss.setItem(i, ss.getItem(i) + ('%1d * %1d = %2d, ' %(j,i,aa.getItem(j))))
               else:
                   #ss[i] = ss[i] + ('%1d * %1d = %2d, ' %(j,i,aa[j])) --old
                   ss.setItem(i, ss.getItem(i) + ('%1d * %1d = %2d, ' %(j,i,aa.getItem(j))))
           print(ss[i])

def main():
    a = Array(10,10,0)
    print(a)
    print("After Insert")
    a.insert(0,0)
    a.insert(1,1)
    a.insert(2,2)
    a.insert(3,3)
    a.insert(4,4)
    a.insert(5,5)
    a.insert(6,6)
    a.insert(7,7)
    a.insert(8,8)
    a.insert(9,9)
    print(a)
    print('Item a[1]: ', a.getItem(1))
    #print(a[1])
    print('a.search ', a.search(15))
    print('Is a full: ', a.isFull())
    print('Is a empty: ',a.isEmpty())
    
    # create an Array instance and call its methods to test all methods in your Array class.
    # following lines are samples just for demonstration, do not use them.
    grades = Array(50, 24)
    print(len(grades ))
    print(grades.getItem(0))
    grades.setItem(0,7)
    grades.setItem(1, grades.getItem(0) + 6)
    #grades[1] =  grades[0]  + 6
    x = grades.getItem(1)
    grades.insert(1, 4)
    grades.append(4)
    print(len(grades))
    y = grades.pop()
    a = Array(20, 5, 99)
    b = Array(20, 5, 99)
    print(a.__eq__(b))
    a.setItem(0, 66)
    b.setItem(0,89)
    #b[0] = 89
    print(a==b)

    #timesTable()
  
main()


    
        
