#Take multiple input and print sum
x=input("Enter the numbers:").split()
sum=0
for i in x:
    sum=sum+int(i)
print (sum)