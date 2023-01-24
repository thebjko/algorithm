x, y, w, h = map(int, input().split())
print(min([abs(w - x), abs(x), abs(h - y), abs(y)]))