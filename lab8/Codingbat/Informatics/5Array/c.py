a = int(input())

list = [int(i) for i in input().split()]

pos = 0
for x in list:
	if x > 0:
		pos += 1

print(pos)