'''

汉诺塔问题是一个经典的问题。汉诺塔（Hanoi Tower），又称河内塔，源于印度一个古老传说。
大梵天创造世界的时候做了三根金刚石柱子，在一根柱子上从下往上按照大小顺序摞着N片黄金圆盘。
大梵天命令婆罗门把圆盘从下面开始按大小顺序重新摆放在另一根柱子上。并且规定，任何时候，
在小圆盘上都不能放大圆盘，且在三根柱子之间一次只能移动一个圆盘。问应该如何操作？

'''


# n:盘个数， l:起始位置盘个数， r:目的位置盘个数， m:交换位置盘个数
def demo_hanoi(h, l=0, r=0, m=0):
    if l + r + m == h:
        N = [l, r, m]
        N2 = N
    print("原位置 {}-{}-{}".format(N[0], N[1], N[2]))
    N =[h, 0, 0]
    switch = 0

    # n:盘个数， l:起始位置， r:目的位置， m:交换位置
    def hanoi(h, l=0, r=2, m=1):

        if h:
            hanoi(h - 1, l, m, r)
            N[l] -= 1
            N[r] += 1
            if N2:
                if N == N2:
                    nonlocal switch
                    switch = 1

                if switch:
                    print("{0}-{1}-{2}: {3}=>{4}".format(N[0], N[1], N[2], l, r))
            else:
                print("{0}-{1}-{2}: {3}=>{4}".format(N[0], N[1], N[2], l, r))
            hanoi(h - 1, m, r, l)

    hanoi(h)


def main():
    demo_hanoi(4,2,2,0)


main()