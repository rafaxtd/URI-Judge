#Read two integer values X and Y. Print the sum of all odd values between them.

#Input
#The input file contain two integer values.

#Output
#The program must print an integer number. This number is the sum off all odd values between both input values that must fit in an integer number #

X = int(input())
Y = int(input())

soma = 0
cont = X

while X > Y:

    cont -= 1

    if cont == Y:
        break

    

    elif cont % 2 != 0:
        soma += cont
    

print(soma)