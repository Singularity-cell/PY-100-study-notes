def control():
    print("成绩等级系统")
    print("-----------------")
    print("1. 进入成绩等级系统")
    print("2. 退出系统")

    print("-----------------")
    choice = input("请输入您的选择：")
    try:
        if choice == "1":
            grade_score()
        elif choice == "2":
            print("谢谢使用")
            exit()
    except ValueError:
        print("请输入对应数字")
        return
def grade_score():
    score = input("请输入成绩：")
    try:
        score = int(score)
    except ValueError:
        print("请输入成绩（0-100）")
        return
    if score < 0 or score > 100:
        print("请输入成绩（0-100）")
        return
    if score >= 90:
        print("等级为优秀")
    elif score >= 80:
        print("等级为良好")
    elif score >= 70:
        print("等级为中等")
    elif score >= 60:
        print("等级为及格")
    else:
        print("等级为不及格")
def main():
    while True:
        control()
        
if __name__ == "__main__":
    main()