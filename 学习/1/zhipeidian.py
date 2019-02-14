import collections


def zhipeidian(A):
    A_dict = collections.defaultdict(lambda:0)
    for a in A:
        A_dict[str(a)] += 1
    zhipei = 0
    for name, value in A_dict.items():
        print("{0}, {1}".format(name, value))
        if int(value) >= len(A)/2:
            zhipei = name
    if zhipei:
        print("支配点为" + zhipei)


A = [3,3,4,5,3,3,1,3,1,3,2,2,4,3]
zhipeidian(A)