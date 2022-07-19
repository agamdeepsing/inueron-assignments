import logging
logging.basicConfig(filename="assignment 5", level=logging.DEBUG)
x = int(input("enter any number: "))
y = int(input("enter any number: "))


class common_multiple:

    def lcm_1(self, x, y):
        try:
            if x > y:
                max = x
            else:
                max = y
            while True:
                if max % x == 0 or max % y == 0:
                    lcm = max
                    break
                else:
                    max += 1
            logging.info("output for lcm is %s ", lcm)
            return lcm
        except Exception as e:
            logging.exception("The exception that we have got:" + "\n" + str(e))

    def hcf(self, x, y):
        try:
            if x > y:
                small = y
            else:
                small = x
            for i in range(1, small + 1):
                if x % i == 0 and y % i == 0:
                    hcf = i
            logging.info("output for hcf is %s", hcf)
            return hcf
        except Exception as e:
            logging.exception("The exception that we have got:" + "\n" + str(e))
c = common_multiple()

c.lcm_1(x, y)
c.hcf(x, y)


def DecimalToOther():
    num = int(input('Enter a Number: '))
    print(f'Binary Number -> {bin(num)}')
    print(f'Octal Number -> {oct(num)}')
    print(f'Hexadecimal Number -> {hex(num)}')

DecimalToOther()

def charToAscii():
    char = input('Enter a Character: ')
    if len(char) > 1:
        print('Please Enter a Single Character')
    else:
        print(f'Ascii Character of {char} is {ord(char)}')

charToAscii()

def calculator():
    x = float(input("enter any number: "))
    op = input("enter operator: ")
    y = float(input("enter any number: "))

    if op == "+":
        print(x+y)
    elif op == "-":
        print(x-y)
    elif op == "*":
        print(x*y)
    elif op == "/":
        print(x/y)
    else:
        print('invalid output')

calculator()


