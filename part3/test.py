arr = [5,6,7,8,9,1,2,3]
l = 0
r = len(arr)

while(l<=r):
	mid = (l+r)//2
	if(arr[mid]>arr[mid+1]):
		print(mid+1)
		break
	elif(arr[mid]<arr[mid+1] and arr[mid]>arr[l]):
		low = mid+1
	elif(arr[mid]<arr[mid+1] and arr[mid]<arr[l]):
		right = mid