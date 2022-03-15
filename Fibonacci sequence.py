"""Write a Python Program for Fibonacci numbers.

The Fibonacci numbers are the numbers in the following integer sequence. 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ……..
 In mathematical terms, the sequence Fn of Fibonacci numbers is defined by the recurrence relation"""


n_term=int(input("How many terms? "))
n_1=0;n_2=1
count=0
if n_term<=0:
    print("Please enter the positive integer")
elif n_term==1:
    print("Fibonacci series upto", n_term,":",n_1)
else:
    print("Fibonacci sequence:")
    while count<n_term:
        print(n_1)
        n_th=n_1+n_2
        n_1=n_2
        n_2=n_th
        count +=1