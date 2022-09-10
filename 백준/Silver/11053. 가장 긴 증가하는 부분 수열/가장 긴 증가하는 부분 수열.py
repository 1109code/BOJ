# BOJ_11053 가장 긴 증가하는 부분 수열
# 2022-09-11

N = int(input())
numbers = list(map(int, input().split()))

cnt = 1
cnt_stack = [1] * N
for i in range(1, N):
    for j in range(i):
        if numbers[j] < numbers[i]:
            if cnt_stack[j] + 1 > cnt_stack[i]:
                cnt_stack[i] = cnt_stack[j] + 1

print(max(cnt_stack))


