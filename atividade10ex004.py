def maior(x,y,z):
    max=x
    if y > max:
        max=y
    if z> max:
        max=z
    return max
def menor(x,y,z):
    min=x
    if y < min:
        min=y
    if z<min:
        min=z
    return min
def menu():
    x=int(input('primeiro numero:'))
    y = int(input('segundo numero:'))
    z = int(input('terceiro numero:'))

    print("maior:",maior(x,y,z))
    print("menor:",menor(x,y,z))


