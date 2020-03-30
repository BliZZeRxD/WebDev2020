a = int(input())

list = [int(i) for i in input().split()]

i = 0
ans = 0
while i < a - 1:
	x = list[i]
	y = list[i + 1]
	if y > x:
		ans += 1
	i += 1

print(ans)