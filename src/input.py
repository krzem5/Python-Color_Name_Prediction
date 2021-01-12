from tkinter import *
import DB
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
def main():
	tk=Tk()
	tk.resizable(0,0)
	tk.title("Color Input")
	label=Label(tk,relief='groove',bg=randC(),width=50,height=25)
	print(database.ni)
	for c in range(len(COLORS)):
		def cmd(x=COLORS[c]):
			database.write(label["bg"],x)
			label["bg"]=randC()
			print(database.ni)
		cl="white" if COLORS[c] in ["purple","black","blue","red","green","brown"] else "black"
		Button(tk,command=cmd,text=COLORS[c]+"-ish",bg=COLORS[c],fg=cl).pack(padx=0,pady=0)
	label.pack()
	tk.mainloop()
if __name__=='__main__':
	main()