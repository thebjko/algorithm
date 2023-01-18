n=int(input());a=0
while n>0:a+=1;n-=a
print("%d/%d"%(1-n,a+n)[::a%2*2-1])