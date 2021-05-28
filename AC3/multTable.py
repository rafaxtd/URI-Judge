a = int(input())
b = int(input())
cont = a

if a <= b:
    for i in range(a, b+1):

        
        for n in range(1, 10+1):
            total = cont * n
            print(f'{cont} x {n} = {total}')
            
        print('-'*10)
        cont += 1
        
        
else:
    print('Nenhuma tabuada no intervalo!')      
