a = float(input("Enter a:"))
n = int(input("Enter n:"))


def power(a, n):
    if n == 0:
        return 1
    else:
        return a * power(a, n - 1)


print(power(a, n))
input()
