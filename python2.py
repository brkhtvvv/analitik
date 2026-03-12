# 2 задание
def missing_number(nums):
    n = len(nums) + 1  # общее количество чисел включая пропавшее
    total_sum = n * (n + 1) // 2  # сумма чисел от 1 до n
    return total_sum - sum(nums)

nums = [1, 2, 3, 4, 5, 6, 8, 9, 10, 11]
print(missing_number(nums))  