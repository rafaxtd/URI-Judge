rent = int(input())
pay = int(input())

payment = 1

if rent > pay:
    while rent != 0:   

        print(f'pagamento: {payment}')
        print(f'antes = {rent}')
        rent -= pay
        print(f'depois = {rent}')
        print('-----')
       
        payment += 1

        if rent == 0:
            break

        if rent < pay:
            
            print(f'pagamento: {payment}')
            print(f'antes = {rent}')
            rent = 0
            print(f'depois = {rent}')
            print('-----')
           
            


else:
    print(f'pagamento: {payment}')
    print(f'antes = {rent}')
    rent = 0
    print(f'depois = {rent}')
    print('-----')
    




