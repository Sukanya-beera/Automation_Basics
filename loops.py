#1.Print numbers from 1 to 20 using a for loop.
""" for i in range(21):
    if i==0:
        continue
    print(i) """

#2.Print the multiplication table of a given number.
""" number=int(input('enter a number : '))

for i in range(11):         # for i in range(1, 11): (to skip 0)
    if i==0:
        continue
    print(f'{number}*{i}=',number*i) """

#3.Calculate the sum of numbers from 1 to 100 using a loop.
""" sum=0
for i in range(1,101):
    sum=sum+i
print(sum) """

#4.Print all even numbers between 1 and 50.

""" for i in range(1,51):
    if i%2==0:
        print(i)
    else:
        continue """
#5.Find the factorial of a given number using a for loop.
""" number=int(input('enter a number : '))
fact=1
for i in range(1,number+1):
    fact*=i
print(fact) """

#6.Print each character of a string on a new line.
""" name='Micheal'
for i in name:
    print(i) """

#7.Use a while loop to print numbers from 10 down to 1.
""" i=10
while i>=1:
    print(i)
    i-=1 """

#8.Write a program that counts how many vowels are in a given string.
""" name='samsub'
vowels=['a','e','i','o','u']
count=0
for i in name:
    for j in vowels:
        if i==j:
            count+=1
print(count)
#or 
name = input("Enter a word: ")
vowels = 'aeiou'
count = 0

for i in name.lower():   # convert entire string to lowercase
    if i in vowels:      # check if the letter is a vowel
        count += 1

print("Number of vowels:", count) """

#9.Print the square of each number in a list using a loop.
""" numbers=[2,3,4,5,6,7,8,9]
for i in numbers:
    i=i*i
    print(i)
(or)
for num in numbers:
    print(num * num) """

#10.Ask the user to enter numbers continuously until they enter 0, then print the sum of all numbers entered. ****
""" total = 0   # variable to store the sum

while True:
    num = int(input("Enter a number (0 to stop): "))
    
    if num == 0:   # condition to break the loop
        break
    
    total += num   # add number to total

print("The sum of all numbers is:", total) """

