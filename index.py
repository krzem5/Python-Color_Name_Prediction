from tkinter import *
import DB
import math
import random



CHARS=list("0123456789abcdef")
COLORS="black,brown,red,green,blue,yellow,orange,purple,pink,white,gray".split(',')
COLORS.sort()
database=DB.DB("./colors.txt")
def randC():
	seq="#"
	for _ in range(6):
		seq+=random.choice(CHARS)
	return seq
def guess(c):
	def calc_s(c2,c1):
		s=[]
		for i in range(1,7):
			s+=[abs(CHARS.index(c2[i])-CHARS.index(c1[i]))]
		return sum(s)
	def pick(possible):
		l=[]
		for c in COLORS:l+=[[c,0]]
		for p in possible:
			l[COLORS.index(p[1])][1]+=1
		ls=sorted(l,key=lambda v:v[1]>>0,reverse=True)
		return ls[0][0]
	possible=[database.fetch(0)+[calc_s(c,database.fetch(0)[0])]]
	for p in database.all():
		s=calc_s(c,p[0])
		if s<possible[0][2]:possible=[p+[s]]
		elif s==possible[0][2]:possible+=[p+[s]]
	gc=pick(possible)
	return gc
def main():
	tk=Tk()
	tk.resizable(0,0)
	tk.title("Color Input")
	label=Label(tk,relief='groove',bg="#000000",text="",width=50,height=25)
	global totn,okn
	totn=0
	okn=0
	def end():
		print(f"Total guesses:\t{totn}\nTotla good guesses:\t{okn}\t({math.ceil(okn/totn*1000)/10}%)\nTotal wrong guesses:\t{totn-okn}\t({math.ceil((totn-okn)/totn*1000)/10}%)\nBilans:\t{okn-(totn-okn)}")
		tk.destroy()
	Button(tk,bg="deepskyblue",text="END",command=end).pack()
	def bad():
		global totn,okn
		database.write(label["bg"],input("What color is that?"))
		print("not ok")
		label["bg"]=randC()
		label["text"]=guess(label["bg"])+"-ish"
		totn+=1
	Button(tk,bg="red",text="WRONG",command=bad).pack()
	def ok():
		global totn,okn
		database.write(label["bg"],label["text"].replace("-ish",""))
		print("ok")
		label["bg"]=randC()
		label["text"]=guess(label["bg"])+"-ish"
		totn+=1
		okn+=1
	Button(tk,bg="lime",text="CORRECT",command=ok).pack()
	label["bg"]=randC()
	label["text"]=guess(label["bg"])+"-ish"
	label.pack()
	tk.mainloop()
if __name__=='__main__':
	main()
