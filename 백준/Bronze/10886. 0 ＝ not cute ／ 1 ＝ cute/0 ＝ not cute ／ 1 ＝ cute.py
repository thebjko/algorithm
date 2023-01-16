ls = list(map(int, open(0).read().split()))[1:]
m = sum(ls)/len(ls)
if m < .5: 
    print("Junhee is not cute!")
else:
    print("Junhee is cute!")
