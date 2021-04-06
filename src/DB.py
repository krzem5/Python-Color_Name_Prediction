import os



class DB:
	def __init__(self,d):
		self.d=d
		if (os.path.exists(self.d)):
			open(self.d,"a").close()
		else:
			open(self.d,"w").close()
		self.ni=self.getNi()
	def write(self,v,c):
		f=open(self.d,"a")
		f.write(f"{self.ni}:{v}:{c}\n")
		f.close()
		self.ni+=1
	def fetch(self,di):
		for l in open(self.d,"r"):
			s=l.replace('\n','').split(':')
			if s[0]==str(di):return s[1:]
		return ["",""]
	def getNi(self):
		i=0
		for l in open(self.d,"r"):
			if l!="":i+=1
		return i
	def all(self):
		l=[]
		for ln in open(self.d,"r"):
			l+=[ln.replace('\n','').split(':')[1:]]
		return l
	def count(self,seq):
		vc=0 if seq.startswith("#") else 1
		occ=0
		for c in self.all():
			if c[vc]==seq:occ+=1
		return occ
