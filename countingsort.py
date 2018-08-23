def counting_sort(data):
	
	m = max(data) + 1
	counter = [0] * m
	
	for i in data:
		
		counter[i] += 1
	
	j = 0
	
	for key in range(m):
		for c in range(counter[key]):
			
			data[j] = key
			j += 1
	
	print("next step: " + str(data))
	
	return data

data = [10, 2, 3, 5, 6, 1, 8, 9]
print("start: " + str(data))
data = counting_sort(data)