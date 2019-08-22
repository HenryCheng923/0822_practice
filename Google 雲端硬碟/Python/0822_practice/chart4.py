lines = []
with open('3.txt', 'r', encoding = 'utf-8-sig') as f:
	for line in f:
		lines.append(line.strip())

for line in lines:
	s = line.split(' ')
	time = s[0][:5] #取出時間
	name = s[0][5:] #取出名字
	print(time, ' ', name)