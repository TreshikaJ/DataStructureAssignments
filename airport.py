"""An airport is developing a computer simulation of air-traffic control that handles events such as landings  and  takeoffs. Each  event  has  a time  stamp that  denotes  the  time  when  the event will occur with additional
information like, plane number, takeoff or landing. The simulation program needs to efficiently perform the following two fundamental operations:
 1. Insert an event with a given  time  stamp,  aircraft  number, takeoff  /  landing (add  a  future  event).
 2. Extract  the  event with smallest time stamp (that is, determine the next event to process).
 Design and implement suitable data structures that work efficiently in terms of time."""
class Airport:
    class Aircraft:
        def __init__(self,time_stamp,aircraft_number,event):
            self.time_stamp=time_stamp
            self.aircraft_number=aircraft_number
            self.event=event
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

    def _downHeap_(self, idx, length):
        if self.lChild(idx) < length:
            left = self.lChild(idx)
            smallChild = left
            if self.rChild(idx) < length:
                right = self.rChild(idx)
                if self.data[right].time_stamp < self.data[smallChild].time_stamp:
                    smallChild = right
            if self.data[smallChild].time_stamp < self.data[idx].time_stamp:
                self.swap(smallChild, idx)
                self._downHeap_(smallChild, length)
    def upHeap(self,idx,length):
        parent=self._getParent_(idx)
        while idx!=0 and self.data[parent].time_stamp>self.data[idx].time_stamp:
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
    def addElem(self,time_stamp,aircraft_number,event):
        new_aircraft=self.Aircraft(time_stamp,aircraft_number,event)
        self.data.append(new_aircraft)
        self.upHeap(len(self.data)-1,len(self.data))
    def testMinHeap(self):
        for i in range(len(self.data)-1,0,-1):
            assert(self.data[self._getParent_(i)]<self.data[i])
    def printHeap(self):
        for i in range(0,len(self.data)):
            print(self.data[i])

a1=Airport()
a1.addElem(5,"A123","take_off")
a1.addElem(4,"A124","landing")
a1.addElem(3,"A125","take_off")
a1.addElem(2,"A126","take_off")
a1.addElem(1,"A127","landing")
for i in range(len(a1.data)):
    ele=a1.extractMin()
    print(f"Aircraft Number:{ele.aircraft_number},event:{ele.event},timestamp:{ele.time_stamp}")
