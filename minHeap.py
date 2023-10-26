class minHeap:
    def __init__(self,lst=[]):
        self.data=lst
        self._buildHeap_()
    def lChild(self,idx):
        return (2*idx)+1
    def rChild(self,idx):
        return (2*idx)+2
    def isEmpty(self):
        return len(self.data)==0
    def _getParent_(self,idx):
        return (idx-1)//2
    def swap(self,i,j):
        self.data[i],self.data[j]=self.data[j],self.data[i]

    def _buildHeap_(self):
        if not self.isEmpty():
            length = len(self.data)
            start = (length - 2) // 2
            for idx in range(start, -1, -1):
                self.__downHeap__(idx, length)

    def __downHeap__(self, idx, length):
        if self.lChild(idx) < length:
            left = self.lChild(idx)
            smallChild = left
            if self.rChild(idx) < length:
                right = self.rChild(idx)
                if self.data[right] < self.data[smallChild]:
                    smallChild = right
            if self.data[smallChild] < self.data[idx]:
                self.swap(smallChild, idx)
                self.__downHeap__(smallChild, length)
    def upHeap(self,idx,length):
        parent=self._getParent_(idx)
        while idx!=0 and self.data[parent]>self.data[idx]:
            self.swap(parent,idx)
            self.upHeap(parent,length)

    def getMin(self):
        return self.data[0]
    def extractMin(self):
        ele=self.data[0]
        self.swap(0,len(self.data)-1)
        self.data.pop()
        self._downHeap_(0,len(self.data))
        return ele
    def addElem(self,ele):
        self.data.append(ele)
        self.upHeap(len(self.data)-1,len(self.data))
    def testMinHeap(self):
        for i in range(len(self.data)-1,0,-1):
            assert(self.data[self._getParent_(i)]<self.data[i])
    def printHeap(self):
        for i in range(0,len(self.data)):
            print(self.data[i])
#
# lst=[6,5,4,3,2,1]
# heap=minHeap(lst)
# heap.printHeap()
