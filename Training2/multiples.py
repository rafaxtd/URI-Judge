# Read two integer values (A and B). After, the program should print the message "Sao Multiplos" (are multiples) or "Nao sao Multiplos" (aren’t multiples), corresponding to the read values.

A, B = input().split(" ")
A = int(A)
B = int(B)


for i in range (1, 10+1):
    result = A * i
    print(result)

    if result == B:
       multiple = True
       break
    else:
        multiple = False

if multiple == True:
    print('Sao Multiplos')
else:
    
    print('Nao sao Multiplos')