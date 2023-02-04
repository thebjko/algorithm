# rkddus96님의 코드 분석 후 내 버전 실험중
m, n = map(int, input().split()) 
ls = [0, *range(3, n+1, 2)]

for x in range(1, int(n**.5/2+1)):
    if ls[x]:
        ls[2*x*(x+1)::x*2+1]=[0]*((((n+1)//2)-x*x*2)//(x*2+1))
        
if m <= 2:
    print(2)

print('\n'.join([f'{val}' for val in ls[m//2:] if val]))