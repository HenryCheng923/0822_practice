

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
	allen_word_count = 0
	viki_word_count = 0
	allen_sticker_count = 0
	viki_sticker_count = 0
	allen_image_count = 0
	viki_image_count = 0
	for line in lines:
		s = line.split(' ')
		time = s[0]
		name = s[1]
		if name == 'Allen':
			if s[2] =='貼圖':
				allen_sticker_count += 1
			elif s[2] == '圖片':
				allen_image_count += 1
			else:
				for msg in s[2:]:
					allen_word_count += len(msg)
		elif name == 'Viki':
			if s[2] == '貼圖':
				viki_sticker_count += 1
			elif s[2] == '圖片':
				viki_image_count += 1
			else:
				for msg in s[2:]:
					viki_word_count += len(msg)
	print('allen說了： ',allen_word_count,'Allen傳了',allen_sticker_count,'貼圖','Allen傳了',allen_image_count,'圖片')
	print('Vike說了： ',viki_word_count,'Viki傳了',viki_sticker_count,'貼圖','Viki傳了',viki_image_count,'圖片')

def main():
	lines = read_input('-LINE-Viki.txt')
	new = convert(lines)
	#write_output('output.txt',new)
	#print(new)

main()