#Read four numbers (N1, N2, N3, N4), which one with 1 digit after the decimal point, corresponding to 4 scores obtained by a student. Calculate the average with weights 2, 3, 4 e 1 respectively, for these 4 scores and print the message "Media: " (Average), followed by the calculated result. If the average was 7.0 or more, print the message "Aluno aprovado." (Approved Student). If the average was less than 5.0, print the message: "Aluno reprovado." (Reproved Student). If the average was between 5.0 and 6.9, including these, the program must print the message "Aluno em exame." (In exam student).

# In case of exam, read one more score. Print the message "Nota do exame: " (Exam score) followed by the typed score. Recalculate the average (sum the exam score with the previous calculated average and divide by 2) and print the message “Aluno aprovado.” (Approved student) in case of average 5.0 or more) or "Aluno reprovado." (Reproved student) in case of average 4.9 or less. For these 2 cases (approved or reproved after the exam) print the message "Media final: " (Final average) followed by the final average for this student in the last line.

N1, N2, N3, N4 = input().split(' ')

N1 = float(N1)
N2 = float(N2)
N3 = float(N3)
N4 = float(N4)

N1 = (N1 * 2.0) 
N2 = (N2 * 3.0) 
N3 = (N3 * 4.0) 
N4 = (N4 * 1.0) 



media = (N1 + N2 + N3 + N4) / (2.0 + 3.0 + 4.0 + 1.0)
print(f'Media: {media:.1f}')

if media >= 7.0:
    print('Aluno aprovado.')
elif media < 5.0:
    print('Aluno reprovado.')
elif media >= 5.0 and media <= 6.9:
    print('Aluno em exame.')
    exam = float(input())
    print(f'Nota do exame: {exam}')
    final = (media + exam) / 2.0
    if final >= 5.0:
         print('Aluno aprovado.')
         print(f'Media final: {final}')
    else:
        print('Aluno reprovado.')
        print(f'Media final: {final}')