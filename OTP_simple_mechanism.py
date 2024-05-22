#One time password simple  mechanism 
import random
otp = random.randint(999,9999)
email = input('Please input your email : ')
print(f'sending otp {otp} to {email}...')