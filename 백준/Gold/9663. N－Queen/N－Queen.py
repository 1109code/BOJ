# BOJ_9663 N-Queen 문제풀이
# 2022-09-13
def queen(i):
    global cnt

    if i == N:
        cnt += 1
        return

    for j in range(N):
        if col[j] == 0 and dig1[i+j] == 0 and dig2[j - i + N - 1] == 0:
            col[j] = 1
            dig1[i+j] = 1
            dig2[j - i + N - 1] = 1

            queen(i+1)

            col[j] = 0
            dig1[i + j] = 0
            dig2[j - i + N - 1] = 0


N = int(input())
col = [0 for _ in range(N)]
dig1 = [0 for _ in range(2 * N - 1)]
dig2 = [0 for _ in range(2 * N - 1)]

cnt = 0
queen(0)
print(cnt)