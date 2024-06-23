def isprime(n):
  if n>1 :
    return True if n>=2 and n<=3 else n%2==1 and n%3!=0
  else: 
    return False

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

def lcm_1(n1, n2): # counting the Least Common Multiple (LCM) 'WITHOUT FORMULA'
    # making tuples of the prime factorization of both integer
    n1 = primeFactor(n1) 
    n2 = primeFactor(n2)
    # join the two tuples
    kpk = (n1)+(n2)
    # looping thru the number present in the tuple
    for i in kpk:
        # and check iwhere i present the most between the two tuples
        # then subtracting the amount of i in kpk by the least amount of i of either the two tuples
        if i in n1 and i in n2 and n1.count(i) > n2.count(i):
            x = list(kpk)
            for r in range(kpk.count(i)-n1.count(i)):
                x.remove(i)
            kpk=tuple(x)
        elif i in n1 and i in n2 and n2.count(i) > n1.count(i):
            x = list(kpk)
            for r in range(kpk.count(i)-n2.count(i)):
                x.remove(i)
            kpk=tuple(x)
        elif i in n1 and i in n2 and n1.count(i) == n2.count(i):
            x = list(kpk)
            for r in range(kpk.count(i)-n1.count(i)):
                x.remove(i)
            kpk=tuple(x)
    # return a sorted tuple of kpk
    return tuple(sorted(kpk))

def gcd(n1, n2): # return the Greatest Common Factor (GCM) or Greatest Common Divisor (GCD)
    #making set of factors of the integer given
    n1 = (set(i for i in range(1,n1+1) if n1%i==0))
    n2 = (set(i for i in range(1,n2+1) if n2%i==0))
    # intersecting the sets. then convert it to a list
    # means returning a new list, that only contains the items that are present in both sets.
    fpb = list((n1&n2))
    # return the highest number in the list
    return fpb[len(fpb)-1]

def lcm(n1, n2): # return the Least Common Multiple (LCM)
    # basically just using the LCM formula
    return (n1*n2)/(gcd(n1, n2))


a = 6
b = 8

print(gcd(a, b))
print(lcm(a, b))