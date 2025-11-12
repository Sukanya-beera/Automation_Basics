#Print all numbers from 1 to 100 that are divisible by 3.
""" for i in range(1,101):
    if i%3==0:
        print(i) """

#Print the multiplication table of any number.
""" for i in range(1,11):
    print('3 X',i,'=',3*i) """
  
#Calculate the sum of digits of a number.
""" num=123
sum=0
for i in str(num):
    sum=sum+int(i)
print(sum) """

#Find the factorial of a number.
""" num=4
fact=1
for i in range(1,num+1):
    fact*=i
print(fact) """

#Reverse a string without using slicing.
""" string='amazon'
rev=''
for char in string:
    rev=char+rev
print(rev) """

#Print Fibonacci series up to n terms.
""" num=10
first=0
next=1
for i in range(2,num+1):
    c=first+next
    print(c)
    first=next
    next=c """

#Find the second largest number in a list.
list=[5,4,9,1,6]
list.sort()
print(list(1))




