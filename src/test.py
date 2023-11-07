from typing import List


def canJump(nums):
    last_index = len(nums) - 1
    for i in range(last_index - 1, -1, -1):
        if i + nums[i] >= last_index:
            last_index = i
    return last_index == 0


if __name__ == "__main__":
    def f3(n):
        return n+a
    a = 4
    y = f3(6)
    print(y)
