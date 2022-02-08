str = input()

#иассив для операций act, массив для чисел - digit
list_action = []
list_digit = []

#функция ставит приоритеты для последовательности действий
def prior(c):
	if c == '>':
		return 2
	if c == '+' or c == '-':
		return 3
	if c == '*':
		return 4
	if c == '(':
		return 1
	if c == ')':
		return 5


i = 0
#цикл идет по строке формулы (str = input()) и распределяет данные на 2 листа: act - стек для операций (никогда не может быть чисел), digit - стек для чисел (+ тут могут временно быть операторы) 
while i <= len(str) - 1:
	while i <= len(str) - 1 and str[i].isdigit() == True:
		digit = 10 * digit + int(str[i])
		flag = 1
		i = i + 1
	if flag == 1:
		list_digit.append(digit)
		digit = 0
		flag = 0
	if i <= len(str) - 1 and str[i].isdigit() == False:
		if str[i] == '(' or len(list_action) == 0:
			list_action.append(str[i])
		elif str[i] == ')':
			end = len(list_action) - 1
			while end >= 0:
				if list_action[end] == '(':
					list_action.pop(end)
					break
				list_digit.append(list_action[end])
				list_action.pop(end)
				end = end - 1
		elif prior(str[i]) <= prior(list_action[len(list_action) - 1]):
			end = len(list_action) - 1
			list_digit.append(list_action[end])
			list_action.pop(end)
			list_action.append(str[i])
		else:	
			list_action.append(str[i])
	i = i + 1
if i == len(str) + 1:
	end = len(list_action) - 1
	while end >= 0:
		list_digit.append(list_action[end])
		list_action.pop(end)
		end = end - 1
	
#в итоге по принципу обратной польской записи операторы и операнды лежат в стеке digit. стек act пуст и больше не используется


#создаем массив для результата. в итоге там останется 1 числоб другие листы будут пустыю тут только числа без операторов
list_finish = []

#итоговый расчеты по принципу обратной польской считаем: цифры для вычислений переносим из digit в finish, результат вычислений кладем во временную переменную new, убираем отработанные значения из finish и digit.
#промежуточный результат вычислений new кладем в finish
while len(list_digit) > 0:
	if list_digit[0] != '+' and list_digit[0] != '-' and list_digit[0] != '*' and list_digit[0] != '>':
		list_finish.append(list_digit[0])
	else:
		if list_digit[0] == '+':
			new = list_finish[len(list_finish) - 2] + list_finish[len(list_finish) - 1]
		elif list_digit[0] == '-':
			new = list_finish[len(list_finish) - 2] - list_finish[len(list_finish) - 1]
		elif list_digit[0] == '*':
			new = list_finish[len(list_finish) - 2] * list_finish[len(list_finish) - 1]
		elif list_digit[0] == '>':
			if list_finish[len(list_finish) - 2] > list_finish[len(list_finish) - 1]:
				new = 1
			else:
				new = 0
		list_finish.pop()
		if len(list_finish) != 0:
			list_finish[len(list_finish) - 1] = new
		else:
			list_finish[0] = new
	list_digit.pop(0)


print('act = ', list_action, 'dig = ', list_digit, 'finish = ', list_finish)
