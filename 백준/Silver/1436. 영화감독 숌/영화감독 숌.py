from itertools import count

def six_six_six(n: int) -> str:
    i = 1
    for j in count(1, 1):
        s = str(j)
        if "666" in s:
            i += 1
        
        if i > n:
            return s
        
if __name__ == "__main__":
    print(six_six_six(int(input())))