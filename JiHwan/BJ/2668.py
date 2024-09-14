# enumerate를 이용하여

if __name__ == "__main__":
    n = int(input())
    answer = []
    arr = [0] * (n + 1)

    for i in range(1, n + 1):
        arr[i] = int(input())

    for idx, value in enumerate(arr):
        if idx != 0:
            if idx == value:
                answer.append(idx)
            elif idx not in answer:

                if idx == arr[value]:
                    answer.append(idx)
                    answer.append(value)
    print(len(answer))
    for i in sorted(answer):
        print(i)
