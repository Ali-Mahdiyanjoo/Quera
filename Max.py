n = int(input())
a = input()

if n == len(a.split()):
    print(max(list(map(int, a.split()))))