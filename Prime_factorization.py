def primeFactor(n):
    f = () # tuple to store the factors
    # try to divide n by 2 and add 2 to f tuple
    # then check if the result (n) is stil an even number or odd
    while n % 2 == 0: 
        f += (2,)
        n /= 2
    # n must be odd at this point
    # since odd numbers only divisible by odd number i use step of 2
    for i in range(3,int(n+1),2):     
        # while i divides n , add i to f tuple
        while n % i== 0:
            f += (i,)
            n /= i
    # when n cant be divided by two step above
    # means now n is a prime number. Add n to f tuple
    if isprime(n):
        f += (n,)

    return f
