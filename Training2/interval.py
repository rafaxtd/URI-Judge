#You must make a program that read a float-point number and print a message saying in which of following intervals the number belongs: [0,25] (25,50], (50,75], (75,100]. If the read number is less than zero or greather than 100, the program must print the message “Fora de intervalo” that means "Out of Interval".

#The symbol '(' represents greather than. For example:
#[0,25] indicates numbers between 0 and 25.0000, including both.
#(25,50] indicates numbers greather than 25 (25.00001) up to 50.0000000.

n1 = float(input())



if n1 > 0 and n1 <= 25.0000:
    print(f'Intervalo [0,25]')

elif n1 >= 25.00001 and n1 <= 50.0000000:
    print(f'Intervalo (25,50]')

elif n1 <= 0 or n1 > 100.00:
    print(f'Fora de intervalo')

elif n1 > 50.0000000 and n1 <= 100:
    print(f'Intervalo (75,100]')



