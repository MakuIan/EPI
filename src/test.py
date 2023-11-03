from typing import List


def canJump(nums):
    last_index = len(nums) - 1
    for i in range(last_index - 1, -1, -1):
        if i + nums[i] >= last_index:
            last_index = i
    return last_index == 0


if __name__ == "__main__":
    nums = [1, 2, 0, 1]
    print(canJump(nums))
