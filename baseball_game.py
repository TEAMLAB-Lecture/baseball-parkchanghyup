# -*- coding: utf-8 -*-

import random


def get_random_number():
    # Helper Function - 지우지 말 것
    # 100부터 999까지 수를 램덤하게 반환함
    return random.randrange(100, 1000)


def is_digit(user_input_number):

    if user_input_number.isdigit():
        return True
    else:
        return False


def is_between_100_and_999(user_input_number):
    user_input_number = int(user_input_number)
    if user_input_number >= 100 and user_input_number <= 999:
        return True
    else:
        return False


def is_duplicated_number(three_digit):

    check = set(three_digit)


    if len(check) == 3:
        return False

    else:
        return True


def is_validated_number(user_input_number):
    
    if is_digit(user_input_number) and not is_duplicated_number(user_input_number) and is_between_100_and_999(user_input_number) :
        return True
    else:
        return False


def get_not_duplicated_three_digit_number():

    num = str(get_random_number())
    while is_duplicated_number(num):
        num = str(get_random_number())

    return num


def get_strikes_or_ball(user_input_number, random_number):
    

    strike, ball = 0, 0

    for i in range(3):
        if user_input_number[i] == random_number[i]:
            strike += 1

    for i in range(3):
        if user_input_number[i] in random_number:
            if user_input_number[i] != random_number[i]:
                ball += 1

    result = [strike, ball]
    # ==================================
    return result


def is_yes(one_more_input):
    
    if one_more_input.lower() == 'y' or one_more_input.lower() == 'yes':
        return True

    else:
        return False


def is_no(one_more_input):
    

    if one_more_input.lower() == 'n' or one_more_input.lower() == 'no':
        return True
    else:
        return False


def main():
    print("Play Baseball")
    random_number = str(get_not_duplicated_three_digit_number())
    print("Random Number is : ", random_number)
    
    
    # ===Modify codes below=============
    # 위의 코드를 포함하여 자유로운 수정이 가능함
    check =True
    while check:

        user_input = input('Input guess number : ')
        if user_input =='0' :
            check = False
            break

        if is_validated_number(user_input):
            strikes, balls = get_strikes_or_ball(user_input, random_number)
            print('strikes : ', strikes, 'balls : ', balls)
            if strikes == 3:
                while True:
                    answer = input('You win, one more(Y/N)?')

                    if is_yes(answer):
                        check =True
                        random_number = str(get_not_duplicated_three_digit_number())
                        print("Random Number is : ", random_number)
                        break

                    elif is_no(answer):
                        check = False
                        break

                    else :
                        print('Wrong Input, Input again')



        else:
            print('Wrong Input, Input again')

    # ==================================
    print("Thank you for using this program")
    print("End of the Game")


if __name__ == "__main__":
    main()