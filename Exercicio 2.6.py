# Escreva um programa que solicite ao usuário a nota de um aluno, que deve ser um numero real entre 0.0 e 10.0
'''
Se a nota for menor que 6.0, o programa deve imprimir a mensagem “Nota F”.
• Se a nota for de 6.0 até 7.0, o programa deve imprimir a mensagem “Nota D”.
• Se a nota for entre 7.0 e 8.0, o programa deve imprimir a mensagem “Nota C”.
• Se a nota for entre 8.0 e 9.0, o programa deve imprimir a mensagem “Nota B”.
• Se a nota for entre 9.0 e 10.0, o programa deve imprimir a mensagem “Nota A”.

'''
print('>'*35)
media = float (input('Digite a nota de um aluno  '))

if media < 6:
    print ('Sua Média não foi boa. NOTA F')
elif media <= 7:
    print ('Sua media foi razoável. NOTA D')
elif media <= 8:
    print ('Sua média foi boa. NOTA C')
elif media <= 9:
    print ('Sua média foi legal. NOTA B')
if media >=9:
    print('Sua nota foi Excelente! Parabéns! NOTA A!')

print('>'*35)

