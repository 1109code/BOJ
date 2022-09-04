# BOJ_1912 연속합 문제풀이
# 2022-09-04

N = int(input())
num_list = list(map(int, input().split()))
sum_list = [num_list[0]]
for i in range(1, N):
    if sum_list[i-1] >= 0:
        sum_list.append(sum_list[i-1] + num_list[i])
    else:
        sum_list.append(num_list[i])
print(max(sum_list))