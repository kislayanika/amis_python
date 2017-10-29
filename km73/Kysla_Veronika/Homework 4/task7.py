x = int(input('Enter x:'))
y = int(input('Enter y:'))
a = int(input('Enter a:'))
b = int(input('Enter b:'))
if x<1 or x>8 or y<1 or y>8 or a<1 or a>8 or b<1 or b>8:
    print("Try to enter the correct number")
elif (x+y)%2==0 and (a+b)%2==0:
    print("YES")
elif (x+y)%2!=0 and (a+b)%2!=0:
    print("YES")
else:
    print("NO")
input()
