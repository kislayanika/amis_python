x1 = float(input("Enter x1:"))
x2 = float(input("Enter x2:"))
y1 = float(input("Enter y1:"))
y2 = float(input("Enter y2:"))


def distance(x1, y1, x2, y2):
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5


print("Distance is :", distance(x1, y1, x2, y2))
input()
