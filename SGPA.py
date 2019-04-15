import json
from graphIt import sanitize

def get_SGPA(year):
	with open('dataset.json') as f:
		text=f.read()
		r=json.loads(text)
	name=[]
	roll=[]
	s1=[]
	s2=[]
	s3=[]
	s4=[]
	s5=[]
	s6=[]
	s7=[]
	s8=[]
	if int(year)==14:
		for key,value in r.items():
			p=r[key]["sgpa"]
			if int(key[0:2])!=int(year):
				continue
			while len(p)<8:
				p.append("WH")
			name.append(r[key]["name"])
			roll.append(str(key))
			s1.append('SGPA:'+str(p[0]))
			s2.append('SGPA:'+str(p[1]))
			s3.append('SGPA:'+str(p[2]))
			s4.append('SGPA:'+str(p[3]))
			s5.append('SGPA:'+str(p[4]))
			s6.append('SGPA:'+str(p[5]))
			s7.append('SGPA:'+str(p[6]))
			s8.append('SGPA:'+str(p[7]))
	elif int(year)==15:
		for key,value in r.items():
			p=r[key]["sgpa"]
			if int(key[0:2])!=int(year):
				continue
			while len(p)<8:
				p.append("WH")
			name.append(r[key]["name"])
			roll.append(str(key))
			s1.append('SGPA:'+str([0]))
			s2.append('SGPA:'+str(p[1]))
			s3.append('SGPA:'+str(p[2]))
			s4.append('SGPA:'+str(p[3]))
			s5.append('SGPA:'+str(p[4]))
			s6.append('SGPA:'+str(p[5]))
			s7.append('SGPA:'+str(p[6]))
	elif int(year)==16:
		for key,value in r.items():
			p=r[key]["sgpa"]
			if int(key[0:2])!=int(year):
				continue
			while len(p)<8:
				p.append("WH")
			name.append(r[key]["name"])
			roll.append(str(key))
			#print(p[0]+","+p[1]+","+p[2]+","+","+p[3]+","+p[4]+","+str(key))
			s1.append('SGPA:'+str(p[0]))
			s2.append('SGPA:'+str(p[1]))
			s3.append('SGPA:'+str(p[2]))
			s4.append('SGPA:'+str(p[3]))
			s5.append('SGPA:'+str(p[4]))
	elif int(year)==17:
		for key,value in r.items():
			p=r[key]["sgpa"]
			if int(key[0:2])!=int(year):
				continue
			while len(p)<8:
				p.append("WH")
			name.append(r[key]["name"])
			roll.append(str(key))
			#print(p[0]+","+p[1]+","+p[2]+","+str(key))
			s1.append('SGPA:'+str(p[0]))
			s2.append('SGPA:'+str(p[1]))
			s3.append('SGPA:'+str(p[2]))
	sanitize(s1)
	sanitize(s2)
	sanitize(s3)
	sanitize(s4)
	sanitize(s5)
	sanitize(s6)
	sanitize(s7)
	sanitize(s8)
	highs=[]
	m=max(s1)
	t=[i for i, j in enumerate(s1) if j == m]
	for val in t:
		highs.append("Semester 1: "+name[val]+","+roll[val]+","+s1[val])
	m=max(s2)
	t=[i for i, j in enumerate(s2) if j == m]
	for val in t:
		highs.append("Semester 2: "+name[val]+","+roll[val]+","+s2[val])
	m=max(s3)
	t=[i for i, j in enumerate(s3) if j == m]
	for val in t:
		highs.append("Semester 3: "+name[val]+","+roll[val]+","+s3[val])
	if int(year)<=16:
		m=max(s4)
		t=[i for i, j in enumerate(s4) if j == m]
		for val in t:
			highs.append("Semester 4: "+name[val]+","+roll[val]+","+s4[val])
	if int(year)<=16:
		m=max(s5)
		t=[i for i, j in enumerate(s5) if j == m]
		for val in t:
			highs.append("Semester 5: "+name[val]+","+roll[val]+","+s5[val])
	if int(year)<=15:
		m=max(s6)
		t=[i for i, j in enumerate(s6) if j == m]
		for val in t:
			highs.append("Semester 6: "+name[val]+","+roll[val]+","+s6[val])
	if int(year)<=15:
		m=max(s7)
		t=[i for i, j in enumerate(s7) if j == m]
		for val in t:
			highs.append("Semester 7: "+name[val]+","+roll[val]+","+s7[val])
	if int(year)<=14:
		m=max(s8)
		t=[i for i, j in enumerate(s5) if j == m]
		for val in t:
			highs.append("Semester 8: "+name[val]+","+roll[val]+","+s8[val])
	print(s1)
	s1=[float(v[5:]) for v in s1]
	s2=[float(v[5:]) for v in s2]
	s3=[float(v[5:]) for v in s3]
	s4=[float(v[5:]) for v in s4]
	s5=[float(v[5:]) for v in s5]
	s6=[float(v[5:]) for v in s6]
	s7=[float(v[5:]) for v in s7]
	s8=[float(v[5:]) for v in s8]
	if int(year)==14:
		return [s1,s2,s3,s4,s5,s6,s7,s8,highs,roll,name]
	elif int(year)==15:
		return [s1,s2,s3,s4,s5,s6,s7,highs,roll,name]
	elif int(year)==16:
		return [s1,s2,s3,s4,s5,highs,roll,name]
	elif int(year)==17:
		return [s1,s2,s3,highs,roll,name]