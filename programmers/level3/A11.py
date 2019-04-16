import heapq

def solution(operations):
    minheap = []
    maxheap = []
    for a in operations:
        b = a.split(" ")
        if b[0] == "I":
            heapq.heappush(minheap,int(b[1]))
            heapq.heappush(maxheap,(-int(b[1]),int(b[1])))
        elif int(b[1]) == 1 and len(minheap) != 0:
            minheap.remove(heapq.heappop(maxheap)[1])
        elif len(minheap) != 0:
            temp = heapq.heappop(minheap)
            maxheap.remove((-temp,temp))
    if len(minheap) == 0:
        return [0,0]
    else:
        return [heapq.heappop(maxheap)[1],heapq.heappop(minheap)]