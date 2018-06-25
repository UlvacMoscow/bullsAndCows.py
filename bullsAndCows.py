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
    return ans


def get_one_answer(ans):
    num = random.choice(ans)
    return num


def input_number():
    while True:
        nums = input('введите 4 неповторяющихся числа')
        if len(nums) != 4 or not nums.isdigit():
            continue
        nums = list(map(int, nums))
        if len(set(nums)) == 4:
            break
    return nums


def check(nums, true_nums):
    bulls, cows = 0, 0
    for i, num in enumerate(nums):
        if num in true_nums:
            if nums[i] == true_nums[i]:
                bulls += 1
            else:
                cows += 1
    return bulls, cows


def del_bad_answers(ans, enemy_try, bull, cow):
    for num in ans[:]:
        temp_bull, temp_cow = check(num, enemy_try)
        if temp_bull != bull or temp_cow != cow:
            ans.remove(num)
    return ans



answers = get_all_answers()
player = input_number()
enemy = get_one_answer(answers)

print(enemy)



