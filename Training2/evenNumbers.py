# Make a program that reads five integer values. Count how many of these values ​​are even and  print this information like the following example.

# URI 1065

even = 0

for i in range(0, 5):
    n = int(input())

    if n % 2 == 0:
        even += 1  


print (f'{even} valores pares')