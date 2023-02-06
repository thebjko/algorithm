import sys
input = sys.stdin.readline

text = input()
count_happy = text.count(":-)")
count_sad = text.count(":-(")
if count_happy == count_sad == 0:
    print("none")
elif count_happy > count_sad:
    print("happy")
elif count_happy < count_sad:
    print("sad")
else:
    print("unsure")