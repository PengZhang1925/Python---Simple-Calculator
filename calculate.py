#!/usr/bin/python
# coding: utf-8

from tkinter import *
#import tkinter
# top = tkinter.Tk()

class calculate:
	def __init__(self,master):
		self.master = master
		self.initWidgets()
		self.hi = None
	
	def initWidgets(self):
		self.show = Label(relief=GROOVE,font=('Courier New',20),\
			width=30,height=5,bg='white',anchor=SE,justify='right',border=0,text='欢迎你使用老子的科学计算器!')
		self.show.pack(side=TOP,pady=10)
		p=Frame(self.master)
		p.pack(side=TOP)
		
		self.attributes = attributes=("AC","±","%","÷","7","8","9","*","4","5","6","-","1","2","3","+","0","00",".","=")
		for i in range(len(attributes)):
			if (i+1)%4 == 0 or attributes[i] == '=': 
				b=Button(p,text=attributes[i],font=('Times New Roman',15),width=10,height=5,bg="dark orange",border=0)
				print(attributes[i])
			elif i<=2: 
				b=Button(p,text=attributes[i],font=('Times New Roman',15),width=10,height=5,bg="light grey",border=0)
				print(attributes[i])
			else :
				b=Button(p,text=attributes[i],font=('Times New Roman',15),width=10,height=5,bg="dark grey",border=0)
				print(attributes[i])
			b.grid(row=i//4,column=i%4)
			b.bind('<Button-1>',self.click)
			print(b)
			if b['text'] == 'AC': b.bind('<Button-1>',self.clean)
		self.i = 0

	def click(self,event):
		if(event.widget['text'] in self.attributes):
			if self.i == 0:
				self.show['text'] = ''
			self.show['text'] += event.widget['text']
			self.i += 1
			print(self.i)
		elif(event.widget['text'] in ('+', '-', '*', '/', '%', '**', '//',"±","÷")):
			self.show['text'] = self.show['text'] + event.widget['text']
		elif(event.widget['text'] == '=' and self.show['text'] is not None):
			self.hi = self.show['text']
			print(self.hi)
			self.show['text'] = str(eval(self.hi))
			self.hi = None
			self.i = 0

	def clean(self,event):
		self.hi = None
		self.show['text'] = ''

root = Tk()
root.title("科学计算器")
root.resizable(False,False)
calculate(root)
root.mainloop()