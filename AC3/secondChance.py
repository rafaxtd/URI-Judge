def getGrades(list, x):

    for i in range(x):
        n = float(input())
        list.append(n)
        
    return list

n = int(input())

grades = []
activityGrades = []
lastGrade = []
cont = 0

getGrades(grades, n)
getGrades(activityGrades, n)

for i in range(n):

    if grades[i] == 10 or activityGrades[i] < 10:
        lastGrade.append(grades[i])
    elif activityGrades[i] == 10:
        calc = grades[i] + 2

        if calc > 10:
            calc = 10
        

        lastGrade.append(calc)

        if grades[i] != lastGrade[i]:
            cont += 1

print(f'NOTAS ALTERADAS: {cont}')

for i in range(n):
    if grades[i] != lastGrade[i]:
        print(f'*({(i+1):0>3}) original: {grades[i]:05.2f} | final: {lastGrade[i]:05.2f}')
    else:
        print(f'-({(i+1):0>3}) original: {grades[i]:05.2f} | final: {lastGrade[i]:05.2f}')


        




