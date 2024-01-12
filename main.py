import random as ra
print("Welcome to password generator!!")
characters="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@[]{}#()*;._-"
length = int(input("enter length:  "))
password=""
for a in range(length):
    password += ra.choice(characters)
print(password)
print("I hope this password generator helps you to build a strongest password")