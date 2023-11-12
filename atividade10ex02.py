dia=input('Digite o dia:')
mes=input('Digite o més:')
ano=input('Digite o ano:')
semana=(input('digite o dia da semana'))
if semana=='d':
    print('Domingo,{} de {} de {}.'.format(dia, mes, ano))
elif semana=='2':
    print('Segunda-Feira,{} de {} de {}.'.format(dia, mes, ano))
elif semana=='3':
    print('Terça-Feira,{} de {} de {}.'.format(dia, mes, ano))
elif semana=='4':
    print('Quarta-Feira,{} de {} de {}.'.format(dia, mes, ano))
elif semana=='5':
    print('Quinta-Feira,{} de {} de {}.'.format(dia, mes, ano))
elif semana=='6':
    print('Sexta-Feira,{} de {} de {}.'.format(dia, mes, ano))
else:
    print('Sábado,{} de {} de {}.'.format(dia, mes, ano))


