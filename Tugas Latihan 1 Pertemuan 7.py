from random import random

print("Program menentukan bilangan acak < 0.5")
jum_bil = int(input("Masukan nilai N :"))
print("--------------------------------")

x = 0

while x < jum_bil:
    nilai_random = random()
    if nilai_random < 0.5:
        x += 1
        print("Data ke-", x, ":", nilai_random)
