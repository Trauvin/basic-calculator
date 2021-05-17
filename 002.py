print("Escolha uma opção: \n")

opcao  = int(input("1 - Adição | 2 - subtração | 3 - divisão \n4 - multiplicação | 5 - potência | 6 - raiz: "))

x = float(input("Digite o primeiro número da operação: "))

if not opcao == 6:
	y = float(input("Digite o segundo número da operação: "))


def soma(x, y):
	return x + y

def subtracao(x, y):
	return x - y

def divisao(x, y):
	return x / y

def multiplicacao(x, y):
	return x * y

def potencia(x, y):
	return x ** y

def raiz(x):
	return x ** 0.5


if (opcao == 1):
	print(f"A soma entre {x} e {y} é: ", soma(x, y))

elif (opcao == 2):
	print(f"A subtração entre {x} e {y} é: ", subtracao(x, y))

elif (opcao == 3):
	print(f"A divisão entre {x} e {y} é: ", divisao(x, y))

elif (opcao == 4):
	print(f"A multiplicação entre {x} e {y} é: ", multiplicacao(x, y))

elif (opcao == 5):
	print(f"A potência entre {x} e {y} é: ", potencia(x, y))

elif (opcao == 6):
	print(f"A raiz entre {x} é: ", raiz(x))

else:
	print("Digite uma opção válida.")



