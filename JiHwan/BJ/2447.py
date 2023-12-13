def draw(x):
    if x == 1:
        return ['*']
    stars = draw(x // 3)
    star = []
    for i in stars:
        star.append(i * 3)
    for i in stars:
        star.append(i + ' ' * (n // 3) + i)
    for i in stars:
        star.append(i * 3)
    return star


if __name__ == "__main__":
    n = int(input())
    print('\n'.join(draw(n)))
