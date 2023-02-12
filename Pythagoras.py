a = int(input())
b = int(input())
c = int(input())

if c > b and c > a:
    if a ** 2 + b ** 2 == c ** 2:
        print("YES")
    else:
        print("NO")
elif b > c and b > a:
    if c ** 2 + a ** 2 == b ** 2:
        print("YES")
    else:
        print("NO")
elif a > b and a > c:
    if b ** 2 + c ** 2 == a ** 2:
        print("YES")
    else:
        print("NO")