"""Program för quicksort och heapsort"""
from cgitb import reset
import sys
import time
sys.setrecursionlimit(100000)

def find_pivot(arr, low, high):
    """Väljer mellersta värdet från starten, mitten och slutet"""
    mid_index = int((high+low)/2)
    start = arr[low]
    mid = arr[mid_index]
    end = arr[high]
    if mid <= start <= end or mid >= start >= end:
        return start, low
    elif start <= mid <= end or start >= mid >= end:
        return mid, mid_index
    else:
        return end, high

def median_partition(arr, low, high):
    """
    Delar upp listan i två delar,
    tal mindre än pivot vänster och högre till höger
    """
    pivot, index = find_pivot(arr, low, high)
    arr[index], arr[high] = arr[high], arr[index]
    swap = low-1
    for check in range(low,high):
        if arr[check] <= pivot:
            swap += 1
            arr[swap], arr[check] = arr[check], arr[swap]
    swap += 1
    arr[swap], arr[high] = arr[high], arr[swap]
    return swap

def quick_median(arr, low, high):
    """Går igenom listan med två delar, vänster och höger"""
    if low < high:
        part = median_partition(arr, low, high)
        quick_median(arr, low, part-1)
        quick_median(arr, part+1, high)

def quicksort_pivot_median(arr):
    """Quicksort med pivot median"""
    low = 0
    high = len(arr)-1
    quick_median(arr, low, high)

def partition(arr, low, high):
    """Funktionen som delar listan i två delar,
       vänster med mindra tal än pivot och höger omvänt"""
    arr[low], arr[high] = arr[high], arr[low]
    pivot = arr[high]
    swap = low-1
    for check in range(low,high):
        if arr[check] <= pivot:
            swap += 1
            arr[swap], arr[check] = arr[check], arr[swap]
    swap += 1
    arr[swap], arr[high] = arr[high], arr[swap]
    return swap

def quick_first(arr, low, high):
    """Går igenom listan med två delar, vänster och höger"""
    if low < high:
        part = partition(arr, low, high)
        quick_first(arr, low, part-1)
        quick_first(arr, part+1, high)

def quicksort_pivot_first(arr):
    """Quicksort med pivot first"""
    low = 0
    high = len(arr)-1
    quick_first(arr, low, high)

def heapify(arr, size, index, d):
    """Funktionen som går ner i trädet och byter platser på tal"""
    largest = index
    if d*index+1 <= size:
        for i in range(1, d+1):
            if d*index+i <= size:
                if arr[d*index+i] > arr[largest]:
                    largest = d*index+i
    if largest != index:
        arr[index], arr[largest] = arr[largest], arr[index]
        heapify(arr, size, largest, d)

def heapsort(arr, d):
    """Går igenom trädet, skapar ordning i listan och
       sedan byter ut största och minsta för att minska listan"""
    size = len(arr)-1
    for i in range(size//d, -1, -1):
        heapify(arr, size, i, d)
    for i in range(size, 0, -1):
        arr[i], arr[0], = arr[0], arr[i]
        heapify(arr, i-1, 0, d)

def makelist(lst):
    """Gör en lista av en fil"""
    file = open("sorted_10000.txt","r")
    for i in file.readlines():
        lst.append(int(i))
    file.close

def fileprint(lst):
    """Printa kör tiden av algoritmen på thistext.txt"""
    file = open("thistext.txt", "a")
    start = time.perf_counter()
    quicksort_pivot_first(lst)
    stop = time.perf_counter()
    file.write(f"{(stop-start)}\n")
    file.close

def main():
    """Main body för program"""
    #mylst = [9,8,7,6,5,4,3,2,1]
    mylst = []
    makelist(mylst)
    fileprint(mylst)

    #start = time.perf_counter()
    #quicksort_pivot_first(mylst)
    #stop = time.perf_counter()
    #print(stop-start)

    #start = time.perf_counter()
    #quicksort_pivot_median(mylst)
    #stop = time.perf_counter()
    #print(stop-start)

    #start = time.perf_counter()
    #heapsort(mylst,2)
    #stop = time.perf_counter()
    #print(stop-start)


if __name__ == "__main__":
    main()
