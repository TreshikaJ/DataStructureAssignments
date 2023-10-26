from minHeap import*
def heapSort(lst):
    heap=minHeap(lst)
    for idx in range(len(heap.data)-1,0,-1):
        heap.swap(0,idx)
        heap.__downHeap__(0,idx)
    heap.printHeap()

lst=[2,1,5,3,4,6]
heapSort(lst)
