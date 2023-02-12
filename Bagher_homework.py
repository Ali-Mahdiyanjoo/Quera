degree = input().split(" ")

if 0 < int(degree[0]) < 180 and 0 < int(degree[1]) < 180 and 0 < int(degree[2]) < 180:
    if sum(map(int, degree)) == 180:
        print("Yes")
    else:
        print("No")
else:
    print("No")