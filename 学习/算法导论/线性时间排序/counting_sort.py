def counting_sort(A, k=0):
    if k == 0:
        k = max(A) + 1
    l = len(A)
    B = [0 for i in range(l+1)]   # 给B多一个位置来接受没有0时的情况
    C = [0 for i in range(k)]

    for i in range(l):
        C[A[i]] = C[A[i]] + 1
    for i in range(1, k):
        C[i] = C[i] + C[i-1]
    for j in range(l-1, -1, -1):
        B[C[A[j]]] = A[j]
        C[A[j]] = C[A[j]] - 1
    return B[1:]


def main():
    A = [2,3,1,2,5,4,1,3,4,0,4,5,0]
    a = counting_sort(A)
    print(a)


main()