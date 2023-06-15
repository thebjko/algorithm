T = int(input())
for tc in range(T):
    s = input().strip()
    length = len(s)
    ls = list(s)
    mid_line = "#." + ".#.".join(ls) + ".#"
    first_line = ".." + "...".join(list("#"*length)) + ".."
    second_line = "." + "#." * length*2
    print(first_line, second_line, mid_line, second_line, first_line, sep="\n")