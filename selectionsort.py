def selection_sort(data):
	
	for i in range(len(data)):
		
		j = i + 1
		
		while j < len(data):
			
			if data[i] >= data[j]:
				
				temp = data[i]
				data[i] = data[j]
				data[j] = temp
				
				print("next step: " + str(data))
			
			j += 1
	
	return data

data = [10, 2, 3, 5, 6, 1, 8, 9]
print("start: " + str(data))
data = selection_sort(data)