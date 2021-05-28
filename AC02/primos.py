n = int(input())
alfabeto = ['','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
            'U', 'V', 'W', 'X', 'Y', 'Z']
qtd_linhas = 0
qtd_letras = 0

if 1 <= n and n <= 26:
    while n >= qtd_linhas:
        qtd_letras = 0
        while qtd_linhas > qtd_letras:
            print(alfabeto[qtd_linhas],end='')
            qtd_letras += 1
        print('')
        qtd_linhas += 1
