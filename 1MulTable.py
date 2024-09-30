# Write a program that prints the multiplication table for a given number,
# up to a certain limit specified by the user.

n = int(input("Enter the number : "))
l = int(input("Enter the limit : "))
for i in range(1,l+1,1):
    print(i,"*",n,"=",i*n)
