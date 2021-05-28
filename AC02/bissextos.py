n1 = int(input())
n2 = int(input())

bi = 0

for i in range(n1, n2+1):

    b = str(i)
   
    if len(b) == 3 and (b[1] == '0' and b[2] == '0'):

        result = i % 400
        if result == 0:
            print(i)
            bi += 1

    elif len(b) == 4 and (b[2] == '0' and b[3] == '0'):
        result = i % 400
        if result == 0:
            print(i)
            bi += 1
    else:
        if i % 4 == 0:
            print(i)
            bi += 1

 

print(f'bissextos: {bi}')
