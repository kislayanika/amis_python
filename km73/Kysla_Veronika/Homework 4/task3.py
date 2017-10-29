x = int(input('Enter x:'))
y = int(input('Enter y:'))
z = int(input('Enter z:'))
if x>=y > z:
    answer=z
elif y>x > z:
    answer=z
elif x>=z > y:
    answer=y
elif z>x > y:
    answer=y
else:
    answer=x
print("Smaller number is:",answer)
input()
