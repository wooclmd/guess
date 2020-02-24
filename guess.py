import random
start = input('請輸入開始值: ')
end = input('請輸入結束值: ')
start = int(start)
end = int(end)

r = random.randint(start, end)
count = 0
while True:
	count = count + 1 
	num = input('請猜數字: ')
	num = int(num)
	if num == r:
		print('猜對了')
		print('這是你猜的第', count, '次')
		break
	elif num > r:
		print('猜錯了, 比', num, '小')
	else:
		print('猜錯了, 比', num, '大')
	print('這是你猜的第', count, '次')