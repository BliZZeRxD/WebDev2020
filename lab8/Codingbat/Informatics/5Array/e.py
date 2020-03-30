n = int(input())

list = [int(i) for i in input().split()]

i = 1
ok = False
for i in range(0, len(list) - 1):
	if list[i]*list[i + 1] > 0:
		ok = True
		break

if ok:
	print("YES")
else:
	print("NO")