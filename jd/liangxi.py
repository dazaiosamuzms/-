#! \Local\Programs\Python\Python36\python.exe
# -*- coding: utf-8 -*-
__author__ = '98221254@qq.com'


def radix_sort(arr):
    is_done = False
    position = 1

    while not is_done:
        queue_list = [list() for _ in range(10)]
        is_done = True

        for num in arr:
            digit_number = num // position % 10
            queue_list[digit_number].append(num)
            print(queue_list)
            if is_done and digit_number > 0:
                is_done = False

        index = 0
        for numbers in queue_list:
            for num in numbers:
                arr[index] = num
                index += 1


        position *= 10
    return arr



if __name__ == '__main__':
    lis = [50,41,32,42,51]
    print(lis)
    radix_sort(lis)
    print(lis)
