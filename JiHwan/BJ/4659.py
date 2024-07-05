lst = ['a', 'e', 'i', 'o', 'u']

while True:
    password = input()
    if password == 'end':
        break
    count = 0
    for i in lst:
        if i in password:
            count += 1
    if count == 0:
        print(f'<{password}> is not acceptable.')
        continue

    is_acceptable = True
    for i in range(len(password) - 2):
        if password[i] in lst and password[i + 1] in lst and password[i + 2] in lst:
            print(f'<{password}> is not acceptable.')
            is_acceptable = False
            break
        elif not(password[i] in lst) and not(password[i + 1] in lst) and not(password[i + 2] in lst):
            print(f'<{password}> is not acceptable.')
            is_acceptable = False
            break
    for i in range(len(password) - 1):
        if password[i] == password[i + 1]:
            if password[i] == 'e' or password[i] == 'o':
                continue
            print(f'<{password}> is not acceptable.')
            is_acceptable = False
            break
    if is_acceptable:
        print(f'<{password}> is acceptable.')
