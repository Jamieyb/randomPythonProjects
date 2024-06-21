def isprime(n):
  if n>1 :
    return True if n>=2 and n<=3 else n%2==1 and n%3!=0
  else: 
    return False

print(isprime(1))