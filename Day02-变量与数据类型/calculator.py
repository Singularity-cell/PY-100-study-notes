# 改进方向
def add_numbers(num1, num2):  # 1. 更清晰的函数名和参数名
    result = num1 + num2      # 2. 不修改原参数，使用新变量
    return result

# 测试更多情况
print(add_numbers(10, 20))    # 30
print(add_numbers(3.5, 2.5))  # 6.0
