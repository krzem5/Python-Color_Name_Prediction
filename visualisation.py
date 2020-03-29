from tkinter import *
import DB
import math



COLORS="black,brown,red,green,blue,yellow,orange,purple,pink,white,gray".split(',')
COLORS.sort()
def print_occ():
	db=DB.DB("./colors.txt")
	print(f"Total items:\t{db.ni}")
	l=[]
	for c in COLORS:
		l+=[[c,db.count(c)]]
	ls=sorted(l,key=lambda v:v[1]>>1,reverse=True)
	for p in ls:
		i="\t" if p[0]=="red" else ""
		print(f"{ls.index(p)+1}. {p[0]}:{i}\t{p[1]}\t({math.ceil(p[1]/db.ni*1000)/10}%)")
def main():
	print_occ()
	tk=Tk()
	tk.resizable(0,0)
	tk.title("Color DB visiuaisation")
	cnv=Canvas(tk,width=850,height=400)
	x=0
	y=0
	for c in DB.DB("./colors.txt").all():
		cnv.create_rectangle(x*10,y*10,(x+1)*10,y*10+10,fill=c[0])
		cnv.create_rectangle(450+x*10,y*10,450+(x+1)*10,y*10+10,fill=c[1])
		x+=1
		if x>=40:
			y+=1
			x=0
	cnv.pack()
	tk.mainloop()
if __name__=='__main__':
	main()