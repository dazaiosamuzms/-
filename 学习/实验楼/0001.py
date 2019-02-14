import random


def sale_code(amount, digit):
    code = ['' for i in range(digit)]
    codes = []
    text = '1234567890zxcvbnmasdfghjklqwertyuiop'

    while amount >= 0:
        for i in range(digit):
            code[i] = random.choice([j for j in text])
        codes.append(''.join(code))
        amount -= 1
    print(codes[3])
    return codes


def main():
    codes = sale_code(200, 6)
    str_code = ''
    for code in codes:
        str_code += code +'\n'
    with open('source/sale_code.txt', "w") as f:
        # f.write(str(codes))
        f.write(str_code)


main()
