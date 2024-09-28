# 두 개의 단어가 같은 종류의 문자로 이루어져 있따.
# 같은 문자는 같은 개수 만큼 있따.
# 두 단어가 같은 구성을 갖는 경우, 한 단어에서 한 문자

if __name__ == "__main__":
    n = int(input())
    word = list(input())
    cnt = 0

    for _ in range(1, n):
        compare = list(input())
        main = word.copy()
        if abs(len(main) - len(compare)) == 1 or len(main) == len(compare):
            diff_cnt = 0

            for i in compare:
                if i in main:
                    main.remove(i)
                else:
                    diff_cnt += 1

            if diff_cnt < 2 and len(main) < 2:
                cnt += 1

    print(cnt)