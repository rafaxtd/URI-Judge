

buy = True
vic = 0 

while buy == True:

    n = float(input())

    if n == -1.0:
        buy = False

    else:

         vic += n
    
real = vic * 2.50

print(f'VC$ {vic:.2f}')
print(f'R$ {real:.2f}')

