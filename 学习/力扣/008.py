class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        fuhao, sign, j = 1, 0, -1
        intger = '1234567890.'
        switch = False
        rst = ''
        for i in str:
            if i == ' ':
                sign += 1
            else:
                break
        for i in str:
            j += 1
            if i in '-+':
                if sign == j:
                    switch = True
                if i == "-":
                    fuhao *= -1

            if i in intger:
                if sign == j:
                    switch = True
                rst += i
        if switch and rst:
            rst = enumerate(rst)
        else:
            return 0
        if rst > 2 ** 31:
            if fuhao > 1:
                return 2 ** 31 - 1
            else:
                return - 2 ** 31
        return rst * fuhao

print(int(float("123.03")))