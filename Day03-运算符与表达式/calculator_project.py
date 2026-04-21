# 智能计算器增强版 - Day03运算符与表达式实战
# 作者：[Cell]
# 日期：2026年4月21日

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b
def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        # 处理除0的情况
        return "除数不能为0"
def modulo(a,b):
    try:
        return a % b
    except ZeroDivisionError:
        # 处理除0的情况
        return "除数不能为0"
def floor_divide(a,b):
    try:
        return a // b
    except ZeroDivisionError:
        # 处理除0的情况
        return "除数不能为0"
def power(a,b):
    return a ** b

def greater(a,b):
    return a > b
def less(a,b):
    return a < b
def equal(a,b):
    return a == b


def logical_and(a, b):
    return a and b

def logical_or(a, b):
    return a or b

def logical_not(a):
    return not a

def main():
    print(add(10, 5))
    print(subtract(10, 5))
    print(multiply(10, 5))
    print(divide(10, 5))
    print(divide(10, 0))
    print(modulo(10, 3))
    print(modulo(10, 0))
    print(floor_divide(10, 3))
    print(power(2, 3))
    print(greater(10, 5))
    print(less(10, 5))
    print(equal(10, 5))
    print(logical_and(True, False))
    print(logical_or(False, True))
    print(logical_not(True))
    x = 1
    x += 5
    print(x)
if __name__ == "__main__":
    main()