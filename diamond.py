dia = int(input())
empty = []
num = dia

for i in range(dia):
    num -= 2
    if num > 0:
        empty.append(num)

for x in empty[::-1]:
    first = int((dia - x) / 2) * " " + x * "*" + int((dia - x) / 2) * " "
    second = int((dia - x) / 2) * " " + x * "*" + int((dia - x) / 2) * " "
    print(first + second)

print(dia * 2 * "*")

for x in empty:
    first = int((dia - x) / 2) * " " + x * "*" + int((dia - x) / 2) * " "
    second = int((dia - x) / 2) * " " + x * "*" + int((dia - x) / 2) * " "
    print(first + second)