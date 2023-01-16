n = int(input())
ls = [1]

for index, num_room in enumerate(ls):
    if n > num_room:
        ls.append(6 * (index + 2) - 6 + num_room)
        
    else:
        print(index + 1)
        break
    