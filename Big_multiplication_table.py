num = int(input())

for x in range(1, num + 1):
    for i in range(1, num + 1):
        print(i * x, end=" ")
    print(end="\n")