#basic password generator

import random

#string of all available characters
chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@£$%^&*().,?0123456789'

#asks user how long password to be
length = input('password length? ')
length = int(length)

#generates it
password = ''
for i in range(length):
    password += random.choice(chars)
    
#prints it duh
print(password)
n = input("You are welcome")