# tkinter is already installed to pycharm. idk if pyclasp is too, but if it's not you can install it fairly easily
# just hover over the red squiggly line and ask pycharm to install it, if you need to
import tkinter as tk
import pyclasp as clasp

root = tk.Tk()

"""Binary Attribute and Hard Constraint Row
TODO: 
   Make a space to display current binary attributes
   Make a space to display current hard restraints
   Make a place to enter a binary attribute to add
   Make a place to enter a hard constraints to add
"""
#labels
lb_binAtr = tk.Label(root, text="Binary Attributes").grid(row=0, column=0)
lb_hardConstr = tk.Label(root, text="Hard Constraints").grid(row=0, column=1)
#Listbox(placeholder)
lbox_binAtr = tk.Listbox(root).grid(row=1, column=0)
lbox_hardConstr = tk.Listbox(root).grid(row=1, column=1)


"""Preference Logic Rows
TODO:
    Make a space to place each of the current preferences
    Make a space to enter a preference to add for each preference
"""
#labels
lb_Pen = tk.Label(root, text="Penalty Logic").grid(row=2, column=0)
lb_Poss = tk.Label(root, text="Possibilistic Logic").grid(row=2,column=1)
lb_Qual = tk.Label(root, text="Qualitative Choice Logic").grid(row=2, column=2)
#listboxes(placeholder)
lbox_Pen = tk.Listbox(root).grid(row=3, column=0)
lbox_Poss = tk.Listbox(root).grid(row=3, column=1)
lbox_Qual = tk.Listbox(root).grid(row=3, column=2)

"""Feasable Objects Row
TODO:
    Make a space to place all of the feasable objects
"""
#labels
lb_obj = tk.Label(root, text="Feasible Objects").grid(row=4,column=0)
#listboxes(placeholder)
lbox_obj = tk.Listbox(root).grid(row=5, column=0)

root.mainloop()