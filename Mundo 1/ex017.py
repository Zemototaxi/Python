from math import hypot
cat = float(input('digite o cateto oposto '))
cat2 = float(input('digite o cateto adjacente '))
# esse é o calculo que eu faria se não importasse hypot (a**2 + b**2)**0.5
print(f'Hipotenusa é igual a {hypot(cat, cat2)}')
