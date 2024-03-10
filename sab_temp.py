# -*- coding: utf-8 -*-

from tkinter import *
from math import sqrt
import tkinter.font

class myApp:

    def prevod(self, event=None):
        v = float(self.ent_in.get())
        print(self.dir.get())
        self.ent_out.delete(0, END)
        
        if self.dir.get() == 1:
            self.degree_rec = ((50 - v) * 212 / 70)  + 80
            v = v * 9 / 5 + 32
        else:
            v = (v - 32) * 5 / 9
            self.degree_rec = ((50 - v) * 212 / 70)  + 80
            
        self.ent_out.insert(0, str(round(v, 2)))
        self.ca.coords(self.r, 146, 292, 152, self.degree_rec)

    def __init__(self, root):

        root.title('Převodník teplot')
        root.resizable(False, False)
        root.bind('<Return>', self.prevod)        

        def_font = tkinter.font.nametofont("TkDefaultFont")
        def_font.config(size=16)

        self.left_frame = Frame(root)
        self.right_frame = Frame(root)
        self.s_p_lable_frame = LabelFrame(self.left_frame, text="Směr převodu", padx=30)
        self.l_lable_frame = Label(self.left_frame, text="Vladislav Shumilin, SHU0020")
        self.entry_frame = LabelFrame(self.left_frame, pady=10, padx=30)
        
        self.dir = IntVar()
        self.dir.set(1)
        self.degree_rec = 292 
        
        self.rbu_c_to_f = Radiobutton(self.s_p_lable_frame, text="C -> F", value=1, variable = self.dir)
        self.rbu_f_to_c = Radiobutton(self.s_p_lable_frame, text="F -> C", value=0, variable = self.dir)
        
        self.lbl_in = Label(self.entry_frame, text="Vstup")
        self.ent_in = Entry(self.entry_frame, width=20, font = def_font)
        self.ent_in.insert(0, '')
        
        self.lbl_out = Label(self.entry_frame, text="Vystup")
        self.ent_out = Entry(self.entry_frame, width=20, font = def_font)
        self.ent_out.insert(0, '')
        
        self.bu_convert = Button(self.entry_frame, text="Convert", command=self.prevod)

        self.ca = Canvas(self.right_frame, width=300, height=400)
        self.photo = PhotoImage(file="th_emtpy.png")
        self.ca.create_image(150, 200, image=self.photo)
        self.r = self.ca.create_rectangle(146, 292, 152, 80, fill="blue")
        self.ca.coords(self.r, 146, 292, 152, self.degree_rec)

        self.left_frame.pack(side="left", fill=Y, padx=20)
        self.right_frame.pack(side="right")
        self.s_p_lable_frame.pack(fill=BOTH)
        self.entry_frame.pack(fill=BOTH, expand=True)
        
        self.lbl_in.pack()
        self.ent_in.pack()
        self.lbl_out.pack()
        self.ent_out.pack()   
        self.bu_convert.pack(side='bottom')
        
        self.l_lable_frame.pack()
        
        self.ca.pack()
        self.ent_in.focus_force()
        
        self.rbu_c_to_f.pack(side="left")
        self.rbu_f_to_c.pack(side="right")


root = Tk()
app = myApp(root)
root.mainloop()

