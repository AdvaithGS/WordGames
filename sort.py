f = open("english.txt")
l = []
for i in f:
	x = i.strip()
	if all([ 97 <= ord(j) <= 122 for j in x]) :
		l.append(x)

f = open("english.txt","w")
for i in l:
	f.write(i.lower() + '\n')
f.close()
	
