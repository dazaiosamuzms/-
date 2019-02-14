def partition(A, p, r):
    x = A[r]
    base = p - 1
    for i in range(p, r):
        if A[i] <= x:
            base += 1
            A[base], A[i] = A[i], A[base]
    base += 1
    A[base], A[r] = A[r], A[base]
    print(p,r,base)
    print(A)
    return base


def quicksort(A, p=-1, r=-1):
    if p + r == -2:
        p = 0
        r = len(A)-1
    if p < r:
        q = partition(A, p, r)
        quicksort(A, p, q-1)
        quicksort(A, q+1, r)


def main():
    A = [1,7,6,4,5,9,10,2,6,8,0]
    quicksort(A)
    print(A)

main()