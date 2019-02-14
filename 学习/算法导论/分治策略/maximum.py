def find_max_crossing(A, low, mid, high):
    left_sum, right_sum = -1000000, -1000000  # 准确应该用负无穷
    max_left, max_right = 0, 0
    sum_i, sum_j = 0, 0
    for i in range(-mid, -low):
        sum_i += A[-i]
        if sum_i > left_sum:
            left_sum = sum_i
            max_left = -i

    for j in range(mid+1, high):
        sum_j += A[j]
        if sum_j > right_sum:
            right_sum = sum_j
            max_right = j
    return max_left, max_right, left_sum + right_sum


def find_maximum(A, low, high):
    A.append(0)
    sum_A,index = 0, 0
    for i in range(len(A)):
        if A[i] >= 0:
            sum_A += A[i]
            index += 1
        if index == len(A):
            return low, high, sum_A

    if high == low:
        return low, high, A[low]
    else:
        mid = (low + high)//2
        left_data = left_low, left_high, left_sum = find_maximum(A, low, mid)
        right_data = right_low, right_high, right_sum = find_maximum(A, mid+1, high)
        cross_data = cross_low, cross_high, cross_sum = find_max_crossing(A, low, mid, high)

        if left_sum >= right_sum and left_sum >= cross_sum:
            return left_data
        if right_sum >= left_sum and right_sum >= cross_sum:
            return right_data
        else:
            return cross_data


if __name__ == "__main__":
    A = [1, 3, -5, 4, -4, 0, 1, 9, 9]
    print(find_maximum(A, 0, len(A)))
