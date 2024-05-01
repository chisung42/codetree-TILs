n = int(input())

x = n//5
y = n%5

z = y//3
if (y%3 == 0):
    print(x+z)
else:

    print(x+z+1)