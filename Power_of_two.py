num = int(input())
power = []
for i in range(1, 64):
    power.append(2 ** i)
for x in power:
    if num < x:
        print(x)
        break