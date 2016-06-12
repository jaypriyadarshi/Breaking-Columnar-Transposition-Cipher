f = open('corpus.en','r')
f2 = open('corpus/ch1.txt','r')
f3 = open('corpus/ch2.txt','r')
f4 = open('corpus/ch3.txt','r')
f5 = open('corpus/ch6.txt','r')
f6 = open('corpus/ch7.txt','r')
f7 = open('corpus/ch8.txt','r')
f8 = open('corpus/ch9.txt','r')
f9 = open('corpus/ch14.txt','r')
f10 = open('corpus/ch15.txt','r')
f11 = open('corpus/ch11.txt','r')
f12 = open('corpus/ch12.txt','r')
f13 = open('corpus/ch13.txt','r')
f14 = open('corpus/CH4.txt','r')
f15 = open('corpus/DraftRecom-PDF.txt','r')
f16 = open('corpus/Session2-PDF.txt','r')
f17 = open('corpus/Session3-PDF.txt','r')
f18 = open('corpus/Session4-PDF.txt','r')

f19 = open('corpus/journal.pbio.0020001.txt','r')
f20 = open('corpus/journal.pbio.0020010.txt','r')
f21 = open('corpus/journal.pbio.0020012.txt','r')
f22 = open('corpus/journal.pbio.0020013.txt','r')
f23 = open('corpus/journal.pbio.0020019.txt','r')
f24 = open('corpus/journal.pbio.0020028.txt','r')
f25 = open('corpus/journal.pbio.0020043.txt','r')
f26 = open('corpus/journal.pbio.0020046.txt','r')
f27 = open('corpus/journal.pbio.0020047.txt','r')

data10 = f.readlines()
data1 = f2.readlines()
data2 = f3.readlines()
data3 = f4.readlines()
data4 = f5.readlines()
data5 = f6.readlines()
data6 = f7.readlines()
data7 = f8.readlines()
data8 = f9.readlines()
data9 = f10.readlines()
data11 = f11.readlines()
data12 = f12.readlines()
data13 = f13.readlines()
data14 = f14.readlines()
data15 = f15.readlines()
data16 = f16.readlines()
data17 = f17.readlines()
data18 = f18.readlines()

data19 = f19.readlines()
data20 = f20.readlines()
data21 = f21.readlines()
data22 = f22.readlines()
data23 = f23.readlines()
data24 = f24.readlines()
data25 = f25.readlines()
data26 = f26.readlines()
data27 = f27.readlines()

lis = ['corpus/journal.pbio.0020047.txt','corpus/journal.pbio.0020035.txt','corpus/journal.pbio.0020040.txt','corpus/journal.pbio.0020042.txt','corpus/journal.pbio.0020052.txt','corpus/journal.pbio.0020053.txt','corpus/journal.pbio.0020054.txt','corpus/journal.pbio.0020063.txt','corpus/journal.pbio.0020064.txt','corpus/journal.pbio.0020067.txt','corpus/journal.pbio.0020068.txt','corpus/journal.pbio.0020071.txt','corpus/journal.pbio.0020073.txt','corpus/journal.pbio.0020105.txt','corpus/journal.pbio.0020112.txt','corpus/journal.pbio.0020113.txt','corpus/journal.pbio.0020116.txt','corpus/journal.pbio.0020121.txt','corpus/journal.pbio.0020127.txt','corpus/journal.pbio.0020133.txt','corpus/journal.pbio.0020140.txt']
data29 = []
for l in lis:
	f28 = open(l,'r')
	data28 = f28.readlines()
	data29 += data28


data = data10+data1+data2+data3+data4+data5+data6+data7+data8+data9+data11+data12+data13+data14+data15+data16+data17+data18+data19+data20+data21+data22+data23+data24+data25+data26+data27+data29
data = f.readlines()

f1 = open('count1.py','w')
count={'a':{},'b':{},'c':{},'d':{},'e':{},'f':{},'g':{},'h':{},'i':{},'j':{},'k':{},'l':{},'m':{},'n':{},'o':{},'p':{},'q':{},'r':{},'s':{},'t':{},'u':{},'v':{},'w':{},'x':{},'y':{},'z':{}}

first = True
for i in data:
	j = i.split(" ")
	for k in j:
		k = k.lower()
		length = len(k)
		for l in range(length):
			if k[l].isalpha():
				if l != length-1:
					if first == False:
						if k[l] in count[prev].keys():
							count[prev][k[l]] += 1
						else:
							count[prev][k[l]] = 1

					if k[l+1].isalpha():
						if k[l+1] in count[k[l]].keys():
							count[k[l]][k[l+1]] += 1
						else:
							count[k[l]][k[l+1]] = 1
						las_char = k[l]
				else:
					if k[l].isalpha(): 					
						prev = k[l]
					else:
						if k[l-1].isalpha():						
							prev = k[l-1]
						else:
							prev = las_char
		first = False

Ap = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
for a in count.iterkeys():
	for alp in Ap:
		if alp not in count[a]:
			count[a][alp] = 1		

total = 0
for a in count.iterkeys():
	for b in count[a].iterkeys():
		total += count[a][b]

for a in count.iterkeys():
	for b in count[a].iterkeys():
		count[a][b] = float(count[a][b])/total	

s = "count = "+str(count)

f1.write(s)

f1.close()
f.close()
			
		
				
				
		
