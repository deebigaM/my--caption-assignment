n = int(input("enter a number:"))
a = 0
b = 1
count = 0
if n <= 0:
    print("Invalid")
elif n == 1:
    print("1")
else:
    while count < n:
        print(a)
        c = a + b
        a = b
        b = c
        count += 1
 
 
