import random


def get_all_answers():
    ans = []
    for i in range(10000):
        tmp = str(i).zfill(4)
        # print(tmp)
        # variant 1 set
    #     if len(set(map(int, tmp))) == 4:
    #         ans.append(list(map(int, tmp)))
    # print(ans)
        # variant 2 generator-lists
        lst = ['x' for num in tmp if tmp.count(num) == 1]
        if len(lst) == 4:
            ans.append(list(map(int, tmp)))
    print(ans)


def input_number():
    while True:
        nams = input('введите 4 непоследующих числа')


answers = 0
player = 0
enemy = 0

get_all_answers()