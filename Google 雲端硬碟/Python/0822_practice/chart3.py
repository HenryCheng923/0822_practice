def read_input(filename):
	lines = []
	with open(filename, 'r', encoding = 'utf-8-sig') as r: #加上sig就可以去除怪符號了
		for line in r:
			lines.append(line.strip())
	return lines	

def write_output(filename, news):
	with open(filename, 'w', encoding = 'utf-8') as w:
		for new in news:
			w.write(new + '\n' )

def convert(lines):
	h_count = 0
	h_img = 0
	h_co_count = 0
	h_msg = 0
	o_count = 0
	o_img = 0
	o_co_count = 0
	o_msg = 0

	for line in lines:
		s = line.split(' ')
		time = s[0]
		name = s[1]
		if name == '鄭治堅':
			h_count += 1
			if s[2] == '貼圖':
				h_img += 1
			elif s[2] == '圖片':
				h_co_count += 1
			else:
				for msg in s[2:]:
					h_msg += len(msg)
		elif name == '許元達':
			o_count	+= 1
			if s[2] == '貼圖':
				o_img += 1
			elif s[2] == '圖片':
				o_co_count += 1
			else:
				for msg in s[2:]:
					o_msg += len(msg)
	
	print("鄭治堅總共發言： ", h_count, '次')
	print("總內容字數有： ", h_msg, '字')
	print("並使用了： ", h_img, '次貼圖')
	print("而傳送了： ", h_co_count, '次圖片' + '\n')

	print("許元達總共發言： ", o_count, '次')
	print("總內容字數有： ", o_msg, '字')
	print("並使用了： ", o_img, '次貼圖')
	print("而傳送了： ", o_co_count, '次圖片')
def main():
	lines = read_input('line.txt')
	new = convert(lines)
	#write_output('output.txt',new)
	#print(lines)

main()