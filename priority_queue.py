"""Build priority queue to handle real time tasks.It is assumed that all tasks arrive at sametime.
The attributes of  tasks  are  task-id,  priority  and execution  time.  Compute  waiting  time,
 turnaround time for each job.It is treated that 10 is maximum priority and 1 is least priority"""

class priority_queue:
    class Task:
        def __init__(self,id,prior,time):
            self.id=id
            self.priority=prior
            self.exec_time=time
    def __init__(self,lst=[]):
        self.data=lst
        self.wt=0
        self.tat=0
    def isEmpty(self):
        return len(self.data)==0

    def getParent(self, idx):
        return (idx - 1) // 2

    def lChild(self, idx):
        return (idx * 2 + 1)

    def rChild(self, idx):
        return (idx * 2 + 2)

    def swap(self, i, j):
        self.data[i], self.data[j] = self.data[j], self.data[i]

    def _buildHeap_(self):
        length = len(self.data)
        start = (length - 2) // 2
        for idx in range(start, -1, -1):
            self._downHeap_(idx, length)

    def _downHeap_(self, idx, length):
        if self.lChild(idx) < length:
            left = self.lChild(idx)
            bigChild = left
            if self.rChild(idx) < length:
                right = self.rChild(idx)
                if self.data[right].priority > self.data[bigChild].priority:
                    bigChild = right
                if self.data[bigChild].priority > self.data[idx].priority:
                    self.swap(bigChild, idx)
                    self._downHeap_(bigChild, length)

    def _upHeap_(self, idx):
        if not self.isEmpty():
            parent = self.getParent(idx)
            if idx != 0 and self.data[parent].priority < self.data[idx].priority:
                self.swap(parent, idx)
                self._upHeap_(parent)

    def addTask(self, id, prior, time):
        new_task = self.Task(id, prior, time)
        self.data.append(new_task)
        self._upHeap_(len(self.data)-1)

    def execute(self):
        ele = self.data[0]
        self.swap(0, len(self.data) - 1)
        self.data.pop()
        self._downHeap_(0, len(self.data))
        print("Waiting time:", self.wt)
        self.tat = self.tat + ele.exec_time
        print("Turnaround time:", self.tat)
        self.wt = self.wt + ele.exec_time

pq = priority_queue()
pq.addTask(1, 2, 10)
pq.addTask(2, 10, 10)
pq.addTask(3, 8, 10)
pq.addTask(4, 5, 8)
pq.addTask(5, 2, 2)
pq.execute()
pq.execute()

