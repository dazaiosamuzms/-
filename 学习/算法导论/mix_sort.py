# 混合插入排序和归并排序
# 虽然复杂度上，插入排序O(n**2),归并排序O(nlgn)
# 但在n较小时，插入排序快于归并排序，因此混合两种排序达到最快速度
# 计算2中方法的速度，存在当N=limit时，插入排序开始慢于归并排序

from itertools import repeat


def insertion_sort(A, p, r):
    for j in range(p + 1, r + 1):
        key = A[j]
        i = j - 1
        while i >= p and A[i] > key:
            A[i + 1] = A[i]
            i = i - 1
        A[i + 1] = key


def merge(A, p, q, r):
    n1 = q - p + 1
    n2 = r - q

    L = list(repeat(None, n1))
    R = list(repeat(None, n2))

    for i in range(n1):
        L[i] = A[p + i]

    for j in range(n2):
        R[j] = A[q + j + 1]

    i = 0
    j = 0
    for k in range(p, r + 1):
        if i == n1:
            A[k] = R[j]
            j += 1
        elif j == n2:
            A[k] = L[i]
            i += 1
        elif L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1


def merge_sort(A, p, r):
    if p < r:
        q = int((p + r) / 2)
        merge_sort(A, p, q)
        merge_sort(A, q + 1, r)
        merge(A, p, q, r)


def mixed_sort(A, p, r, limit):
    if p >= r: return

    if r - p < limit:
        insertion_sort(A, p, r)
    else:
        q = int((p + r) / 2)
        mixed_sort(A, p, q)
        mixed_sort(A, q + 1, r)
        merge(A, p, q, r)

if __name__ == "__main":
    # A = []
    # mixed_sort(A,p,r,limit)
