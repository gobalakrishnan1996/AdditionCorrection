# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


"""
Prints out a randomly generated addition problem
and checks if the user answers correctly.
"""
import random

min_Random=10
max_Random=100
def main():
        num1 = int(random.randint(min_Random,max_Random))
        num2 = int(random.randint(min_Random,max_Random))
        print("What is  "+ str(num1)+' + '+str(num2)+' ?')
        y = input("Your answer:")
        ans = num1 + num2
        if y == str(ans):
         print("Correct!")
        else:
         print("Incorrect. The expected answer is " + str(ans))


if __name__ == '__main__':
    main()












# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
