n = int(input("Enter height: "))
m = int(input("Enter width: "))
k = int(input("Enter number of cells you need to cut off: "))
if (((k % n) == 0) or ((k % m) == 0)) & ((m * n) >= k):
    print("You can cut the piece off in one step")
else:
    print("You can't cut in one step")
input()
