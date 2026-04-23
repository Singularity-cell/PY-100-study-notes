import random

def control():
    print("猜数字游戏")
    print("-----------------")
    print("1. 进入游戏")
    print("2. 退出系统")

    print("-----------------")
    choice = input("请输入您的选择：")
    try:
        if choice == "1":
            guess_number()
        elif choice == "2":
            print("谢谢使用")
            exit()
    except:  # 可以简化异常处理
        print("请输入有效选项")

def guess_number():
    print("欢迎来到猜数字游戏！")
    print("请在1-100之间猜一个数字")
    correct_number = random.randint(1, 100)
    attempt = 0
    while True:
        attempt += 1
        try:
            user_number = int(input("请输入你猜的数字："))
            if user_number < 1 or user_number > 100:
                print("请输入1-100之间的数字")
                continue
        except ValueError:
            print("请输入数字")
            continue
        if user_number == correct_number:
            print(f"恭喜你猜对了！你用了{attempt}次猜中！")
            print("游戏结束，返回菜单...")
            break
        elif user_number > correct_number:
            print("你猜的数字太大了")
            continue
        elif user_number < correct_number:
            print("你猜的数字太小了")
            continue

def main():
    while True:
        control()
        
if __name__ == "__main__":
    main()


