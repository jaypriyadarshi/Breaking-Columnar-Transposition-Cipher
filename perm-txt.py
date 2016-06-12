f = open('input.txt','r')
f1 = open('out5.txt','r')
corrupted = f.readlines();
order = [18,8,4,24,43,23,11,10,6,13,47,15,27,46,3,49,36,48,9,34,30,50,45,32,7,38,29,37,5,44,2,39,41,33,21,40,19,31,1,26,20,14,35,12,42,17,16,25,22,28]
order1 = f1.readlines()

order2 = []
for j in order1:
	order1 = order1[:-1]
	order2.append(int(j))
#print order2
orginal = []
#print corrupted
for j in range(10):
	orginal.append('')

j=0

#order2 = [12, 5, 9, 10, 22, 42, 23, 3, 7, 17]
#order2 = [17, 7, 3, 23, 0, 46, 30, 8, 18, 11, 1, 42, 26, 6, 15, 4, 41, 36, 28, 20, 39, 32, 12, 38, 49, 34, 21, 2, 33, 29, 27, 43, 10, 37, 35, 44, 31, 45, 9, 5, 47, 14, 25, 13, 22, 40, 19, 24, 16, 48]
#order2 = [40, 32, 20, 3, 27, 29, 41, 4, 43, 1, 38, 18, 30, 0, 15, 24, 22, 10, 36, 6, 37, 28, 31, 35, 12, 39, 49, 8, 11, 34, 21, 44, 42, 33, 2, 48, 26, 47, 23, 14, 9, 5, 25, 19, 13, 46, 16, 45, 7, 17]
#order2 = [17, 7, 3, 23, 0, 46, 30, 8, 18, 11]
order2 = [17, 7, 23, 42, 10, 9, 12, 5, 22, 3]
for index in order2:
	for j in range(10):
		orginal[j] += corrupted[j][index]

for data in orginal:
	print data
	
	
	
		
	
	
