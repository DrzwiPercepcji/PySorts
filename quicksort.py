def quick_sort(data, left, right):
	
	if len(data) <= 1:
		return data
	
	i = left
	j = right
	
	pivot = data[(left + right) // 2]
	
	while i < j:
		
		while data[i] < pivot:
			i += 1
		
		while data[j] > pivot:
			j -= 1
		
		if i < j:
			
			temp = data[i]
			data[i] = data[j]
			data[j] = temp
			
			print("next step: " + str(data))
			
		i += 1
		j -= 1
	
	if left < j:
		data = quick_sort(data, left, j)
		
	if i < right:
		data = quick_sort(data, i, right)
	
	return data

data = [10, 2, 3, 5, 6, 1, 8, 9]
print("start: " + str(data))
data = quick_sort(data, 0, len(data) - 1)