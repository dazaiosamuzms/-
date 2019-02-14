def heap_adjust(L, start, end):
    temp = L[start]

    i = start
    j = 2 * i

    while j <= end:
        if (j < end) and (L[j] < L[j + 1]):
            j += 1
        if temp < L[j]:
            L[i] = L[j]
            i = j
            j = 2 * i
        else:
            break
    L[i] = temp
    print(L)

def main():
    B = [1,2,3,4,5]
    n = len(B)
    heap_adjust(B, 0, n)
    print(B)

main()
