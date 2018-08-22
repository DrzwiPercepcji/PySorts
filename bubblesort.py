def bubble_sort(data):
	for i in range(len(data)):
		j = len(data) - 1
		
		while j > i:
			if data[j] < data[j-1]:
				temp = data[j]
				
				data[j] = data[j-1]
				data[j-1] = temp
				
				print("next step: " + str(data))
			j -= 1
	return data

data = [10, 2, 3, 5, 6, 1, 8, 9]
print("start: " + str(data))
data = bubble_sort(data)