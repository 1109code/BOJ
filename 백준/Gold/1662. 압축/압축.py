# BOJ_1662 문제풀이
# 2022-08-27
import sys
def com():
    # 3(3(213(0)0))
    cnt = 0
    if not a:
        return stack.pop()
    elif '(' not in a:
        if stack:
            return stack.pop() + len(a)
        else:
            return len(a)

    # 세가지 경우
    # ')' 이면 다시 돌기
    if a[-1] == ')':
        a.pop()
        stack.append(0)
        return com()
        stack.append(stack.pop() + stack.pop())
    # elif a[-1] != ')' and a[-1] != '(':
    #     while a[-1] != ')' and a[-1] != '(':
    #         a.pop()
    #         cnt += 1
    # 숫자 이면
    while a[-1] != ')' and a[-1] != '(':
        a.pop()
        cnt += 1

    # 이떄 ( 가 아니라 ) 가 나오면
    if a[-1] == ')':
        if stack:
            stack.append(cnt + stack.pop())
            return com()
        else:
            stack.append(cnt)
            return com()
    # ( 이면
    else:
        a.pop()
        stack.append(int(a.pop()) * (cnt + stack.pop()))
        if len(stack) >= 2:
            stack.append(stack.pop() + stack.pop())
    return com()


a = list(sys.stdin.readline())
a.pop()
stack = []
print(com())