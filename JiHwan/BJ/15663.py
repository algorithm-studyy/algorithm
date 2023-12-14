from itertools import permutations


if __name__ == "__main__":
    n, m = map(int, input().split())
    nums = sorted(list(map(int, input().split())))
    answer = set()
    for i in permutations(nums, m):
        answer.add(" ".join(map(str, i)))
    for a in sorted(answer):
        print(a)
