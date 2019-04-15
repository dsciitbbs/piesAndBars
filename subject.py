import json
from graphIt import sanitize

def transform(val):
	#Change aphabetical grades to numeric
	for index,value in enumerate(val):
		if value=='EX':
			val[index]=10
		elif value=='A':
			val[index]=9;
		elif value=='B':
			val[index]=8;
		elif value=='C':
			val[index]=7
		elif value=='D':
			val[index]=6
		elif value=='P':
			val[index]=5
		else:
			val[index]=0
	return val

def get_subject(code):
	"""TODO-Find max,min of each subject"""
	with open('dataset.json') as f:
		text=f.read()
		r=json.loads(text)
	name=[]
	roll=[]
	val={}
	for key,value in r.items():
		t=r[key]["grades"]
		for k1,v1 in t.items():
			if code in t[k1].keys():
				x=t[k1][code]
				year=key[0:2]
				if year not in val.keys():
					val[year]=[];
				val[year].append(x);
	for key,value in val.items():
		x=transform(value)
		val[key]=x
	return val