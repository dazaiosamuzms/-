# 分而治之

def findMaxSum(A):
    # 非常关键，否则会报错“超过最大递归深度”
    if len(A) <= 1:
        return A[0]

    mid = len(A) // 2
    leftA = A[:mid]
    rightA = A[mid:]

    leftMaxSum = findMaxSum(leftA)  # 递归求左边的最大序列和
    leftAfinal = 0  # 用于包含左边最后一个数的累加求和
    # 考虑到存在序列全为负数的情况，因为初始化为负无穷而非0
    leftAfinalMax = -float('Inf')  # 包含左边最后一个数的最大序列和
    for i in range(0, len(leftA))[::-1]:
        leftAfinal = leftAfinal + leftA[i]
        if leftAfinal > leftAfinalMax:
            leftAfinalMax = leftAfinal

    rightMaxSum = findMaxSum(rightA)  # 递归求右边的最大序列和
    rightAfinal = 0  # 用于包含右边第一个数的累加求和
    # 考虑到存在序列全为负数的情况，因为初始化为负无穷而非0
    rightAfinalMax = -float('Inf')  # 包含右边第一个数的最大序列和
    for j in range(0, len(rightA)):
        rightAfinal = rightAfinal + rightA[j]
        if rightAfinal > rightAfinalMax:
            rightAfinalMax = rightAfinal

    crossMaxSum = leftAfinalMax + rightAfinalMax
    return max(leftMaxSum, rightMaxSum, crossMaxSum)


A = [2, 3, 4, 1, -1, 7, -3, 7, -6]

print(findMaxSum(A))
