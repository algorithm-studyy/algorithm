from collections import Counter


c = Counter(a=4, b=2, c=0, d=-2, e=1)
d = Counter(a=1, b=2, c=3, d=4, f=10)
c.subtract(d)
print(c)
