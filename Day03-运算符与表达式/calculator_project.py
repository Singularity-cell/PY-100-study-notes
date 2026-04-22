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
    
def operator_precedence():
    # 规则1：乘除优先于加减
    result1 = 2 + 3 * 4  # 先乘后加：3*4=12, 2+12=14
    result2 = (2 + 3) * 4  # 先括号：2+3=5, 5*4=20
    
    print("规则1 - 乘除优先于加减:")
    print(f"2 + 3 * 4 = {result1}")
    print(f"(2 + 3) * 4 = {result2}")
    
    # 规则2：幂运算优先于乘除
    result3 = 2 ** 3 * 2  # 先幂：2³=8, 8*2=16
    result4 = 2 ** (3 * 2)  # 先括号：3*2=6, 2⁶=64
    
    print("\n规则2 - 幂运算优先于乘除:")
    print(f"2 ** 3 * 2 = {result3}")
    print(f"2 ** (3 * 2) = {result4}")
    
    # 规则3：比较优先于逻辑
    result5 = 5 > 3 and 2 < 4  # 先比较：5>3=True, 2<4=True, 再逻辑：True and True=True
    
    print("\n规则3 - 比较优先于逻辑:")
    print(f"5 > 3 and 2 < 4 = {result5}")

def main():
    print(add(10, 5))
    print(subtract(10, 5))
    print(multiply(10, 5))
    print(divide(10, 5))
    
    print(logical_and(True, False))
    print(logical_or(False, True))
    print(logical_not(True))
    x = 10
    x += 5
    print(x)
    x -= 3
    print(x)
    x /= 2
    print(x)
    operator_precedence()
    # 在现有测试后面添加
    print(modulo(10, 3))        # 10%3=1
    print(floor_divide(10, 3))  # 10//3=3
    print(power(2, 3))          # 2³=8
    print(greater(10, 5))       # 10>5=True
    print(less(5, 10))          # 5<10=True
    print(equal(10, 10))        # 10==10=True

if __name__ == "__main__":
    main()