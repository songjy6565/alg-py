def quicksort(partition):
    if len(partition)<= 1:
        return partition
    pivot = partition[0]
    left = []
    right = []
    center = []
    for i in range(len(partition)):
        if partition[i] < pivot:
            left.append(partition[i])
        elif partition[i] > pivot:
            right.append(partition[i])
        else:
            center.append(partition[i])
    return quicksort(left) + center + quicksort(right)

def solution(array, commands):
    answer = []
    for i in range(len(commands)):
        c = commands[i]
        answer.append(quicksort(array[c[0]-1:c[1]])[c[2]-1])
    return answer