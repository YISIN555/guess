import random

r = random.randint(1, 100)
print(r)
while True:
	num = input('請猜數字:')
	num = int(num)
	if num == r:
		print('你猜中了')
		break
	elif num < r:
		print('比它小')
	elif num > r:
		print('比它大')



