import random

r = random.randint(1, 100)
while True:
	num = input('請猜數字: ')
	num = int(num)
	if num == r:
		print('答對了!')
		break
	elif num > r:
		print('答錯了,比', num, '小')
	else:
		print('答錯了,比', num, '大')