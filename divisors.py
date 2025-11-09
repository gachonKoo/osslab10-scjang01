import sys

number= int(input(""))


for i in range(number):
    if number % i == 0:
        print(i, end=" ")

        print()