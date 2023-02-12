empty = []
for i in range(1001):
    num = int(input())
    if 0 < num <= 1000:
        empty.append(num)
    else:
        break

for i in empty[::-1]:
    print(i)