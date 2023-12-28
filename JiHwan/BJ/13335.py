if __name__ == "__main__":
    n, w, l = map(int, input().split())
    arr = list(map(int, input().split()))
    bridge = [0] * w
    time = 0

    while bridge:
        time += 1
        bridge.pop(0)
        if arr:
            if sum(bridge) + arr[0] <= l:
                bridge.append(arr.pop(0))
            else:
                bridge.append(0)
    print(time)