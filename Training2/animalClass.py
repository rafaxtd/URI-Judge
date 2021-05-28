#In this problem, your job is to read three Portuguese words. These words define an animal according to the table below, from left to right. After, print the chosen animal defined by these three words.

class1 = input()
class2 = input()
class3 = input()


if class1 == 'vertebrado':
    if class2 == 'ave':
        if class3 == 'carnivoro':
            print('aguia')
        else:
            print('pomba')
    elif class2 == 'mamifero':
        if class3 == 'onivoro':
            print('homem')
        else:
            print('vaca')

if class1 == 'invertebrado':
    if class2 == 'inseto':
        if class3 == 'hematofago':
            print('pulga')
        else:
            print('lagarta')
    elif class2 == 'anelideo':
        if class3 == 'hematofago':
            print('sanguessuga')
        else:
            print('minhoca')





