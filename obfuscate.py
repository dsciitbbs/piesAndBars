import json
from random import shuffle,randint
from cryptography.fernet import Fernet
from pathlib import Path
import sys
import os

def FernetEncrypt(message, cipher):

	message = message.encode('utf-8')
	#cipher = Fernet(cipher_key)
	encrypted_text = cipher.encrypt(message)

	#decrypted_text = cipher.decrypt(encrypted_text)

	return encrypted_text.decode('utf-8')


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


def obfuscate(policy):
	with open('result-data-export.json') as f:
		t=f.read()
		x=json.loads(t)
	data={}
	if(policy=="General"):
		for key,value in x.items():
			p=key[0:7]+str(int(key[7:9])+randint(1,7)*randint(1,21))[0:2]#change rollno
			r=10
			while p in data.keys():
				p=p[0:7]+str(r)
				r=r+1
			data[p]=value
			data[p]['name']=change(value['name'].upper())
			data[p]['dob']=change2(value['dob'])

	elif(policy=="Fernet"):
		#my_file = Path("Keys.json")
		present = False
		Encryption_dict = {}
		if os.path.exists("Keys.json"):
			with open("Keys.json", 'r') as file:
				Encryption_list = file.read()
			try:
				Encryption_dict = json.loads(Encryption_list)
				if "Fernet" in Encryption_dict.keys():
					present = True
			except Exception as e:
				print("Not JSON")

		if not present:
			#print(dir(Fernet))
			cipher_key = Fernet.generate_key()
			Encryption_dict["Fernet"] = cipher_key.decode('utf-8')
			with open("Keys.json", 'w') as file:
				file.write(json.dumps(Encryption_dict))
		else:
			cipher_key = Encryption_dict["Fernet"].encode('utf-8')
		cipher = Fernet(cipher_key)
		for key,value in x.items():
			p = FernetEncrypt(key, cipher)
			data[p]=value
			data[p]['name']=FernetEncrypt(value['name'].upper(), cipher)
			data[p]['dob']=FernetEncrypt(value['dob'], cipher)

	with open('dataset.json','w') as f:
		json.dump(data,f)

if __name__ == '__main__':
	obfuscate(sys.argv[1])
