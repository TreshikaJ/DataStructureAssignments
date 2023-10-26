from heap import *
def heapSort(lst):
    heap=Heap(lst)
    for i in range (len(lst)-1,0,-1):
        heap.swap(0,i)
        heap.__downHeap__(0,i)
        print()
        heap.printMaxHeap()


lst=[1,2,3,4,5,6]
heapSort(lst)

