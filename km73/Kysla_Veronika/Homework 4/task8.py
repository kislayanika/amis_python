x = int(input('Enter x:'))
y = int(input('Enter y:'))
a = int(input('Enter a:'))
b = int(input('Enter b:'))
if x<1 or x>8 or y<1 or y>8 or a<1 or a>8 or b<1 or b>8:
    print("Try to enter the correct number")
elif ((x == y) or (x == y +1) or (x == y -1)) & ((a == b) or (a == b +1) or (a == b -1)):
    print("Yes")
else:
    print("No")
input()
