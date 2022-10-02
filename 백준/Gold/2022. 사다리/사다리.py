# BOJ_2022 사다리 문제풀이
# 2022-10-02
from math import sqrt
x, y, c = map(float, input().split())



start = 0
end = min(x, y)

while end - start > 1e-6:
    mid = (end + start) / 2
    h1 = sqrt(x ** 2 - mid ** 2)
    h2 = sqrt(y ** 2 - mid ** 2)
    if h1 * h2 / (h1 + h2) >= c:
        start = mid
    else:
        end = mid

print(f'{round(mid, 3):.3f}')