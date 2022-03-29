import tkinter as tk
from tkinter import *
from tkinter import messagebox

attrFile = open("attributes.txt", "w")
hardConstrFile = open("constraints.txt","w")

BA_Options = [] #binaryAttributes



root = tk.Tk()
root.title("CAP4630 Project 3")

"""TASK METHOD DEFINITIONS"""
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

"""END TASK METHOD DEFINITIONS"""

"""ADD BUTTON DEFINITIONS"""
#TODO: implement methods for add buttons
def binAtr_add():
    userAtr = binAtr_entr_attr.get()
    userAtr = userAtr.replace(" ","-")
    userOp1 = binAtr_entr_op1.get()
    userOp1 = userOp1.replace(" ","-")
    userOp2 = binAtr_entr_op2.get()
    userOp2 = userOp2.replace(" ","-")
    if userAtr != "" and userOp1 != "" and userOp2 != "":
        try:
            statement = userAtr + ": " + userOp1 + ", " + userOp2 + "\n"
            with open("attributes.txt", "a") as attrFile:
                attrFile.write(statement)
                binAtr_lbox.insert(END, statement)
                BA_Options.append(userOp1)
                BA_Options.append(userOp2)
        except FileNotFoundError:
            print("The attributes.txt does not exist")
    else:
        messagebox.showinfo("ERROR: Binary Attributes","Please fill in all entries before entering a binary attribute.")
    
def hardConstr_add():
    userHardConstr = hardConstr_entr_constr.get()
    if userHardConstr != "":
        userHC_list = userHardConstr.split(" ")
        for curr in userHC_list:
            if curr == "NOT" or curr == "AND" or curr == "OR":
                continue
            elif curr in BA_Options:
                continue
            else:
                 messagebox.showinfo("ERROR: Hard Constraints","Constraint contains options that don't exist in the current attributes.")
    else:
        messagebox.showinfo("ERROR: Hard Constraints","Please enter in a constraint.")

"""END ADD BUTTON DEFINITIONS"""

"""RESET METHOD"""
def reset():
    #preference file would go on this line
    attrFile = open("attributes.txt", "w")
    hardConstrFile = open("constraints.txt","w")
    #preference file would go on this line
    binAtr_lbox.delete(0,END)
    hardConstr_lbox.delete(0,END)
    pen_lbox.delete(0,END)
    poss_lbox.delete(0,END)
    qual_lbox.delete(0,END)

"""END RESET METHOD"""

    

#TODO: implement commands for open file buttons
#TODO: implement method for Reset button


"""END METHOD DEFINITIONS"""

top = Frame(root)
top.grid(row=0, column=0) #top frame to help align with preferences row

"""START BINARY CONSTRAITS"""
#binary attribute frames
binAtr_frame = tk.LabelFrame(top, text="Binary Attributes", padx=10, pady=10)
binAtr_frame2 = tk.Frame(binAtr_frame)
binAtr_frame.grid(row=0, column=0, padx=10)
binAtr_frame2.grid(row=0, column=2, sticky='ns')

#binary attribute frame 1
binAtr_lbox = tk.Listbox(binAtr_frame, width=50)
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

binAtr_addButton = tk.Button(binAtr_frame2, text="Add Attribute", command=binAtr_add)
binAtr_openFileButton = tk.Button(binAtr_frame2, text="Open File")

#binary attribute frame 2 (placements)
binAtr_lb_attr.grid(row=0,column=0)
binAtr_entr_attr.grid(row=1, column=0)
binAtr_lb_op1.grid(row=2, column=0)
binAtr_entr_op1.grid(row=3,column=0)
binAtr_lb_op2.grid(row=2, column=2)
binAtr_entr_op2.grid(row=3,column=2)
binAtr_addButton.grid(row=4, column=0)
binAtr_openFileButton.grid(row=5, column=0)
"""END binary Attributes"""

"""HARD CONSTRAITS"""
#hard constraints frames
hardConstr_frame = tk.LabelFrame(top, text="Hard Constraints", padx=10, pady=10)
hardConstr_frame2 = tk.Frame(hardConstr_frame)
hardConstr_frame.grid(row=0, column=1, padx=10)
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

#buttons
hardConstr_addButton = tk.Button(hardConstr_frame2, text="Add Constraint", command=hardConstr_add)
hardConstr_fileButton = tk.Button(hardConstr_frame2, text="Open File")

#frame2 fill
hardConstr_lb_constr.grid(row=0, column=0)
hardConstr_entr_constr.grid(row=1, column=0)
hardConstr_addButton.grid(row=2, column=0)
hardConstr_fileButton.grid(row=3, column=0)
"""END HARD CONSTRAINTS"""

"""FEASIBLE OBJECTS"""
feasObj_frame = LabelFrame(top, text="Feasible Objects", padx=10, pady=10)
feasObj_frame.grid(row=0, column=3)

feasObj_lbox = Listbox(feasObj_frame)
feasObj_lbox.grid(row=0, column=0)
feasObj_scroll = Scrollbar(feasObj_frame, orient='vertical', command=feasObj_lbox.yview)
feasObj_scroll.grid(row=0, column=1, sticky='ns')
feasObj_lbox['yscrollcommand'] = feasObj_scroll.set
"""END FEASIBLE OBJECTS"""

"""PREFERENCES"""
pref_frame = LabelFrame(root, text="Preferences", bd='5', pady=5)
pref_frame.grid(row=1, column=0)

"""PENALTY (PREFERENCE 1)"""
#penalty frames
pen_frame = LabelFrame(pref_frame, text="Penalty Logic", padx=10, pady=10)
pen_frame2 = Frame(pen_frame)
pen_frame.grid(row=0, column=0, padx=10)
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
poss_frame = LabelFrame(pref_frame, text="Possibilistic Logic", padx=10, pady=10)
poss_frame2 = Frame(poss_frame)
poss_frame.grid(row=0, column=1, padx=10)
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
qual_frame = LabelFrame(pref_frame, text="Possibilistic Logic", padx=10, pady=10)
qual_frame2 = Frame(qual_frame)
qual_frame.grid(row=0, column=2, padx=10)
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
b_reset = Button(exitFrame, text="Reset", command=reset)
b_reset.grid(row=0,column=0)
b_quit.grid(row=0,column=1)


root.mainloop()