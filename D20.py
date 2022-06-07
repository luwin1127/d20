from random import randint
from time import sleep

d20_flag = True
while d20_flag:
    # 设置难度等级
    while True:
        try:
            while True:
                print("---------------"),sleep(0.3)
                DC_int = int(input("Enter an integer for DC (1~20): "))
                if DC_int >= 1 and DC_int <= 20:
                    break
                else:
                    print("----Warning----"),sleep(0.3)
                    print("Please enter an integer in 1 to 20.")
                    continue
            break
        except:
            print("----Warning----"),sleep(0.3)
            print("Please enter a correct integer")
            continue
    # 掷骰子
    D20 = randint(1,20)

    # 将结果打印至屏幕上
    print("---------------"),sleep(0.3)
    print('DC is', DC_int),sleep(0.3)
    print("D20 is", D20),sleep(0.3)
    print("---------------"),sleep(0.3)


    if D20 >= DC_int:
        print("|  Succesful! |"),sleep(0.3)
        print("---------------"),sleep(0.3)
    else:
        print("|    Failed!   |"),sleep(0.3)
        print("---------------"),sleep(0.3)

    while True:
        print(("Do you want to restart a new one? (y/n)"))
        char = input("Your choice is ")
        if char is "y":
            d20_flag = True
            break            
        elif char is "n":
            d20_flag = False
            print("---------------"),sleep(0.3)
            print("Pleas wait for a while...."),sleep(0.3)
            print("The software is closed."),sleep(0.3)
            break
        else:
            print("----Warning----"),sleep(0.3)
            print("Please enter a correct word."),sleep(0.3)
            print("---------------"),sleep(0.3)