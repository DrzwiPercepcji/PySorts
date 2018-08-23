def selection_sort(data):
	
	for i in range(len(data) - 1):
		
		min_value = min(data[i:])
		min_index = data[i:].index(min_value)
		
		if i == i + min_index:
			continue
		
		data[i + min_index] = data[i]
		data[i] = min_value
		
		print("next step: " + str(data))
	
	return data

data = [10, 2, 3, 5, 6, 1, 8, 9]
print("start: " + str(data))
data = selection_sort(data)