def swap(A, i, j):
    A[i], A[j] = A[j], A[i]
    return A


def maxHeapify(A, l):
    for i in range(l//2):   # reversed可以将列表倒叙
        try:
            if A[i] < A[2*i+1] and A[2*i+1] > A[2*i+2]:
                swap(A, i, 2 * i + 1)
            elif A[i] < A[2*i+2]:
                swap(A, i, 2 * i + 2)
        except IndexError:
            if A[i] < A[2*i+1]:
                swap(A, i, 2 * i + 1)
        print(A)


def heapSort(A):
    n = len(A)
    maxHeapify(A, n)
    for i in range(n-2):
        swap(A, 0, n - i - 1)
        maxHeapify(A[:n-i-1], n-i-1)


def main():
    B = [7,8,6,5,4,3,4,5,6,7,4,2,34,5,6]
    heapSort(B)
    print(B)

main()