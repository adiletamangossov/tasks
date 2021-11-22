sign = input('Введите операцию: ')
quantity = int(input('Введите кол-во чисел: '))
operation = ''
result = 0

for num in range(1, quantity + 1):
	print('Введите ' + str(num) + ' число:', end = ' ')
	number = int(input())
	if num == 1:
		result += number
		operation += str(number)
	else:
			if sign == '+':
				result += number
				operation += ' ' +  sign + ' ' + str(number)
			elif sign == '-':
				result -= number
				operation += ' ' +  sign + ' ' + str(number)
			elif sign == '*':
				result *= number
				operation += ' ' +  sign + ' ' + str(number)
			elif sign == '/':
				result /= number
				operation += ' ' +  sign + ' ' + str(number)
			else:
				print('Ошибка: такой операции не существует. Попробуйте ещё раз.')
				sign = input('Введите операцию: ')
				first_num = int(input('Введите первое число: '))
				second_num = int(input('Введите второе число: '))
print(operation + ' =', int(result))