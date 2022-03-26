# tkinter is already installed to pycharm. idk if pyclasp is too, but if it's not you can install it fairly easily
# just hover over the red squiggly line and ask pycharm to install it, if you need to
import tkinter as tk
from tkinter import *
import pyclasp as clasp

root = tk.Tk()

top = Frame(root)
top.grid(row=0, column=0)

#binary attributes
binAtr_frame = tk.LabelFrame(top, text="Binary Attributes")
binAtr_frame2 = tk.LabelFrame(binAtr_frame)
binAtr_frame.grid(row=0, column=0)
binAtr_frame2.grid(row=0, column=1)

binAtr_lbox = tk.Listbox(binAtr_frame) #listbox

binAtr_lb_attr = tk.Label(binAtr_frame2, text = "Attribute")
binAtr_lb_op1 = tk.Label(binAtr_frame2, text = "Option 1")
binAtr_lb_op2 = tk.Label(binAtr_frame2, text = "Option 2")
binAtr_entr_attr = tk.Entry(binAtr_frame2) #attribute entry
binAtr_entr_op1 = tk.Entry(binAtr_frame2) #option 1 entry
binAtr_entr_op2 = tk.Entry(binAtr_frame2) #option 2 entry
binAtr_add = tk.Button(binAtr_frame2, text="Add Attribute") #add button
binAtr_openFile = tk.Button(binAtr_frame2, text="Open File") #open file button

binAtr_lbox.grid(row=0,column=0) #listbox

binAtr_lb_attr.grid(row=0,column=0)
binAtr_entr_attr.grid(row=1, column=0) #attribute entry

binAtr_lb_op1.grid(row=2, column=0)
binAtr_entr_op1.grid(row=3,column=0) #option1 entry

binAtr_lb_op2.grid(row=2, column=2)
binAtr_entr_op2.grid(row=3,column=2) #option2 entry
binAtr_add.grid(row=4, column=0) #add button
binAtr_openFile.grid(row=5, column=0) #open file button
#end binary Attributes

#hard constraints
hardConstr_frame = tk.LabelFrame(top, text="Hard Constraints")
hardConstr_frame2 = tk.LabelFrame(hardConstr_frame)
hardConstr_frame.grid(row=0, column=1)
hardConstr_frame2.grid(row=0, column=1)

hardConstr_lbox = tk.Listbox(hardConstr_frame)

hardConstr_lb_constr = tk.Label(hardConstr_frame2, text="Constraint")
hardConstr_entr_constr = tk.Entry(hardConstr_frame2)
hardConstr_add = tk.Button(hardConstr_frame2, text="Add Constraint")
hardConstr_file = tk.Button(hardConstr_frame2, text="Open File")

hardConstr_lbox.grid(row=0, column=0)

hardConstr_lb_constr.grid(row=0, column=0)
hardConstr_entr_constr.grid(row=1, column=0)
hardConstr_add.grid(row=2, column=0)
hardConstr_file.grid(row=3, column=0)
#end hardConstr

#Feasible Objects
feasObj_frame = LabelFrame(top, text="Feasible Objects")
feasObj_frame2 = LabelFrame(feasObj_frame)
feasObj_frame.grid(row=0, column=3)
feasObj_frame2.grid(row=0, column=1)

feasObj_lbox = Listbox(feasObj_frame)
feasObj_lbox.grid(row=0, column=0)

#preferences
pref_frame = LabelFrame(root, text="Preferences")
pref_frame.grid(row=1, column=0)

#penalty
pen_frame = LabelFrame(pref_frame, text="Penalty Logic")
pen_frame2 = LabelFrame(pen_frame)
pen_frame.grid(row=0, column=0)
pen_frame2.grid(row=0, column=1)

pen_lbox = Listbox(pen_frame)
pen_lbox.grid(row=0, column=0)

pen_lb_pref = Label(pen_frame2, text="Preference")
pen_lb_val = Label(pen_frame2, text="Value")
pen_entr_pref = Entry(pen_frame2)
pen_entr_val = Entry(pen_frame2)
pen_add = Button(pen_frame2, text="Add Preference")
pen_file = Button(pen_frame2, text="Open File")

pen_lb_pref.grid(row=0, column=0)
pen_entr_pref.grid(row=1, column=0)
pen_lb_val.grid(row=0, column=1)
pen_entr_val.grid(row=1, column=1)
pen_add.grid(row=2, column=0)
pen_file.grid(row=3, column=0)

#possibilistic
poss_frame = LabelFrame(pref_frame, text="Possibilistic Logic")
poss_frame2 = LabelFrame(poss_frame)
poss_frame.grid(row=0, column=1)
poss_frame2.grid(row=0, column=1)

poss_lbox = Listbox(poss_frame)
poss_lbox.grid(row=0, column=0)

poss_lb_pref = Label(poss_frame2, text="Preference")
poss_lb_val = Label(poss_frame2, text="Value")
poss_entr_pref = Entry(poss_frame2)
poss_entr_val = Entry(poss_frame2)
poss_add = Button(poss_frame2, text="Add Preference")
poss_file = Button(poss_frame2, text="Open File")

poss_lb_pref.grid(row=0, column=0)
poss_entr_pref.grid(row=1, column=0)
poss_lb_val.grid(row=0, column=1)
poss_entr_val.grid(row=1, column=1)
poss_add.grid(row=2, column=0)
poss_file.grid(row=3, column=0)

#qualitiative
qual_frame = LabelFrame(pref_frame, text="Possibilistic Logic")
qual_frame2 = LabelFrame(qual_frame)
qual_frame.grid(row=0, column=2)
qual_frame2.grid(row=0, column=1)

qual_lbox = Listbox(qual_frame)
qual_lbox.grid(row=0, column=0)

qual_lb_pref = Label(qual_frame2, text="Preference")
qual_entr_pref = Entry(qual_frame2)
qual_add = Button(qual_frame2, text="Add Preference")
qual_file = Button(qual_frame2, text="Open File")

qual_lb_pref.grid(row=0, column=0)
qual_entr_pref.grid(row=1, column=0)
qual_add.grid(row=2, column=0)
qual_file.grid(row=3, column=0)

#buttons for the other tasks
bottom = Frame(root)
bottom.grid(row=2, column=0)

b_exemplify = Button(bottom, text="Exemplify")
b_optimize = Button(bottom, text="Optimize")
b_omni = Button(bottom, text="Omni-Optimize")

b_exemplify.grid(row=0, column=0)
b_optimize.grid(row=0, column=1)
b_omni.grid(row=0, column=2)





root.mainloop()