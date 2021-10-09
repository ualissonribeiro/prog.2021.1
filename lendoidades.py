#Objetivo do programa
#pedir ao usuário para que digite a idade do primeiro indivíduo
#ler a idade de um indivíduo
#imprimir essa idade na tela
#pedir ao usuário para que digite a idade do segundo indivíduo
#ler a idade de um outro indivíduo
#imprimir essa idade de um outro indivíduo na tela
#somar as duas idades
#imprimir a soma dessas duas idades na tela


print("digite a idade da primeira pessoa")
idadedapessoa1 = int(input()) #função que converte o parâmetro pra inteiro
print(" idade digitada é ")
print(idadedapessoa1) 

print("digite aidade da segunda pessoa")
idadedapessoa2 = int(input())
print("a idade digitada é")
print(idadedapessoa2)

soma = idadedapessoa1+idadedapessoa2



print(" a soma das 2 idades é ")
print(soma)

#e se quisermos saber qual idade é a maior??

if(idadedapessoa1>idadedapessoa2):
    print("pessoa 1 tem maior idade")





#a função input() por definição retorna uma string(um texto, uma frase). Se quisermos ler
# um número inteiro e fazermos
#operações tratando a variável que irá receber esta entrada como número inteiro, precisamos
#converter este dado para inteiro