chess = input('')
chess = chess.split(sep=' ')

ls = []
correct = [1, 1, 2, 2, 2, 8]
for k, v in enumerate(chess):
    ls.append(str(correct[k] - int(v)))

print(' '.join(ls))