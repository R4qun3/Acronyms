import random

passLength = int(input("Enter the length of the password:\n"))
c = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+=-[]}{;':/?><.,\"\\"
p = "".join(random.sample(c, passLength))
print(p)