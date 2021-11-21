#FUNÇÕES
def linha(q):
	print(q*'=')

def titulo(tit):
	lin = len(tit) + 44
	print(lin*'=')
	print(f'                     {tit}')
	print(lin*'=')
	
def execao(txt):
	while True:
		try:
			resp = int(input(f' {txt}: '))
			break
		except ValueError:
			print(' Valor Invalido! Tente novamente')
	return resp
				
def validacao(var, num, num2, txt2):
	while var > num or var < num2:
		print('Horario invalido Tente novamente!')
		var = execao(txt2)
	return var

	
#PERGUNTAS
titulo('CALCULE AS HORAS')
while True:
	opc = str(input(' Vc quer subtrair ou somar as horas? [SUB/SOM]: ')).upper()
	if opc == 'SUB' or opc == 'SOM':
		break
	else:
		print('Opção invalida! Tente Novamente.')
		linha(60)

linha(60)
print(' Horario Base: ')
hora = execao('Hora')
hora = validacao(hora, 23, 0, 'Hora')
minuto = execao('Minuto')
minuto = validacao(minuto, 59, 0, 'Minuto')
linha(30)
print(' Segundo Horario:')	
hora2 = execao('Hora2')
hora2 = validacao(hora2, 23, 0, 'Hora')
minuto2 = execao('Minuto2')
minuto2 = validacao(minuto2, 59, 0, 'Minuto')

#EQUAÇÃO
if opc == 'SUB':
		
	if minuto - minuto2 < 0:
		minutoMen = minuto - minuto2
		minutoMen1 = minutoMen * -1
		minutoFinal = 60 - minutoMen1
		hora += 1
		
	else:
		minutoFinal = minuto - minuto2
	
	if hora - hora2 < 0:
		horaMen = hora - hora2
		horaMen1 = horaMen * -1
		horaFinal = 24 - horaMen1
		
	else:
		horaFinal = hora - hora2

else:

	if minuto + minuto2 > 59:
		minutoMai = minuto + minuto2
		minutoFinal = minutoMai - 60
		hora += 1
		
	else:
		minutoFinal = minuto + minuto2
	
	if hora + hora2 > 23:
		horaMai = hora + hora2
		horaFinal = horaMai - 24
	
	else:
		horaFinal = hora + hora2

if opc == 'SUB':
	if hora - hora2 < 0:
		dia = 'Ontem'
	else:
		dia = 'Hoje'
else:
	if hora + hora2 > 23:
		dia = 'Amanhã'
	else:
		dia = 'Hoje'

horaFinal = str(horaFinal)
minutoFinal = str(minutoFinal)

#APRESENTAÇÃO
linha(60)
if len(horaFinal) == 2 and len(minutoFinal) == 2:
	print(f' O resultado desses horarios é igual á {horaFinal}:{minutoFinal} de {dia}!')

elif len(horaFinal) == 1 and len(minutoFinal) == 2:
	print(f' O resultado desses horarios é igual á 0{horaFinal}:{minutoFinal} de {dia}!')
	
elif len(horaFinal) == 2 and len(minutoFinal) == 1:
	print(f' O resultado desses horarios é igual á {horaFinal}:0{minutoFinal} de {dia}!')
	
else:
	print(f' O resultado desses horarios é igual á 0{horaFinal}:0{minutoFinal} de {dia}!')
	