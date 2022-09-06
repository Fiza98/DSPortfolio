# Python program to display all the prime numbers within an interval

lower = 0
upper = 1000000

print("Prime numbers between", lower, "and", upper, "are:")

for num in range(lower, upper + 1):
   # all prime numbers are greater than 1
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print(num)

#FIND THE SUM FOR THE PRIME NUMBERS
N=1000000
s=0  # variable s will be used to find the sum of all prime.
Primes=[True for k in range(N+1)] 
p=2 
Primes[0]=False # zero is not a prime number.
Primes[1]=False #one is also not a prime number.
while(p*p<=N):
    if Primes[p]==True: 
        for j in range(p*p,N+1,p): 
            Primes[j]=False 
    p+=1 
for i in range(2,N): 
    if Primes[i]: 
        s+=i 
print('The sum of prime numbers:',s)
