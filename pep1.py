from tkinter import*
root = Tk()

lab_1=Label(root,text="Enter name")
ent_1=Entry(root)

lab_2=Label(root,text="Enter email")
ent_2=Entry(root)

lab_3=Label(root,text="Enter contact")
ent_3=Entry(root)
lab_4=Label(root,text="Hobbies")

f1=Frame(root)
c1=Checkbutton(f1,text="H1")
c2=Checkbutton(f1,text="H2")
c3=Checkbutton(f1,text="H3")
c1.pack(side=LEFT)
c2.pack(side=LEFT)
c3.pack(side=LEFT)

btn=Button(root,text="submit")
lab_1.grid(row=0,column=0)
ent_1.grid(row=0,column=1)

lab_2.grid(row=1,column=0)
ent_2.grid(row=1,column=1)

lab_3.grid(row=2,column=0)
ent_3.grid(row=2,column=1)

lab_4.grid(row=3,column=0)
f1.grid(row=3,column=1)
btn.grid(row=4,column=0)

root.mainloop()
