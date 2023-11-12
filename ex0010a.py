valor=float(input('Digite o valor da sua carteira.'))
dollar=4.88 #reais#
dobro=2*dollar
if valor==dollar:
    print('Você pode comprar Dollar!'.format(valor))
elif valor>=dobro:
    print('Você pode comprar mais de um dollar .')
else:
    print('Você não tem dinheiro suficiente.')
