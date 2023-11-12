lado1=int(input('digite um numero'))
lado2=int(input('digite um numero'))
lado3=int(input('digite um numero'))

if lado1>lado2+lado3 or lado2>lado1+lado3 or lado3>lado1+lado2:
    print('não é triangulo')
elif lado1==lado2 and lado2==lado3 and lado3==lado2:
    print('Triângulo equilátero')
elif lado1==lado2 or lado2==lado1 or lado3==lado1:
    print('o triângulo é isorceles')
else:
    print('triângulo escaleno')
