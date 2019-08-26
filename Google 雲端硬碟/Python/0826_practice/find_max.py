def find_max(a_list):
	
	if not a_list:
		return 0
	max_num = a_list[0] #先宣告一個數值給MAX
	for num in a_list:
		if num > max_num:
			max_num = num
	return max_num

print(find_max([1,2,3,4,5]))
print(find_max([1,-1,-5]))
print(find_max([]))