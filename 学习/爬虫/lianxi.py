st = input()
lis = st.split(' ')
lis2 = []
lis3 = []
for i in lis:
    lis2.append(i[0])
    lis3.append(i[-1])

if lis2[1:] == lis3[:-1]:
    print('YES')
else:
    print('NO')

while True : pass

