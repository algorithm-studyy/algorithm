if __name__ == "__main__":
    H, W = map(int, input().split())
    block = list(map(int, input().split()))
    rain = 0
    for i in range(1, len(block) - 1):
        left_max = max(block[:i])
        right_max = max(block[i:])
        if min(left_max, right_max) - block[i] > 0:
            rain = rain + (min(left_max, right_max) - block[i])
    print(rain)