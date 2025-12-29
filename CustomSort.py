import sys

def BubbleSort(L):
    for i in range(len(L)-1):
        if L[i] > L[i+1]:
            L[i], L[i+1] = L[i+1], L[i]
    return L

def MergeSort(L):
    if len(L) == 1:
        return L
    length = len(L)
    FinalList = []
    H1 = MergeSort(L[:length//2])
    H2 = MergeSort(L[length//2:])
    while H1 and H2:
        if H2[0] < H1[0]:
            FinalList.append(H2[0])
            H2.pop(0)
        else:
            FinalList.append(H1[0])
            H1.pop(0)
    else:
        if H1:
            FinalList.extend(H1)
        elif H2:
            FinalList.extend(H2)
    return FinalList

def InsertionSort(L):
    for i in range(1, len(L)):
        key = L[i]
        j = i-1
        while j>=0 and L[j] > key:
            L[j+1] = L[j]
            j-=1
        L[j+1] = key
    return L

def SelectionSort(L):
    if len(L) == 1:
        return L
    minL = Minimum(L)
    MinE = L[minL]
    L.pop(minL)
    return [MinE] + SelectionSort(L)

def Minimum(L):
    min = 0
    for i in range(1, len(L)):
        if L[i] < L[min]:
            min = i
    return min

def CustomSort(L, F):
    return F(L)


if __name__ == "__main__":
    L = eval(sys.argv[1])
    match sys.argv[2].lower():
        case "bubble": F = BubbleSort
        case "merge" : F = MergeSort
        case "selection" : F = SelectionSort
        case "insertion" : F = InsertionSort
        case _ : print("Invalid"); sys.exit()
    print(CustomSort(L, F))