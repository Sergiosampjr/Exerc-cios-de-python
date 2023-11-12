dias=int(input('Quantos dias alugado?'))
km=float(input('Quantos KM rodados?'))
preco_do_dia=dias*60
preco_por_km=km*0.15
total=preco_do_dia+preco_por_km
print('O total a pagar é de {0:.2f}R$'.format(total))