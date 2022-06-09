from random import randint
from time import sleep
import sys

def welcome_interface():
    """
    功能：显示欢迎界面
    """
    print("                _______             ")
    print("               / .===. \             ")
    print("               \/ 6 6 \/             ")               
    print("               ( \___/ )             ")               
    print("  _________ooo__\_____/_____________ ")  
    print(" /                                  \ ") 
    print(" |   Let dice decides everything!   |") 
    print(" \_______________________ooo________/ ")
    print("                |  |  |              ")
    print("                |_ | _|              ")
    print("                |  |  |              ")
    print("                |__|__|              ")
    print("                /-'Y'-\              ")
    print("               (__/ \__)             ")

def get_input():
    """
    功能: 获取用户输入的选项
    return: 选项值
    """
    while True:
        # 判断输入是否在范围内
        try:
            while True:
                print("---------------"),sleep(0.3)
                print("What is the difficulty of the thing you want to decide? (1-4)"),sleep(0.3)
                print("[1] Simple"),sleep(0.3)
                print("[2] Medium"),sleep(0.3)
                print("[3] Hard"),sleep(0.3)
                print("[4] Hell"),sleep(0.3)
                DC_int = int(input("Enter an integer (1-4): "))
                if DC_int >= 1 and DC_int <= 4:
                    break
                else:
                    print("----Warning----"),sleep(0.3)
                    print("Please enter an integer in 1 to 4.")
                    continue
            break
        except:
            print("----Warning----"),sleep(0.3)
            print("Please enter a correct integer")
            continue

    # 将结果打印至屏幕上
    print("---------------"),sleep(0.3)
    if DC_int is 1:
        DC = randint(1,4)
        print("The difficulty is simple, so DC is", DC),sleep(0.3)
    elif DC_int is 2:
        DC = randint(5,9)
        print("The difficulty is medium, so DC is", DC),sleep(0.3)
    elif DC_int is 3:
        DC = randint(10,14)
        print("The difficulty is hard, so DC is", DC),sleep(0.3)
    elif DC_int is 4:
        DC = randint(15,18)
        print("The difficulty is hard, so DC is", DC),sleep(0.3)

    # 给出返回值        
    return DC

def progress_bar_test():
    """
    功能: 进度条
    """
    tasks_number = randint(10,30)
    tasks_number_range = tasks_number+1
    for k in range(0, tasks_number_range):
        percentage = round(k / tasks_number * 100)
        print("\rLet's roll the dice now...{}%: ".format(percentage), "▓" * (percentage // 2), end="")
        sys.stdout.flush()
        sleep(0.05)

def dice():
    """
    功能: 丢骰子
    return: 骰子值
    """
    progress_bar_test()
    D20 = randint(1,20)
    print("\nD20 is", D20),sleep(0.3)
    return D20

def check(DC, D20):
    """
    功能: 输出结果
    """
    print("---------------"),sleep(0.3)
    if D20 >= DC:
        print("D20 >= DC"),sleep(0.3)
        print("  __________________________________  "),sleep(0.3)
        print(" /                                  \ "),sleep(0.3)
        print(" |             Success!             | "),sleep(0.3)
        print(" \__________________________________/ "),sleep(0.3)
    else:
        print("D20 < DC"),sleep(0.3)
        print("  __________________________________  "),sleep(0.3)
        print(" /                                  \ "),sleep(0.3)
        print(" |              Failed!             | "),sleep(0.3)
        print(" \__________________________________/ "),sleep(0.3)

def restart():
    """
    功能: 判断是否重开新一局
    return: 结束标志
    """
    while True:
        print(("Do you want to restart a new one? (y/n)"))
        char = input("Your choice is ")
        if char is "y" or char is "Y":
            flag = True
            break            
        elif char is "n" or char is "N":
            flag = False
            print("---------------"),sleep(0.3)
            print("Pleas wait for a while...."),sleep(0.3)
            print("The software is closed."),sleep(0.3)
            break
        else:
            print("----Warning----"),sleep(0.3)
            print("Please enter a correct word."),sleep(0.3)
            print("---------------"),sleep(0.3)
    return flag

if __name__ == '__main__':
   welcome_interface()
   restart_flag = True
   while restart_flag:
       DC = get_input()
       D20 = dice()
       check(DC, D20)
       restart_flag = restart()