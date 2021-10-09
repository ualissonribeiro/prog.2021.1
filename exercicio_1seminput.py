#objetivo do exercício.
#Configurar os valores de peso e altura manualmente no próprio programa
#fazer o cálculo do IMC
#imprimir resultados das comparações do valor do imc com os definidos no exercício

#qual será a saída do programa quando for executado?
#se o resultado do imc for 20
#False
#False
#True
#False
#False

#não serão utilizadas leituras do teclado.
#neste trecho é realizada a atribuição dos valores e o cálculo do imc
peso = 90
altura = 1.8

imc = (peso/(altura*altura))

print(imc<17)
print((imc>=17) and (imc<18.5))
print((imc>=18.5) and (imc<25))
print((imc>=25) and (imc<30))
print(imc>30)

#casos a imprimir
#imc menor que 17
#imc entre 17 e 18.5 --> imc maior ou igual a 17 e imc menor que 18.5
#operador "e" é a palavra and

#imc entre 18.5 e 25 --> imc maior ou igual a 18.5 e imc menor que 25
#operador "e" é a palavra and

#imc entre 25 e 30 --> imc maior ou igual a 25 e imc menor que 30
#operador "e" é a palavra and

#imc maior que 30


#Em python, se quisermos imprimir resultados diretos de comparações, temos duas opções. A
#primeira é colocar este resultado dentro de uma variável e em seguida imprimir diretamente
#esta variável.

#A segunda opção é fazer o print diretamente do resultado