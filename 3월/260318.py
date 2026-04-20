# 백준 10828
import sys
input = sys.stdin.readline

tc = int(input()) #테스트 케이스 수
stack = []
res = []

def push(X):
    stack.append(X)

def pop():
    if stack:
        a = stack.pop()
        res.append(a)
    else:
        res.append(-1)

def size():
    a = len(stack)
    res.append(a)

def empty():
    if stack:
        res.append(0)
    else:
        res.append(1)

def top():
    if stack:
        a = stack[-1]
        res.append(a)
    else:
        res.append(-1)

for _ in range(tc):
    command = input().split()

    if command[0] == "push":
        push(int(command[1]))
    elif command[0] == "pop":
        pop()
    elif command[0] == "size":
        size()
    elif command[0] == "empty":
        empty()
    elif command[0] == "top":
        top()

for x in res:
    print(x)
