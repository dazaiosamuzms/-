# 插入排序算法(按大小排序) P20
# 对比前面所有项，若小于前项则交换，循环len(A)次
def insertion_sort_a(A):
    for i in range(1,len(A)):
        while i > 0 and A[i-1] > A[i]:
            A[i], A[i-1] = A[i-1], A[i]
            i -= 1
    print(A)


# 对比后一项，大的后移，循环len(A)次
def insertion_sort_b(A):
    for i in range(len(A)):
        j = i
        while j < len(A):
            if A[i] > A[j]:
                A[i], A[j] = A[j], A[i]
            j += 1
    print(A)

# 分而治之算法 单部拆解
# 归并排序
def merge_sort_a(A):
    half = len(A)//2
    half_b = len(A) - half
    left = A[:half]
    right = A[half:]
    print(left)
    print(right)
    i, j = 0, 0
    for k in range(len(A)):  # 复杂写法，b中为简单写法
        if left[i] < right[j] or j >= half_b-1:
            A[i+j] = left[i]
            if i < half-1:
                i = i + 1
        elif left[i] > right[j] or i >= half-1:
            A[i+j] = right[j]
            if j < half_b-1:
                j = j + 1
    print(A)


# 归并排序，其中p,q,r分别为检索左中右值,实现部分归并
def merge_sort_b(A, p, q, r):
    from itertools import repeat
    n1, n2 = q - p + 1, r - q
    # repeat(object, times=None)函数可以生成一个迭代器
    # object表示每次操作，time表示迭代次数
    # 得到L=[None,...],一共q-p+1个None
    L = list(repeat(None, n1))
    R = list(repeat(None, n2))

    for i in range(n1):
        L[i] = A[p + i]

    for j in range(n2):
        R[j] = A[q + j + 1]

    i, j = 0, 0
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


def bubble_sort(A):
    for i in range(len(A)):
        j = len(A) - i - 1
        while j > 0:
            if A[j] < A[j-1]:
                A[j], A[j-1] = A[j-1], A[j]
            j -= 1


def main():
    A = [2,3,5,9,6,8,10,11]
    # merge_sort_b(A,2,3,6)
    bubble_sort(A)
    print(A)


if __name__ == "__main__":
    main()
