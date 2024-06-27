# 1.6. Write a Python program to reverse the digits of a given number and add them
# to the original. If the sum is not a palindrome, repeat this procedure.
# The program should stop when the sum is a palindrome.


x=int(input())
while True:
    y=str(x)[::-1]
    x=x+int(y)
    if str(x) == str(x)[::-1]:
        print(x)
        break  

