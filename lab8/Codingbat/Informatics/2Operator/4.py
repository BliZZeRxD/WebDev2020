def sign(a):
	if a > 0:
		return 1
	elif a == 0:
		return 0
	else:
		return -1


a = int(input())
print(sign(a))