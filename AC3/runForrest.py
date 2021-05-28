lista = []
cont = 1
soma = 0
media = 0


while cont > len(lista):
    cont += 1
    n = int(input())

    if n > 0:
        lista.append(n)

    else:

        for i in lista:
            soma += i
        
        media = soma / len(lista)
        break

print(f'MEDIA: {media:.2f}')


for i in lista:
    if i < media:
        print(i)
    






