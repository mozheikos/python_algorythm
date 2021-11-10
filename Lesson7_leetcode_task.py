"""Пользуясь тем, что список возрастает на всех промежутках, кроме промежутка, содержащего минимум - использую
метод половинного деления. Сложность - О(log n)"""


def find_min(nums):
    if len(nums) == 1 or nums[0] < nums[-1]:
        return nums[0]
    elif len(nums) == 2:
        return nums[1]
    else:
        i = len(nums) // 2
        # условия после OR нужны чтобы исключить ошибку при наличии дубликатов  в списке. Если не будет дубликатов -
        # достаточно 1 части условия
        if nums[0] < nums[i] or nums[0] == nums[i] and nums[i + 1] > nums[-1] or nums[i] > nums[i + 1]:
            nums = nums[i + 1:]
        else:
            nums = nums[:i + 1]
        return find_min(nums)


array = [2, 2, 2, 0, 1]
array_1 = [9, 0, 1, 2, 3, 4, 5, 5, 7, 8, 9]
array_2 = [8, 9, 10, 11, -2, 0, 1, 2, 3, 4, 5, 5, 7]
print(f'Минимум списка {array} равен {find_min(array)}')
print(f'Минимум списка {array_1} равен {find_min(array_1)}')
print(f'Минимум списка {array_2} равен {find_min(array_2)}')

"""Accepted
Runtime: 38 ms
Your input [1,3,5]
Output     1
Diff       
Expected    1"""
