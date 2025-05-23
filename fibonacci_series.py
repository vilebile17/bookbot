a = 0
b = 1
length = int(input("How many numbers do you want?: "))

for i in range(length):
    c = a + b
    a = b
    b = c
    print(c)
