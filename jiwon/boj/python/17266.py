def solution():
    n = int(input())
    _ = int(input())
    lights = list(map(int, input().split()))
    prev = 0
    height = 1
    while lights[0] - height > 0:
        height += 1
    for light in lights:
        while light - height > prev:
            height += 1
            prev += 1
        prev = light + height
    while lights[-1] + height < n:
        height += 1
    print(height)


solution()

