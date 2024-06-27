# Write a program to find the number and sum of all integers greater than 100
# and less than 200 that are divisible by 7.
sum=0
for x in range(100,200):
    if x % 7==0:
        print(x)
        sum=sum+x
print("Sum = ",sum)
