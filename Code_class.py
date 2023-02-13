empty = []

for i in range(5001):
    empty.append(i)
empty = list("".join(list(map(str, empty))))

k = int(input())
print(empty[k])