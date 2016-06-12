from random import random
import random
import math
from count1 import count 
from count_let import let_freq
from tri import tri
import operator
import itertools

mat = {}

f = open('input.txt','r')
f1 = open('prob_mat.py','w')
f2= open('out7.txt','w')
ciphertext  = f.readlines()
"""
def cost(ans):
	orginal = []
	D = {'a':{},'b':{},'c':{},'d':{},'e':{},'f':{},'g':{},'h':{},'i':{},'j':{},'k':{},'l':{},'m':{},'n':{},'o':{},'p':{},'q':{},'r':{},'s':{},'t':{},'u':{},'v':{},'w':{},'x':{},'y':{},'z':{}}
	#print corrupted
	for j in range(10):
		orginal.append('')
	j=0
	for i in ans:
		for j in range(10):
			orginal[j] += ciphertext[j][i]

	#calculate deciphered text statistics:
	for i in range(10):
		for j in range(50):
			if j!=49:
				if orginal[i][j+1] in D[orginal[i][j]]:
					D[orginal[i][j]][orginal[i][j+1]] += 1
				else:
					D[orginal[i][j]][orginal[i][j+1]] = 1

	total = 0
	for a in D.iterkeys():
		for b in D[a].iterkeys():
			total += D[a][b]

	for a in D.iterkeys():
		for b in D[a].iterkeys():
			D[a][b] = float(D[a][b])/total

	A = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']		
	score_ans = 0

	for i in A:
		for j in A:
			if j in count[i] and j in D[i]:
				score_ans += abs(count[i][j]-D[i][j])
			elif j in count[i] and j not in D[i]:
				score_ans += count[i][j]
			else:
				pass
	for i in range(49):
		try:
			score_ans += abs()
		except:
			score_ans += -1000

	return score_ans
"""

def acceptance_probability(c_old,c_new,T):
	return math.exp(-1*((c_new-c_old)/T))

def permute_key(sol):

	#toss = random.randint(0,1)

	#if toss == 1:
	x = random.randint(0,49)
	y = random.randint(0,49)
	if y == x:
		y = random.randint(0,49)
	temp = sol[x]
	sol[x] = sol[y]
	sol[y] = temp
	"""
	else:
		x = random.randint(0,49)
		y = random.randint(0,49)
		if y == x:
			y = random.randint(0,49)
		if x > y:
			temp = y
			y = x
			x = temp
		r = random.randint(0,(y-x))
		first = sol[:x]
		last = sol[y+1:]
		middle = sol[x:y+1]
		middle = middle[r:]+middle[:r]
		sol = first+middle+last
	"""
	return sol

def exp_schedule(k=20, lam=0.005, limit=100):
    #"One possible schedule function for simulated annealing"
    return lambda t: if_(t < limit, k * math.exp(-lam * t), 0)

def anneal(solution):
	old_cost = cost(solution)
	T = 1000000000000000000000.0
	#T = 1.00
	T_min = 0.00000000000000000000001
	#T_min = 0.0001
	alpha = 0.9
	while T > T_min:
		i = 0
		N = 0

		while i <= 100*50:
			#print T
			new_solution = permute_key(solution)
			#print i
			new_cost = cost(new_solution)
			if (new_cost - old_cost) < 0:
				solution = new_solution
				old_cost = new_cost
				#N += 1
			else:
				ap = acceptance_probability(old_cost,new_cost,T)
				if ap > 0.5:
					solution = new_solution
					old_cost = new_cost
					#N += 1
			#if N > 10*50:
				#break
			i += 1
		#if N == 0:
			#return solution, old_cost	
		T = T*alpha
	return solution, old_cost

def score(c,d,e):
	res = float(tri[c][d][e])/count[c][d]
	return res

def sol_cost(ans):
	orginal = []
	#D = {'a':{},'b':{},'c':{},'d':{},'e':{},'f':{},'g':{},'h':{},'i':{},'j':{},'k':{},'l':{},'m':{},'n':{},'o':{},'p':{},'q':{},'r':{},'s':{},'t':{},'u':{},'v':{},'w':{},'x':{},'y':{},'z':{}}
	#print corrupted
	for j in range(10):
		orginal.append('')
	j=0
	for i in ans:
		for j in range(10):
			orginal[j] += ciphertext[j][i]

	val = 0
	for i in range(10):
		for j in range(8):
			val += -1*math.log(score(orginal[i][j],orginal[i][j+1],orginal[i][j+2]))

	return val

def maximum():
	ind1 = -1
	ind2 = -1
	ind3 = -1
	m = float("-inf")
	for i in mat.iterkeys():
		for j in mat[i].iterkeys():
			ind = max(mat[i][j].iteritems(), key = operator.itemgetter(1))[0]
			if mat[i][j][ind] > m:
				m = mat[i][j][ind]
				ind3 = ind
				ind2 = j
				ind1 = i
	return ind1,ind2,ind3,m

def next_max(r,o,tempo):
	#ind = max(mat[o].iteritems(), key = operator.itemgetter(1))[0]
	ind = -1
	m = float("-inf")
	for i in mat[r][o].iterkeys():
		if m < mat[r][o][i]:
			if i not in tempo:
				m = mat[r][o][i]
				ind = i
	return ind


def greedy():
	greedy_key = []
	start,second_las,end,m = maximum()
	greedy_key.append(start)
	greedy_key.append(second_las)
	greedy_key.append(end)
	for i in range(7):
		tempo = greedy_key[:]
		next_ele = next_max(second_las,end,tempo)
		greedy_key.append(next_ele)
		second_las = end
		end = next_ele
	return greedy_key


nums = [i for i in range(50)]
for number in nums:
	mat[number] = {}

for i in mat.iterkeys():
	for j in nums:
		mat[i][j] = {}


for data in ciphertext:
	data = data[:-1]
	#print data
	i=0
	j=0
	k=0
	for i in range(50):
		d = data[i]
		j = 0
		while j <50:
			g = data[j]
			q = 0
			while q < 50:
			#calulating if digram or the two letter are far away has more probability of occuring
				h = data[q]
				if i != j and j!=q:
					if q in mat[i][j].keys():
						mat[i][j][q] *= score(d,g,h)
					else:
						mat[i][j][q] = score(d,g,h)
				else:
					mat[i][j][q] = -100000
				q += 1
			j += 1

s = "mat ="+str(mat)
f1.write(s)
f1.close()
f.close()

answer = [17,7,3,23,42,22,10,9,5,12]

gold = sol_cost(answer)
print gold

perms = list(itertools.permutations([17,7,3,23,42,22,10,9,5,12]))

minim = float("inf")
for per in perms:
	score_exhaust = sol_cost(per)
	if score_exhaust < minim:
		minim = score_exhaust
		answer_exh = per
print answer_exh, minim
"""
greedy_sol = greedy()
greedy_val = sol_cost(greedy_sol) 
print greedy_sol
print greedy_val
"""
#key = [i for i in range(50)]
#random.shuffle(key)
#print key
#key = [17, 29, 48, 13, 0, 30, 26, 2, 20, 19, 43, 46, 41, 37, 44, 10, 27, 6, 22, 42, 18, 11, 28, 15, 24, 7, 49, 3, 9, 34, 38, 4, 8, 21, 47, 14, 16, 32, 36, 35, 1, 12, 5, 33, 39, 45, 25, 23, 31, 40]
#answer,final_cost = anneal(key)
#answer = [17,7,3,23,42,22,10,9,5,12,46,14,26,45,2,48,35,47,8,33,29,49,44,31,6,37,28,36,4,43,1,38,40,32,20,39,18,30,0,25,19,13,34,11,41,16,15,24,21,27]
#print answer, final_cost

