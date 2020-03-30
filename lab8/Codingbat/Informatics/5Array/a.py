a = int(input())

list = [int(i) for i in input().split()]

i = 0
for x in list:
	if i % 2 == 0:
		print(x)
	i += 1
