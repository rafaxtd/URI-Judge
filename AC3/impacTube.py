
def add(list, x):
    
    for i in range(x):
        
        list.append(input().split(';'))
      
    
    return 

x = int(input())
list1 = []
add(list1, x)
yesAdd = float(input())
noAdd = float(input())

print('-'*5)
print('BÔNUS')
print('-'*5)

for n in range(len(list1)):

    sub = list1[n][1]
    sub = float(sub)
    monet = list1[n][2]
    monet = float(monet)
    premium = list1[n][3]
    
    name = list1[n][0]
    
    if sub >= 1000 and premium == 'sim':
        total = sub // 1000 * yesAdd
        total += monet
        
        
        print(f'{name}: R$ {total:.2f}')

    elif sub >= 1000 and premium == 'não':
        total = sub // 1000 * noAdd
        total += monet
        

        
        print(f'{name}: R$ {total:.2f}')

    else:
        print(f'{name}: R$ {monet:.2f}')

