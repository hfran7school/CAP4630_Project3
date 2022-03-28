# tkinter is already installed to pycharm. idk if pyclasp is too, but if it's not you can install it fairly easily
# just hover over the red squiggly line and ask pycharm to install it, if you need to
import tkinter as tk
from tkinter import *
import pyclasp as clasp

root = tk.Tk()
root.title("CAP4630 Project 3")

"""METHOD DEFINITIONS"""
#pop up window for exemplify
def exemplify():
    exemp_win = Toplevel(taskFrame)
    exemp_win.title("Exemplify")
    # TODO: create layout for exemplify

#pop up window for optimize
def optimize():
    op_win = Toplevel(taskFrame)
    op_win.title("Optimize")
    # TODO: create layout for optimize

#pop up window for omni-optimize
def omni():
    omni_win = Toplevel(taskFrame)
    omni_win.title("Omni-Optimize")
    # TODO: create layout for omni-optimize

#TODO: implement methods for add buttons
#TODO: implement commands for open file buttons
#TODO: implement method for Reset button


"""END METHOD DEFINITIONS"""

top = Frame(root)
top.grid(row=0, column=0) #top frame to help align with preferences row

"""START BINARY CONSTRAITS"""
#binary attribute frames
binAtr_frame = tk.LabelFrame(top, text="Binary Attributes")
binAtr_frame2 = tk.LabelFrame(binAtr_frame)
binAtr_frame.grid(row=0, column=0)
binAtr_frame2.grid(row=0, column=2, sticky='ns')

#binary attribute frame 1
binAtr_lbox = tk.Listbox(binAtr_frame)
binAtr_lbox.grid(row=0,column=0)
binAtr_scroll = Scrollbar(binAtr_frame, orient='vertical', command=binAtr_lbox.yview)
binAtr_scroll.grid(row=0, column=1, sticky='ns')
binAtr_lbox['yscrollcommand'] = binAtr_scroll.set

#binary attribute frame 2
binAtr_lb_attr = tk.Label(binAtr_frame2, text = "Attribute")
binAtr_lb_op1 = tk.Label(binAtr_frame2, text = "Option 1")
binAtr_lb_op2 = tk.Label(binAtr_frame2, text = "Option 2")
binAtr_entr_attr = tk.Entry(binAtr_frame2)
binAtr_entr_op1 = tk.Entry(binAtr_frame2)
binAtr_entr_op2 = tk.Entry(binAtr_frame2)
binAtr_add = tk.Button(binAtr_frame2, text="Add Attribute")
binAtr_openFile = tk.Button(binAtr_frame2, text="Open File")

#binary attribute frame 2 (placements)
binAtr_lb_attr.grid(row=0,column=0)
binAtr_entr_attr.grid(row=1, column=0)
binAtr_lb_op1.grid(row=2, column=0)
binAtr_entr_op1.grid(row=3,column=0)
binAtr_lb_op2.grid(row=2, column=2)
binAtr_entr_op2.grid(row=3,column=2)
binAtr_add.grid(row=4, column=0)
binAtr_openFile.grid(row=5, column=0)
"""END binary Attributes"""

"""HARD CONSTRAITS"""
#hard constraints frames
hardConstr_frame = tk.LabelFrame(top, text="Hard Constraints")
hardConstr_frame2 = tk.LabelFrame(hardConstr_frame)
hardConstr_frame.grid(row=0, column=1)
hardConstr_frame2.grid(row=0, column=2, sticky='ns')

#frame1
hardConstr_lbox = tk.Listbox(hardConstr_frame)
hardConstr_lbox.grid(row=0, column=0)
hardConstr_scroll = Scrollbar(hardConstr_frame, orient='vertical', command=hardConstr_lbox.yview)
hardConstr_scroll.grid(row=0, column=1, sticky='ns')
hardConstr_lbox['yscrollcommand'] = hardConstr_scroll.set

#frame2
hardConstr_lb_constr = tk.Label(hardConstr_frame2, text="Constraint")
hardConstr_entr_constr = tk.Entry(hardConstr_frame2)
hardConstr_add = tk.Button(hardConstr_frame2, text="Add Constraint")
hardConstr_file = tk.Button(hardConstr_frame2, text="Open File")

#frame2 fill
hardConstr_lb_constr.grid(row=0, column=0)
hardConstr_entr_constr.grid(row=1, column=0)
hardConstr_add.grid(row=2, column=0)
hardConstr_file.grid(row=3, column=0)
"""END HARD CONSTRAINTS"""

"""FEASIBLE OBJECTS"""
feasObj_frame = LabelFrame(top, text="Feasible Objects")
feasObj_frame2 = LabelFrame(feasObj_frame)
feasObj_frame.grid(row=0, column=3)
feasObj_frame2.grid(row=0, column=1, sticky='ns')

feasObj_lbox = Listbox(feasObj_frame)
feasObj_lbox.grid(row=0, column=0)
feasObj_scroll = Scrollbar(feasObj_frame, orient='vertical', command=feasObj_lbox.yview)
feasObj_scroll.grid(row=0, column=1, sticky='ns')
feasObj_lbox['yscrollcommand'] = feasObj_scroll.set
"""END FEASIBLE OBJECTS"""

"""PREFERENCES"""
pref_frame = LabelFrame(root, text="Preferences")
pref_frame.grid(row=1, column=0)

"""PENALTY (PREFERENCE 1)"""
#penalty frames
pen_frame = LabelFrame(pref_frame, text="Penalty Logic")
pen_frame2 = LabelFrame(pen_frame)
pen_frame.grid(row=0, column=0)
pen_frame2.grid(row=0, column=2,sticky='ns')

#penalty frame1
pen_lbox = Listbox(pen_frame)
pen_lbox.grid(row=0, column=0)
pen_scroll = Scrollbar(pen_frame, orient='vertical', command=pen_lbox.yview)
pen_scroll.grid(row=0, column=1, sticky='ns')
pen_lbox['yscrollcommand'] = pen_scroll.set

#penalty frame2
pen_lb_pref = Label(pen_frame2, text="Preference")
pen_lb_val = Label(pen_frame2, text="Value")
pen_entr_pref = Entry(pen_frame2)
pen_entr_val = Entry(pen_frame2)
pen_add = Button(pen_frame2, text="Add Preference")
pen_file = Button(pen_frame2, text="Open File")

#penalty frame2 placements
pen_lb_pref.grid(row=0, column=0)
pen_entr_pref.grid(row=1, column=0)
pen_lb_val.grid(row=0, column=1)
pen_entr_val.grid(row=1, column=1)
pen_add.grid(row=2, column=0)
pen_file.grid(row=3, column=0)
"""END PENALTY (PREFERENCE 1)"""

"""POSSIBILISTIC (PREFERENCE 2)"""
#possibilistic frames
poss_frame = LabelFrame(pref_frame, text="Possibilistic Logic")
poss_frame2 = LabelFrame(poss_frame)
poss_frame.grid(row=0, column=1)
poss_frame2.grid(row=0, column=2,sticky='ns')

#possibilistic frame1
poss_lbox = Listbox(poss_frame)
poss_lbox.grid(row=0, column=0)
poss_scroll = Scrollbar(poss_frame, orient='vertical', command=poss_lbox.yview)
poss_scroll.grid(row=0, column=1, sticky='ns')
poss_lbox['yscrollcommand'] = poss_scroll.set

#possibilistic frame2
poss_lb_pref = Label(poss_frame2, text="Preference")
poss_lb_val = Label(poss_frame2, text="Value")
poss_entr_pref = Entry(poss_frame2)
poss_entr_val = Entry(poss_frame2)
poss_add = Button(poss_frame2, text="Add Preference")
poss_file = Button(poss_frame2, text="Open File")

#possibilistic placements
poss_lb_pref.grid(row=0, column=0)
poss_entr_pref.grid(row=1, column=0)
poss_lb_val.grid(row=0, column=1)
poss_entr_val.grid(row=1, column=1)
poss_add.grid(row=2, column=0)
poss_file.grid(row=3, column=0)
"""END POSSIBILISTIC (PREFERENCE 2)"""

"""QUALITATIVE (PREFERENCE 3)"""
#qualitative frames
qual_frame = LabelFrame(pref_frame, text="Possibilistic Logic")
qual_frame2 = LabelFrame(qual_frame)
qual_frame.grid(row=0, column=2)
qual_frame2.grid(row=0, column=2,sticky='ns')

#qualitiative frame1
qual_lbox = Listbox(qual_frame)
qual_lbox.grid(row=0, column=0)
qual_scroll = Scrollbar(qual_frame, orient='vertical', command=qual_lbox.yview)
qual_scroll.grid(row=0, column=1, sticky='ns')
qual_lbox['yscrollcommand'] = qual_scroll.set

#qualitiative frame2
qual_lb_pref = Label(qual_frame2, text="Preference")
qual_entr_pref = Entry(qual_frame2)
qual_add = Button(qual_frame2, text="Add Preference")
qual_file = Button(qual_frame2, text="Open File")

#qualitative frame2 placements
qual_lb_pref.grid(row=0, column=0)
qual_entr_pref.grid(row=1, column=0)
qual_add.grid(row=2, column=0)
qual_file.grid(row=3, column=0)
"""END QUALITATIVE (PREFERENCE 3)"""

"""END PREFERENCE"""

#buttons for the other tasks
taskFrame = Frame(root)
taskFrame.grid(row=2, column=0)

b_exemplify = Button(taskFrame, text="Exemplify",command=exemplify)
b_optimize = Button(taskFrame, text="Optimize", command=optimize)
b_omni = Button(taskFrame, text="Omni-Optimize", command=omni)

b_exemplify.grid(row=0, column=0)
b_optimize.grid(row=0, column=1)
b_omni.grid(row=0, column=2)

#exit and reset
exitFrame = Frame(root)
exitFrame.grid(row=3, column=0)

b_quit = Button(exitFrame, text="Quit", command=root.destroy)
b_reset = Button(exitFrame, text="Reset")
b_reset.grid(row=0,column=0)
b_quit.grid(row=0,column=1)


root.mainloop()