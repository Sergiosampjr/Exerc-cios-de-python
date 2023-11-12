import math
angulo=float(input('Digite um ângulo:'))
seno=math.sin(angulo)
cosseno=math.cos(angulo)
tangente=math.tan(angulo)
arredon=math.ceil(seno)
arre=math.ceil(cosseno)
arr=math.ceil(tangente)
print('seno {} cosseno {} tangente {}'.format(arredon,arre,arr))