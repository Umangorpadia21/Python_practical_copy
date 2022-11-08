def are_coprime(a,b):
    
    hcf = 1

    for i in range(1, a+1):
        if a%i==0 and b%i==0:
            hcf = i

    return hcf == 1

# Reading two numbers
first = int(input('Enter first number: '))
second = int(input('Enter second number: '))

if are_coprime(first, second):
    print('%d and %d are CO-PRIME' %(first, second))
else:
    print('%d and %d are NOT CO-PRIME' %(first, second))
