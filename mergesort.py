def merge(left, right):
	
	left_index, right_index = 0, 0
	helper = []
	
	while left_index < len(left) and right_index < len(right):
		
		if left[left_index] < right[right_index]:
			
			helper.append(left[left_index])
			left_index += 1
		
		else:
			
			helper.append(right[right_index])
			right_index += 1
	
	helper += left[left_index:]
	helper += right[right_index:]
	
	print("next step: " + str(helper))
	
	return helper

def merge_sort(data):
	
	if len(data) <= 1:
		return data
	
	half = len(data) // 2
	left = merge_sort(data[:half])
	right = merge_sort(data[half:])
	
	return merge(left, right)

data = [10, 2, 3, 5, 6, 1, 8, 9]
print("start: " + str(data))
data = merge_sort(data)