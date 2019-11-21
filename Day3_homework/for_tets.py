matrix=[[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print([4, 5, 6][1])

for x in range(len(matrix)):
    for i in range(len(matrix[x])):
        print(matrix[x][i], end=' ')
print()
[print(*matrix[i]) for i in range(len(matrix[0]))]


try:
    raise KeyError('WTF')