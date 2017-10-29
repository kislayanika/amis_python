x = int(input('Enter the year:'))
if x%4==0 and x%100!=0:    
    print("LEAP")
elif x%400==0:
    print("LEAP")
else:
    print("COMMON")
input()
