# Cáculo da Equação do 2º grau
''' 
Esse código tem função de calcular uma equação do 2º grau em sua forma genérica 
ax² + bx + c = 0
'''

a = float(input('Insira um valor para A:'))
b = float(input('Insira um valor para B:'))
c = float(input('Insira um valor para C:'))     

delta = (b**2)-4*a*c

if delta >= 0:
    x1 = (-b + (delta**(1/2)))/(2*a)
    x2 = (-b - (delta**(1/2)))/(2*a)
    if x1 == x2:
        print('Essa equação possue uma raiz, que é',x1)
    else:
        print('As raizes dessa equação são',x1,'e',x2)
else:
    print('Erro. Delta negativo')
     
          

