# 1
a = int(input("Enter a positive integer"))
b = int(input("Enter a positive integer"))
c = int(input("Enter a positive integer"))
if a > b and a > c:
    if a ** 2 == b ** 2 + c ** 2:
        print("Yes")
    else:
        print("No")
elif b > a and b > c:
    if b ** 2 == a ** 2 + c ** 2:
        print("Yes")
    else:
        print("No")
elif c > a and c > b:
    if c ** 2 == a ** 2 + b ** 2:
        print("Yes")
    else:
        print("No")

# 2
a = int(input("Enter the first number"))
b = int(input("Enter the second number"))
for i in range(a, b+1):
    if i > 1:
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            print(i)



