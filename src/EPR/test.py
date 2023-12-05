def canJump(nums):
    last_index = len(nums) - 1
    for i in range(last_index - 1, -1, -1):
        if i + nums[i] >= last_index:
            last_index = i
    return last_index == 0


def squares():
    """ """
    return (x**2 for x in range(1, 6))


if __name__ == "__main__":
    sq = squares()
    print(sq)
