#Exercio 1.19 http://wiki.python.org.br/EstruturaDeDecisao
#Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas, dezenas e unidades do mesmo.
#Observando os termos no plural a colocação do "e", da vírgula entre outros. Exemplo:
#326 = 3 centenas, 2 dezenas e 6 unidades
#12 = 1 dezena e 2 unidades Testar com: 326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16

numero = input ( "\tDigite um numero menor do que 1000 : " )
numerostr = str(numero)

if len(numerostr) == 3:
	centena = numerostr[0:1]
	dezena = numerostr[1:2]
	unidade = numerostr[2:3]
	print ("\n\t", numerostr, " = ", centena, " centenas ", dezena , " dezenas e ", unidade , " unidades " )
elif len(numerostr) == 2:
	dezena = numerostr[0:1]
	unidade = numerostr[1:2]
	print ("\n\t", numerostr, " = ", dezena , " dezenas e ", unidade , " unidades " )
elif len(numerostr) == 1:
	unidade = numerostr[0:1]
	print ("\n\t", numerostr, " = ", unidade , " unidades " )
