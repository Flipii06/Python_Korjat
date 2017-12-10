file = open('a.txt')
replaced_list = {'i':'iii','by':'aby','się':'sięę'}
read_lines = ''
for word in file.read().split(' '):
	if not word in dictionary_list:
		read_lines += word + ' '
	else:
		read_lines += repkaced__list[word] + ' '
filech = open('a2.txt', 'w+')
filech.write(read_lines)
file.close()
filech.close()
print ('./done')
