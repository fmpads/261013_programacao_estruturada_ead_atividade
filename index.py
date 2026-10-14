'''
13/10/26
Faculdade Municipal de Palhoça
Tecnologia em Análise e Desenvolvimento de Sistemas
Turma: 93. ADS - ADS/MAT - 2026/2 - MATURINO
Disciplina: Prática de Programação Estruturada
Docente: Prof.ª Daniela Amorim
Discente: Jean Douglas Toledo Rodrigues Junior

EaD 03

'''

# Questão 1

soma = 0 # declaração das variáveis que serão utilizadas
print(f"\nQuestão 1. Faça um programa que calcule e escreva a seguinte soma: soma = 1/1 + 3/2 + 5/3 + 7/4 + ... + 99/50.\n")
for i in range (1, 101): # intervalo entre 1 e 100
    if i % 2 == 0: # se o número for par, entra nesta condição
        numerador = i - 1 # define o numerador como o número ímpar anterior
        denominador = i // 2 # define o denominador como a metade do número par
        soma += numerador / denominador # define a somatória das divisões das frações
        if i < 100: # condição pra imprimir o sinal de + entre as frações até no penúltimo
            print(f"{numerador}/{denominador} + ", end="")
        else: # condição para imprimir o sinal de = depois da última fração
            print(f"{numerador}/{denominador} =", end="")
print(f"\n\nsoma = {soma}\n")

# Questão 2

numeros = 0 # declaração das variáveis que serão utilizadas
print(f"Questão 2. Liste os números de 1 até 500.\n")
for i in range(1, 501): # intervalo entre 1 e 500
    if i < 500: # condição pra imprimir a vírgula entre os números até o penúltimo
        print(f"{i},", end=" ")
    else: # condição para imprimir o sinal de = depois do último número
        print(f"{i}", end="\n")
    numeros += 1 # incremento do contador de números

#Questão 3

print(f"\nQuestão 3. Foi feita uma pesquisa entre os habitantes de uma região e coletados os dados de altura e sexo (0=masc, 1=fem) das pessoas.")
print(f"\nFaça um programa que leia 50 dados diferentes e informe:")
print(f"\n- a maior e a menor altura encontradas;")
print(f"\n- a média de altura das mulheres;") 
print(f"\n- a média de altura da população;") 
print(f"\n- o percentual de homens na população.")

contadorHomens = 0
contadorMulheres = 0
maiorAlturaHomens = 0
maiorAlturaMulheres = 0
menorAlturaHomens = 0
menorAlturaMulheres = 0
somaAlturaHomens = 0
somaAlturaMulheres = 0

for i in range(1, 51):
    sexo = int(input(f"\nQual o sexo da {i}ª pessoa (0=masc, 1=fem)? "))
    altura = float(input(f"Qual a {i}ª altura? "))

    if sexo == 0:
        contadorHomens += 1
        somaAlturaHomens += altura
        if contadorHomens == 1:
            maiorAlturaHomens = altura
            menorAlturaHomens = altura
        else:
            if altura > maiorAlturaHomens:
                maiorAlturaHomens = altura
            if altura < menorAlturaHomens:
                menorAlturaHomens = altura
    else:
        contadorMulheres += 1
        somaAlturaMulheres += altura
        if contadorMulheres == 1:
            maiorAlturaMulheres = altura
            menorAlturaMulheres = altura
        else:
            if altura > maiorAlturaMulheres:
                maiorAlturaMulheres = altura
            if altura < menorAlturaMulheres:
                menorAlturaMulheres = altura

mediaAlturaHomens = (somaAlturaHomens / contadorHomens) if contadorHomens > 0 else 0
mediaAlturaMulheres = (somaAlturaMulheres / contadorMulheres) if contadorMulheres > 0 else 0
totalPessoas = contadorHomens + contadorMulheres
mediaPopulacao = ((somaAlturaHomens + somaAlturaMulheres) / totalPessoas) if totalPessoas > 0 else 0

if contadorHomens > 0 and contadorMulheres > 0:
    maiorAltura = max(maiorAlturaHomens, maiorAlturaMulheres)
    menorAltura = min(menorAlturaHomens, menorAlturaMulheres)
elif contadorHomens > 0:
    maiorAltura = maiorAlturaHomens
    menorAltura = menorAlturaHomens
elif contadorMulheres > 0:
    maiorAltura = maiorAlturaMulheres
    menorAltura = menorAlturaMulheres
else:
    maiorAltura = 0
    menorAltura = 0

percentualHomens = (contadorHomens * 100 / totalPessoas) if totalPessoas > 0 else 0

print(f"\nA maior altura é: {maiorAltura} metros")
print(f"\nA menor altura é: {menorAltura} metros")
print(f"\nA média de altura das mulheres é: {mediaAlturaMulheres:.2f} metros")
print(f"\nA média de altura da população é: {mediaPopulacao:.2f} metros")
print(f"\nO percentual de homens da população é: {percentualHomens:.2f} %")

# Questão 4

print(f"\nQuestão 4. Criar um algoritmo que leia os limites inferior e superior de um intervalo e imprima todos os números pares no intervalo aberto e seu somatório.")
print(f"\nSuponha que os números digitados são um intervalo crescente.")
print(f"\nExemplo:")
print(f"\n- Limite inferior: 3")
print(f"\n- Limite superior: 12")
print(f"\n- Saída: 4 6 8 10")
print(f"\n- Soma: 28")

soma = 0 
inferior = int(input("\nQual o limite inferior do intervalo? "))
superior = int(input("Qual o limite superior do intervalo? "))

ultimo_par = superior - 1
while ultimo_par > inferior and ultimo_par % 2 != 0:
    ultimo_par -= 1

for i in range (inferior + 1, superior): 
    if i % 2 == 0: 
        if i == ultimo_par:
            print(f"{i} = ", end="")
        else: 
            print(f"{i} + ", end="")
        soma += i 

print(f"\nSoma: {soma}")