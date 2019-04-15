import json
import mechanicalsoup

def sanitize(vals):
	#Filter out unknown values; set withheld grades to 0"
	for idx,val in enumerate(vals):
		if val is None:
		    vals[idx]='CGPA:0.0'
		elif 'WH' in val:
			vals[idx]='CGPA:0.0'
		elif len(val)==0:
			vals[idx]='CGPA:0.0'

def fill(rolls,last_index,branches,r):
	i=1
	while i<46:
		if len(str(i))<2:
			h='0'+str(i)
		else:
			h=str(i)
		i=i+1
		rolls.append(h)
	for branch in branches:
		last_known=""
		for roll in rolls:
			regno="14"+branch+"010"+roll
			if regno not in r:
				continue
			last_known=regno
		last_index.append(last_known)

def res(rolls,branches,r,last_index):
	#Run if scraping needed
	print("{")
	i=0
	for branch in branches:
		print("\""+branch+"\":[")
		for roll in rolls:
			browser=mechanicalsoup.StatefulBrowser()
			browser.open('http://14.139.195.241/Result/login.php')
			browser.select_form()
			regno="14"+branch+"010"+roll
			browser["regno"]=regno
			if regno not in r:
				continue
			browser["dob"]=r[regno]["dob"]
			response=browser.submit_selected()
			browser.open("http://14.139.195.241/Result/result.php")
			x=browser.get_current_page().find_all(align='right')
			if len(x)==0:
				continue
			values=dict()
			k=1;
			for value in x:
				values[str(k)]=value.text[0:9]
				k=k+1
			if last_index[i]!=regno:
				print("{\"name\":\""+r[regno]["name"]+"\",\"roll\":\""+regno+"\",\"grades\":"+json.dumps(values)+"},")
			else:
				print("{\"name\":\""+r[regno]["name"]+"\",\"roll\":\""+regno+"\",\"grades\":"+json.dumps(values)+"}")
		if i!=5:
			print("],");
		else:
			print("]");
		i=i+1
	print("}")

'''def get_CGPA(year):
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
	with open ('out'+year+'_CGPA.txt') as f:
		text=f.read()
		r=json.loads(text)
	if int(year)==14:
		for key,value in r.items():
			for val in r[key]:
				name.append(val["name"])
				roll.append(val["roll"])
				s1.append(val["grades"].get("1"))
				s2.append(val["grades"].get("2"))
				s3.append(val["grades"].get("3"))
				s4.append(val["grades"].get("4"))
				s5.append(val["grades"].get("5"))
				s6.append(val["grades"].get("6"))
				s7.append(val["grades"].get("7"))
				s8.append(val["grades"].get("8"))
	elif int(year)==15:
		for key,value in r.items():
			for val in r[key]:
				name.append(val["name"])
				roll.append(val["roll"])
				s1.append(val["grades"].get("1"))
				s2.append(val["grades"].get("2"))
				s3.append(val["grades"].get("3"))
				s4.append(val["grades"].get("4"))
				s5.append(val["grades"].get("5"))
				s6.append(val["grades"].get("6"))
				s7.append(val["grades"].get("7"))
	elif int(year)==16:
		for key,value in r.items():
			for val in r[key]:
				name.append(val["name"])
				roll.append(val["roll"])
				s1.append(val["grades"].get("1"))
				s2.append(val["grades"].get("2"))
				s3.append(val["grades"].get("3"))
				s4.append(val["grades"].get("4"))
				s5.append(val["grades"].get("5"))
	elif int(year)==17:
		for key,value in r.items():
			for val in r[key]:
				name.append(val["name"])
				roll.append(val["roll"])
				s1.append(val["grades"].get("1"))
				s2.append(val["grades"].get("2"))
				s3.append(val["grades"].get("3"))
	#print(s5)
	#print(len(name),len(s1),len(s2),len(s3),len(s4),len(s5),len(roll))
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
		return [s1,s2,s3,highs,roll,name]'''

def get_CGPA(year):
	'''rolls=[]
	last_index=[]
	with open('result-data-export.json') as f:
		text=f.read()
		r=json.loads(text)
	branches=['CE', 'CS', 'ME', 'MM', 'EE', 'EC']
	#fill(rolls,last_index,branches,r)
	#res(rolls,branches,r,last_index)'''
	with open('dataset.json') as f:
		text=f.read()
		r=json.loads(text)
	name=[]
	roll=[]
	"""s1-s8 stores the grades of semester 1 to 8, in order.
	name[i],roll[i] and s1[i]-s8[i] give complete information about a person"""
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
			p=r[key]["cgpa"]
			if int(key[0:2])!=int(year):
				continue
			while len(p)<8:
				p.append("WH")
			name.append(r[key]["name"])
			roll.append(str(key))
			s1.append('CGPA:'+str(p[0]))
			s2.append('CGPA:'+str(p[1]))
			s3.append('CGPA:'+str(p[2]))
			s4.append('CGPA:'+str(p[3]))
			s5.append('CGPA:'+str(p[4]))
			s6.append('CGPA:'+str(p[5]))
			s7.append('CGPA:'+str(p[6]))
			s8.append('CGPA:'+str(p[7]))
	elif int(year)==15:
		for key,value in r.items():
			p=r[key]["cgpa"]
			if int(key[0:2])!=int(year):
				continue
			while len(p)<8:
				p.append("WH")
			name.append(r[key]["name"])
			roll.append(str(key))
			s1.append('CGPA:'+str([0]))
			s2.append('CGPA:'+str(p[1]))
			s3.append('CGPA:'+str(p[2]))
			s4.append('CGPA:'+str(p[3]))
			s5.append('CGPA:'+str(p[4]))
			s6.append('CGPA:'+str(p[5]))
			s7.append('CGPA:'+str(p[6]))
	elif int(year)==16:
		for key,value in r.items():
			p=r[key]["cgpa"]
			if int(key[0:2])!=int(year):
				continue
			while len(p)<8:
				p.append("WH")
			name.append(r[key]["name"])
			roll.append(str(key))
			#print(p[0]+","+p[1]+","+p[2]+","+","+p[3]+","+p[4]+","+str(key))
			s1.append('CGPA:'+str(p[0]))
			s2.append('CGPA:'+str(p[1]))
			s3.append('CGPA:'+str(p[2]))
			s4.append('CGPA:'+str(p[3]))
			s5.append('CGPA:'+str(p[4]))
	elif int(year)==17:
		for key,value in r.items():
			p=r[key]["cgpa"]
			if int(key[0:2])!=int(year):
				continue
			while len(p)<8:
				p.append("WH")
			name.append(r[key]["name"])
			roll.append(str(key))
			#print(p[0]+","+p[1]+","+p[2]+","+str(key))
			s1.append('CGPA:'+str(p[0]))
			s2.append('CGPA:'+str(p[1]))
			s3.append('CGPA:'+str(p[2]))
	#handle unusual values
	sanitize(s1)
	sanitize(s2)
	sanitize(s3)
	sanitize(s4)
	sanitize(s5)
	sanitize(s6)
	sanitize(s7)
	sanitize(s8)
	highs=[]
	#Find who scored the maximum
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
	#Strip text, only store number
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