t = int(input())
for _ in range(t):
	n = int(input())
	a = list(map(int, input().split()))
	b = list(map(int, input().split()))
	flag = 0
	if (a == b):
		print("YES")
	else:
		i = 0
		while (i < n - 1):
			if(a[i] == b[i]):
        i += 1
      elif(a[-1] != b[-1] and a[-1] <= a[0]):
				a[-1] += 1
      elif(b[i] < a[i]):
				print("NO")
				flag = 1
				break
			elif(a[i] < b[i] and a[i] <= a[i + 1]):
				a[i] += 1
      else:
        i+=1 
	if (flag == 0):
		print("YES")
