import json
from random import shuffle,randint

def change(p):
	str=""
	for a in p:
		if ord(a)==32:
			str=str+a
			continue
		str=str+chr(((ord(a)-65+randint(1,100))%26)+65)
	return str

def change2(p):
	k=randint(1,12)
	if len(str(k))==1:
		k1="0"+str(k)
	else:
		k1=str(k)
	if k in [1,3,5,7,8,10,12]:
		k2=str(randint(1,31))
	elif k==2:
		k2=str(randint(1,28))
	else:
		k2=str(randint(1,30))
	l=p[0:5]+k1+"-"+k2
	return l


def obfuscate():
	with open('result-data-export.json') as f:
		t=f.read()
		x=json.loads(t)
	data={}
	for key,value in x.items():
		p=key[0:7]+str(int(key[7:9])+randint(1,7)*randint(1,21))[0:2]#change rollno
		r=10
		while p in data.keys():
			p=p[0:7]+str(r)
			r=r+1
		data[p]=value
		data[p]['name']=change(value['name'].upper())
		data[p]['dob']=change2(value['dob'])
	with open('dataset.json','w') as f:
		json.dump(data,f)

obfuscate()