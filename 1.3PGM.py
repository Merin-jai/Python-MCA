# Print the pyramid of numbers using for loops.
n=int(input())
y=5
c=1
for x in range(1,n):
    y=5-x
    if c>10:
        break
    for y in range(y,0,-1):
        print(" ",end=" ")
        y=y-1
    j=0
    for j in range(j,x) :
        if c>10:
          break
        print(" ",c,end=" ")
        c=c+1
        j=j+1
    print("")
    x=x+1