f = open('corpus.en','r')
data = f.readlines()
f1 = open('count_let.py','w')
count_let={}

for i in data:
	j = i.split(" ")
	for k in j:
		k = k.lower()
		for l in k:
			if l.isalpha():
				if l in count_let.keys():
					count_let[l] += 1
				else:
					count_let[l] = 1

total = 0
for a in count_let.iterkeys():
	total += count_let[a]

for a in count_let.iterkeys():
	count_let[a] = float(count_let[a])/total

s = "let_freq = "+str(count_let)
f1.write(s)
f1.close()
f.close()
			
