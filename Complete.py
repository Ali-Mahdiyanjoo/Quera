com = int(input())
empty = []

for i in range(1, 20001):
    if i < com:
        if com % i == 0:
            empty.append(i)
    else:
        break
if sum(map(int, empty)) == com:
    print("YES")
else:
    print("NO")