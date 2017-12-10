file = open('a.txt')
delete_list = ['oraz','się','by','i']
for line in file:
    for word in line.split():
        if word in delete_list:
            line=line.replace(word," ");         
file.close()
print ('./done')
