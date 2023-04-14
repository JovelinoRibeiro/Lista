#String = words, group of caracters
#variable = data, number, value 
#booalean value = True or False
#input = use to read a value from the window = name = input("What is your name? ")
#print("Hello " +name)  
#string concatenetion
#type conversation
#nome, idade, peso = variavel
#toda varievel é um objeto para o python

#tipos primitivos são: 4 principais tipos,exemplos
#(int = 7, -4 ,0, 9875 ) 
#float = ( 7.0, 4.5, 0.057, -15.233) , 
#bool = boolean (True, False)
#(str = string = "ola" todas as palavras tem que estar entre aspas. "7.5" sempre a função input vai voltar como string a nao ser que coloque int ou alguma outra. 

#nome = input("Qual é seu nome? ")
#print("Olá, um prazer te conhecer", input(nome))

n1 = int(input("Digite um valor: "))
n2 = int(input("Digite um segundo valor: "))
s = n1 + n2
#print("A soma entre ", n1, "e", n2, "É igual a ", s)
print("A soma entre {} e {} vale {}".format(n1, n2, s))

+ adição
- subtração
* Multiplicação
/ Divisão
** potencia = 5**2= 25
// divisão inteira = 5/5 = 2
% resto da divisão = 1


Ordem de Precedência
1= ()
2= **
3= * / // %
4= + -
ex:
5+3*2==11
3*5+4**2== 31
3*(5+4)**2==243
raiz quadrada de 81 = 81**(1/2)=9
raiz quadrada de 25 = 25**(1/2)=5
ao cubo = 4**3 =64
ao cubo = pow(4,3) =64
122%3= resto 2
raiz cubica = 127**(1/3) = 5.026

n1 = int(input("Digite um valor: "))
n2 = int(input("Outro valor: "))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print("A Soma é {}, \n o produto é {} e a \n divisão é {:.3f}".format(s, m, d), end="")
print("\n Divisão inteira {} \n e potencia {} ".format(di, e))

Exercicio 02 = pergunta para o teclado
nome = input("Qual é seu nome? ")
print("É um prazer te conhecer, {}!".format(nome))

Exercicio 03 = soma entre dois numeros
n1 = int(input("Digite um valor: "))
n2 = int(input("Digite outro valor: "))
s = n1 + n2
print("A soma de {} e {} é igual a {}!".format(n1, n2, s))

Exercicio 04 = Verificação se tem numeros, maiuscula ou minuscula, se é string.
a = input("Digite algo: " )
print(" o tipo primitivo desse valor é: ", type(a))
print("Só tem espaço? ", a.isspace())
print("é um numero? ", a.isnumeric())
print("é alfabetico? ", a.isalpha())
print("É alfanumerico? ", a.isalnum())
print("Esta em maiusculas? ", a.isupper())
print("Esta em minusculas? ", a.islower())

Exercicio 05 = Faça um programa que mostre um numero inteiro que mostre seu antecessor, e seu sucessor.
n = int(input("Digite um numero: "))
a =  n - 1
s = n + 1
print("Analisando o valor {}, seu antecessor é {} e o sucessor é {}".format(n, a, s,))

Exercicio 06 = Faça um algoritmo que leia um numero e mostre o dobro, triplo e a sua raiz quadrada.
n = int(input("Digite um numero: "))
print("O dobro de {} vale {}. ".format(n, (n*2)))
print("O triplo de {} vale {}. \nA raiz quadrada de {} é Igual a {:.2f}. ".format(n, (n*3), n, (n**(1/2))))


exercicio 07 = Faça uma media entre dois numeros.
n1 = float(input("Primeira nota do aluno: "))
n2 = float(input("Segunda nota do aluno: "))
media = (n1 + n2) /2
print("A media do aluno é {} e {} é igual a {}".format(n1, n2, media))


exercicio 08 = Importando modulos 
import math
num = int(input("Digite um número: "))
raiz = math.sqrt(num)
print("A raiz de {} é igual a {:.3f}".format(num, raiz))

Exercicio 09 = Fatiamento
frase[9:13] vai do 9 ate o 12 
c u r s o   e m   v i  d  e   o     p  y  t  h  o  n
0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20
frase[:13] vai do 0 ate o 12 
frase[12:] vai do 12 ate o final da frase
frase[9:13:2] vai do 9 ate o 12 e o dois no final significa que vai pulando de dois em dois. sempre kickando no segundo

len(frase) siginifica tamanho da frase 
len de curso em video python tem 21 caracteres.
frase.count(o) vai contar quantas vezes existe a letra O 
frase.find("DEO") quantas vezes a frase encontrou deo
curso in frase  o in sign
frase.replace("python", "android troca o nome por outro. 
frase.upper() tudo em caps
frase.lower() tudo em minusculo nao esquece dos parenteses
frase.capitalize a primeira fica maiuscula o restante minuscula
frase.title()transforma a primeira palavra de cada palavra em maiuscula. 
frase.strip() retira espaços desnecessario do inicio e do fim
frase.rstrip() ira remover somente os ultimos espaços
frase.lstrip() ira remover somente os primeiros espaços =L significa left 
frase.split() cada palavra recebe indexação nova. gera uma lista com cada cadeia de caracteres. 
("-").join() faz com que junta as frases e colocar uma traçinho
print(""" texto inteiro""")

exercicio 10 = coloque todo o nome em capslock 
name = input("Digite Seu Nome: ")
print(name.upper())
print(name.lower())

exercicio 11 = Condições = se tem somente o IF é uma estrutura simples, e quando tem o if e else é composta.
ifcard.left():
  bloco verde True
else:
  Bloco vermelho False
exemplo:
tempo = int(input("Quantos anos tem seu carro? "))
print("Seu carro esta novo" if tempo<=3 else "Seu carro ja esta usado")

exercicio 12 = if and else
nome = str(input("Bom dia, Qual é o seu nome? "))
print("Você tem um nome bacana" if nome == "maria" else "Seu nome é comum", nome)

exemplo 2 = 
n1 = float(input("Digite sua primeira nota: "))
n2 = float(input("Digite sua segunda nota: "))
s = (n1+n2) / 2
print("A sua media foi {:.1f}".format(s))
if s >= 5.0:
  print("Você passou!")
else: 
  print("Você precisa estudar mais. ")


exercicio = 13 = faça uma tabuada
num = int(input("Digite um numero para ver sua tabuada: "))
print("{} x {} = {}".format(num, 1, num*1))
print("{} x {} = {}".format(num, 2, num*2))
print("{} x {} = {}".format(num, 3, num*3))
print("{} x {} = {}".format(num, 4, num*4))
print("{} x {} = {}".format(num, 5, num*5))
print("{} x {} = {}".format(num, 6, num*6))
print("{} x {} = {}".format(num, 7, num*7))
print("{} x {} = {}".format(num, 8, num*8))
print("{} x {} = {}".format(num, 9, num*9))
print("{} x {} = {}".format(num, 10, num*10))
print("_" * 40) #faz um traço no final da pagina

exercicio 14 = Conversor de moedas
real = float(input("Quantos reais você tem R$:"))
dolar = real / 5.23
print("Com R$:{:.2f} você terá $$:{:.2f}".format(real, dolar))

exercicio 15 = faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua area e a quantidade de tintanecessaria para pinta-la, sabendo que cada litro de tinta, pinta uma area de 2m quadrados. 

larg = float(input("Largura da parede: "))
alt = float(input("Altura da parede: "))
area = larg * alt
print("Sua parede tem a dimensão de {} x {} e sua área é de {}m2.".format(larg, alt, area))
tinta = area / 2
print("Para pintar essa parede você vai precisar {}L de tinta.".format(tinta))