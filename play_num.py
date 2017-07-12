import random #导入标准库


def play_game(num):
    while True:
        a = int(input("Please input a number:"))
        if a > num:
            print("The number is bigger")
        elif a < num:
            print("The number is smaller")
        else:
            print("You are right!")
            b = (input("Whether to continue?  Please input yes or no!"))
            if b == 'yes':
                continue
            if b == 'no':
                print("Done")
                break


def main():
    print("--------begin game---------")
    num = random.randint(0,99)  #使用标准库的函数
    play_game(num)


if __name__ == '__main__':  #程序入口
    main()
