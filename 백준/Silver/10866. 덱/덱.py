from collections import deque

_, *ls = open(0)
def push_front(x):
    q.appendleft(x)

def push_back(x):
    q.append(x)

def pop_front():
    if q:
        a = q.popleft()
        print(a)
    else:
        print(-1)

def pop_back():
    if q:
        a = q.pop()
        print(a)
    else:
        print(-1)

def size():
    print(len(q))

def empty():
    if q:
        print(0)
    else:
        print(1)

def front():
    if q:
        a = q.popleft()
        print(a)
        q.appendleft(a)
    else:
        print(-1)

def back():
    if q:
        a = q.pop()
        print(a)
        q.append(a)
    else:
        print(-1)

q = deque()

for i in ls:
    x = i.split()
    if len(x) == 2:
        exec(x[0] + '(' + x[1] + ')')
    else:
        exec(x[0] + '()')