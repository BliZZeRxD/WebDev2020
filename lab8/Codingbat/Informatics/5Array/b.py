a = int(input())

list = [int(i) for i in input().split()]

for x in list:
	if x % 2 == 0:
		print(x)
