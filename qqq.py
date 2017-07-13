import tkinter
import os
def AA():
   #if  text=='欧拉欧拉欧拉':
        text='木大木大木大'
def processCancel():
    exit(0)
def ScanAndPrint(list):
    for i in os.walk(PATH):
        #index=0
        if str(i)[3] != '\'': break
        j=i[1]
        k=i[2]
        print(j)
        print(k)
        #i = str(i)
        for name in j:
            list.insert(0,name)
        for name in k:
            list.insert(0,name)
        #list.insert(5,k)
    #return 0
def DoubleClick(event):
    print('按下了按钮!')
i=0
PATH='/'#路径变量

#while(i<1):
root=tkinter.Tk()
f1=tkinter.Frame(root)
f2=tkinter.Frame(root)
i+=1

#window=tkinter.Tk()
   #menu=tkinter.Menu(root)
    #submenu=tkinter.Menu(menu,tearoff=0)
    #submenu.add_command(label='木大木大')
    #menu.add_cascade(label='dio',menu=submenu)
    #root.config(menu=menu)
#menu.pack()
Pathlabel=tkinter.Label(f1,text='目标位置:'+PATH)

Pathlabel.grid()
Pathlabel.grid_configure(column=0,row=0,columnspan=3,rowspan=1)


button=tkinter.Button(f2,text='什么都没有',command=processCancel)
button.pack()


FileBox = tkinter.Listbox(f1)
ScanAndPrint(FileBox)
FileBox.bind('<Button-1>',DoubleClick)
FileBox.grid()
FileBox.grid_configure(column=0,row=1,columnspan=6,rowspan=9)
#FileBox.place(width=800,height=500)
f1.pack()
f2.pack(side='bottom')
root.propagate(True)
root.mainloop()

