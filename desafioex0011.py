
#1 litro de tinta pinta 2m^2
altura=float(input('Digite à altura da parede:'))
largura=float(input('Digite à largura da parede:'))
parede=int(input('Digite a quantidade de litros da tinta:'))
calculo_da_area=altura*largura
quantidade=calculo_da_area/2
print('A altura da parede em metros quadrados é: {}'.format(altura))
print('A largura da parede em metros quadrados é: {}'.format(largura))
print('A área da parede em metros quadrados é: {}'.format(calculo_da_area))
print('A quantidade de tinta necessária para pintar a(s) parede(s) é: {0:.2f} de tinta'.format(quantidade))
