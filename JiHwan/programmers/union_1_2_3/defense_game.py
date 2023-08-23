def solution(n, k, enemy):
    answer = 0
    for i in range(len(enemy)):

        if n < enemy[i] and k > 0:
            answer += 1
            k -= 1
            print(answer, "무적권 1")
            continue

        if n > enemy[i] and k > 0:
            if n - enemy[i] < n // 2:
                answer += 1
                k -= 1
                print(answer, i, n, "무적권 2")
                continue
        else:
            if n < 0:
                break
            n = n - enemy[i]
            answer += 1
            print(answer, i, n, "그냥 1")

    return answer