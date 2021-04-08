import os



class DB:
	def __init__(self,d):
		self.d=d
		if (not os.path.exists(self.d)):
			with open(self.d,"w") as f:
				f.write("")
		self.ni=self.getNi()
	def write(self,v,c):
		with open(self.d,"a") as f:
			f.write(f"{self.ni}:{v}:{c}\n")
		self.ni+=1
	def fetch(self,di):
		with open(self.d,"r") as f:
			for l in f.read().replace("\r\n","\n").split("\n"):
				s=l.replace('\n','').split(':')
				if s[0]==str(di):return s[1:]
		return ["",""]
	def getNi(self):
		i=0
		with open(self.d,"r") as f:
			for l in f.read().replace("\r\n","\n").split("\n"):
				if l!="":i+=1
		return i
	def all(self):
		l=[]
		with open(self.d,"r") as f:
			for ln in f.read().replace("\r\n","\n").split("\n"):
				l+=[ln.replace('\n','').split(':')[1:]]
		return l
	def count(self,seq):
		vc=0 if seq.startswith("#") else 1
		occ=0
		for c in self.all():
			if c[vc]==seq:occ+=1
		return occ
