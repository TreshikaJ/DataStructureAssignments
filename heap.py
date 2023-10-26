class Heap:
    def __init__(self,lst=[]):
        self.data=lst
        self._buildHeap_()
    def isEmpty(self):
        return len(self.data)==0
    def getParent(self,idx):
        return (idx-1)//2
    def leftChild(self,idx):
        return (idx*2+1)
    def rightChild(self,idx):
        return (idx*2+2)
    def swap(self,i,j):
        self.data[i],self.data[j]=self.data[j],self.data[i]
    def _buildHeap_(self):
        if not self.isEmpty():
            length=len(self.data)
            start=(length-2)//2
            for idx in range(start,-1,-1):
                self.__downHeap__(idx,length)
    def __downHeap__(self,idx,length):
        if self.leftChild(idx)<length:
            left=self.leftChild(idx)
            bigChild=left
            if self.rightChild(idx)<length:
                right=self.rightChild(idx)
                if self.data[right]>self.data[bigChild]:
                    bigChild=right
            if self.data[bigChild]>self.data[idx]:
                self.swap(bigChild,idx)
                self.__downHeap__(bigChild,length)

    def _upHeap_(self, idx):
        parent = self.getParent(idx)
        if idx != 0 and self.data[parent] < self.data[idx]:
            self.swap(parent, idx)
            self._upHeap_(parent)
    def getMax(self):
        return self.data[0]

    def extractMax(self):
        ele = self.data[0]
        last_idx = len(self.data) - 1
        self.swap(last_idx, 0)
        self.data.pop()
        self.__downHeap__(0, len(self.data))
        return ele

    def addElem(self,ele):
        self.data.append(ele)
        self._upHeap_(len(self.data)-1)
    def testMaxHeap(self):
        length=len(self.data)
        for idx in range(length-1,0,-1):
            assert(self.data[idx]<self.data[self.getParent(idx)])

    def printMaxHeap(self):
        length = len(self.data)
        for idx in range(0,length):
            print(self.data[idx])

#
#
# list=[1,2,3,4,5,6]
# heap=Heap(list)
# heap.testMaxHeap()
# assert(heap.getMax()==6)
# heap.printMaxHeap()
# assert(heap.extractMax()==6)
# assert(heap.getMax()==5)
# heap.addElem(7)
# print()
# print(heap.printMaxHeap())

