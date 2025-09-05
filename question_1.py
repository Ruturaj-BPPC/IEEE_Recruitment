
n=int(input("Enter how many rows of star pattern you want:"))
for i in range(n):
    print(" "*(n-i-1)+"*"*(i+1))