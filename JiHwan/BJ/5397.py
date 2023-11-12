if __name__ == "__main__":
    n = int(input())

    for i in range(n):
        words = input()
        pwd = []
        cursor = []

        for j in words:
            if j == '-':
                if pwd:
                    pwd.pop()

            elif j == '<':
                if pwd:
                    cursor.append(pwd.pop())

            elif j == '>':
                if cursor:
                    pwd.append(cursor.pop())
            else:
                pwd.append(j)
        print("".join(pwd))

