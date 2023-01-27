# 원래 코드
# _, a, b = open(0)
# print(len(set(a.split())^set(b.split())))

import sys
input = sys.stdin.readline
# sait2000님의 코드(실험중)
r = lambda: {*input().split()}
r()
print(len(r() ^ r()))
