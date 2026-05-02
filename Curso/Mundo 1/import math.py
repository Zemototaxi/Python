import math
x, y = map(float, input().splt())
x2, y2 = map(float, input().split())
distancia = math.sqrt(pow(x2 - 1, 2)+ 2)
print(f'{distancia:.4f}')