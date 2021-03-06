
from tkinter import *
from PIL import Image,ImageTk
from tkinter.filedialog import askopenfilename,asksaveasfilename
from tkinter.messagebox import askquestion,showinfo
from tkinter.colorchooser import*
import time; #we just use this to test for remote collaboration.
#----------------------------------------------------------------------------------------------------------------
root = Tk()
root.title(' Shugar-eSim')
root.wm_iconbitmap('globe.ico')
#----------------------------------------------------------------------------------------------------------------
w = Label(root,bg = 'orange')
w.pack(fill = X)
mcontent = Text(w, bg='white',width=40,relief= 'flat',height=1)
mcontent.pack(side = 'right')
#================================================================================================================
localtime = time.asctime(time.localtime(time.time()))
x = Label(root, text = localtime)
x.pack(fill = X)
y = Label(root,bg =  'orange')
y.pack(side = 'bottom',fill = X)
#----------------------------------------------------------------------------------------------------------------
loadn = Image.open('newfile.png')
rendern = ImageTk.PhotoImage(loadn, master = root)
frmL = Frame(root, bg = 'orange',width = 70)
frmL.pack(side = 'left', fill = BOTH)
lb1 = Listbox(frmL,width=24,height=20)
lb1.insert(1,'py')
lb1.insert(2,'js')
lb1.grid(row = 6,column = 0)
#mcontent = Text(frmL, bg='white',width=18,height=20)
#mcontent.grid(row = 6,column = 0)
scrolly = Scrollbar (frmL, orient = 'vertical', command = mcontent.yview)
scrolly.grid(row =6, column = 1, sticky = 'ns')
mcontent.configure(yscrollcommand = scrolly.set)
btnj = Button(frmL,image= rendern,command = lambda:newpage,padx=0, width = 140,bg = '#FFFACD')
btnj.grid(row = 0, column = 0)
btnk = Button(frmL,image= rendern,command = lambda:newpage,padx=0, width = 140,bg = '#FFFACD')
btnk.grid(row = 1, column = 0)
btnl = Button(frmL,image= rendern,command = lambda:newpage,padx=0, width = 140,bg = '#FFFACD')
btnl.grid(row = 2, column = 0)
btnm = Button(frmL,image= rendern,command = lambda:newpage,padx=0,relief= 'flat', width = 140,bg = '#FFFACD')
btnm.grid(row = 3, column = 0)
btnn= Button(frmL,image= rendern,relief= 'flat',command = lambda:newpage,padx=0, width = 140,bg = 'orange')
btnn.grid(row = 4, column = 0)
#----------------------------------------------------------------------------------------------------------------
frmR = Frame(root, bg = 'orange',width = 70)
frmR.pack(side = 'right', fill = BOTH)
btni = Button(frmR,height = 60,image= rendern,command = lambda:newpage,padx=0, width = 140,bg = '#FFFACD')
btni.grid(row = 0, column = 0)
btnii = Button(frmR,height = 60,image= rendern,command = lambda:newpage,padx=0, width = 140,bg = '#FFFACD')
btnii.grid(row = 1, column = 0)
btnii = Button(frmR,height = 60,image= rendern,command = lambda:newpage,padx=0, width = 140,bg = '#FFFACD')
btnii.grid(row = 2, column = 0)
btnii = Button(frmR,height = 60,image= rendern,command = lambda:newpage,padx=2, width = 140,bg = '#FFFACD')
btnii.grid(row = 3, column = 0)
btnii = Button(frmR,height = 60,image= rendern,relief= 'flat',command = lambda:newpage,padx=2, width = 140,bg = '#FFFACD')
btnii.grid(row = 4, column = 0)
#----------------------------------------------------------------------------------------------------------------
frmCan = Frame(root)
frmCan.pack(side = 'left')
canvas = Canvas(frmCan, bg='#FFFACD', height = 530,width =1030)
canvas.grid(row = 0, column  =0)
scrolly = Scrollbar (frmCan, orient = 'vertical', command = canvas.yview)
scrollx = Scrollbar (frmCan, orient = 'horizontal', command = canvas.xview)
scrolly.grid(row =0, column = 1,sticky = 'ns' )
scrollx.grid(row = 1, column = 0, sticky = 'ew')
canvas.configure(yscrollcommand = scrolly.set)
canvas.configure(xscrollcommand = scrollx.set)
#----------------------------------------------------------------------------------------------------------------
def getColor():
    color = askcolor()

def newpage():
    global filename
    root.title('Untitled Shugar-eSim')
    filename = None
    canvas.delete(1.0,'end')
def openf():
    filename = askopenfilename(defaultextension = '.png',filetypes = [('All Files','*.*'),('Text files','.')])
    if filename == '':
        filename = None
    else:
        load = Image.open(filename)
        render = ImageTk.PhotoImage(load, master = root)
        canvas.create_image(50,50, image=render, anchor = 'nw')
        filename.close()
def save():
    global filename
    if filename=='':
             filename= asksaveasfilename(filetypes = [('All Files',('.png'))])
             if filename=='':
                filename= None
             else:
                s = open(filename,'w')
                s.write(canvas.get(1.0,'end'))
                filename.close()
    else:
            s = open(filename,'w')
            s.write(canvas.get(1.0,'end'))
            filename.close()
def saveas():
    global filename
    filename= asksaveasfilename(filetypes = [('All Files',('.png'))])
    if filename == '':
        filename = None
    else:
        s = open(filename,'w')
        s.write(canvas.get(1.0,'end'))
        filename.close()
def pgst():
    pass
def delete():
    canvas.delete('all')
def prnt():
    pass
def Quit():
    answer = askquestion(title='Quit?', message='Are you sure?')
    if answer=='yes':
        root.destroy()
def abt():
    inf = showinfo(title=' About Shugar-Sim', message='This Product is Liscensed to Ajayi R.O')
    if inf=='yes':
        root.update()
load = Image.open('file.png')
render = ImageTk.PhotoImage(load, master = root)
load1 = Image.open('cancel.png')
render1 = ImageTk.PhotoImage(load1, master = root)
load3 = Image.open('redo.png')
render3 = ImageTk.PhotoImage(load3, master = root)
load12 = Image.open('new.png')
render12 = ImageTk.PhotoImage(load12, master = root)
load13 = Image.open('save.png')
render13 = ImageTk.PhotoImage(load13, master = root)
load14 = Image.open('saveas.png')
render14 = ImageTk.PhotoImage(load14, master = root)
loads = Image.open('bexit.png')
renders = ImageTk.PhotoImage(loads, master = root)
loadp = Image.open('cprint.png')
renderp = ImageTk.PhotoImage(loadp, master = root)
loadcp = Image.open('bcopy.png')
rendercp = ImageTk.PhotoImage(loadcp, master = root)
loadps = Image.open('bpaste.png')
renderps = ImageTk.PhotoImage(loadps, master = root)
loadu = Image.open('undo.png')
renderu = ImageTk.PhotoImage(loadu, master = root)
menubar = Menu(root)
fileMenu = Menu(menubar, tearoff=0,bg='white')
fileMenu.add_command(label = 'New',command=newpage, accelerator = 'Ctrl+N',image=render12, compound='left')
fileMenu.add_command(label = 'Open...',command=openf , accelerator = 'Ctrl+O',image=render, compound='left')
fileMenu.add_command(label = 'Save',command=save , accelerator = 'Ctrl+S',image=render13, compound='left')
fileMenu.add_command(label = 'Save As...',command=saveas,image=render14, compound='left')
fileMenu.add_separator()
fileMenu.add_command(label = 'Delete',command=delete , accelerator = '     Del', image= render1,compound= 'left')
fileMenu.add_command(label = 'Print',command=prnt,image= renderp,compound= 'left',  accelerator = 'Ctrl+P')
fileMenu.add_separator()
fileMenu.add_command(label = 'Exit',command=Quit,image= renders,compound= 'left')
menubar.add_cascade(label = 'File',menu = fileMenu,underline = 0)
root.config(menu = menubar)
fileMenu = Menu(menubar, tearoff=0,bg='white')
fileMenu.add_command(label = 'Copy',command=newpage, accelerator = 'Ctrl+C',image= rendercp,compound= 'left')
fileMenu.add_command(label = 'Paste',command=openf , accelerator = 'Ctrl+V',image= renderps,compound= 'left')
fileMenu.add_separator()
fileMenu.add_command(label = 'Undo',command=save , accelerator = 'Ctrl+Z',image= renderu,compound= 'left')
fileMenu.add_command(label = 'Redo',command=saveas, accelerator = 'Ctrl+Shift+Z',image=render3, compound='left')
menubar.add_cascade(label = 'Edit',menu = fileMenu,underline = 0)
root.config(menu = menubar)
fileMenu = Menu(menubar, tearoff=0,bg='white')
fileMenu.add_command(label = 'Copy',command=newpage, accelerator = 'Ctrl+C',image= rendercp,compound= 'left')
fileMenu.add_command(label = 'Paste',command=openf , accelerator = 'Ctrl+V',image= renderps,compound= 'left')
fileMenu.add_separator()
fileMenu.add_command(label = 'Undo',command=save , accelerator = 'Ctrl+Z',image= renderu,compound= 'left')
fileMenu.add_command(label = 'Redo',command=saveas, accelerator = 'Ctrl+Shift+Z',image=render3, compound='left')
menubar.add_cascade(label = 'View',menu = fileMenu,underline = 0)
root.config(menu = menubar)
fileMenu = Menu(menubar, tearoff=0,bg='white')
fileMenu.add_command(label = 'Copy',command=newpage, accelerator = 'Ctrl+C',image= rendercp,compound= 'left')
fileMenu.add_command(label = 'Paste',command=openf , accelerator = 'Ctrl+V',image= renderps,compound= 'left')
fileMenu.add_separator()
fileMenu.add_command(label = 'Undo',command=save , accelerator = 'Ctrl+Z',image= renderu,compound= 'left')
fileMenu.add_command(label = 'Redo',command=saveas, accelerator = 'Ctrl+Shift+Z',image=render3, compound='left')
menubar.add_cascade(label = 'Tools',menu = fileMenu,underline = 0)
root.config(menu = menubar)
fileMenu = Menu(menubar, tearoff=0,bg='white')
fileMenu.add_command(label = 'Copy',command=newpage, accelerator = 'Ctrl+C',image= rendercp,compound= 'left')
fileMenu.add_command(label = 'Paste',command=openf , accelerator = 'Ctrl+V',image= renderps,compound= 'left')
fileMenu.add_separator()
fileMenu.add_command(label = 'Undo',command=save , accelerator = 'Ctrl+Z',image= renderu,compound= 'left')
fileMenu.add_command(label = 'Redo',command=saveas, accelerator = 'Ctrl+Shift+Z',image=render3, compound='left')
menubar.add_cascade(label = 'Help',menu = fileMenu,underline = 0)
root.config(menu = menubar)
#----------------------------------------------------------------------------------------------------------------
loadn = Image.open('newfile.png')
rendern = ImageTk.PhotoImage(loadn, master = root)
loadf = Image.open('openw.png')
renderf = ImageTk.PhotoImage(loadf, master = root)
loadws = Image.open('wsave.png')
renderws = ImageTk.PhotoImage(loadws, master = root)
loadpr = Image.open('print.png')
renderpr = ImageTk.PhotoImage(loadpr, master = root)
load6 = Image.open('bplay.png')
render6 = ImageTk.PhotoImage(load6, master = root)
load7 = Image.open('bpause.png')
render7 = ImageTk.PhotoImage(load7, master = root)
loadst = Image.open('stop.png')
renderst = ImageTk.PhotoImage(loadst, master = root)
loadzi = Image.open('bzi.png')
renderzi= ImageTk.PhotoImage(loadzi, master = root)
loadzo = Image.open('bzo.png')
renderzo = ImageTk.PhotoImage(loadzo, master = root)
loadza = Image.open('za.png')
renderza = ImageTk.PhotoImage(loadza, master = root)
loadze = Image.open('ze.png')
renderze = ImageTk.PhotoImage(loadze, master = root)
loadm = Image.open('bmove.png')
renderm = ImageTk.PhotoImage(loadm, master = root)
loadrep = Image.open('breplace.png')
renderrep = ImageTk.PhotoImage(loadrep, master = root)
loaddel = Image.open('del.png')
renderdel = ImageTk.PhotoImage(loaddel, master = root)
loadcut = Image.open('bcut.png')
rendercut = ImageTk.PhotoImage(loadcut, master = root)
loadcopy = Image.open('bcopy.png')
rendercopy = ImageTk.PhotoImage(loadcopy, master = root)
loadpaste = Image.open('bpaste.png')
renderpaste = ImageTk.PhotoImage(loadpaste, master = root)
loadset = Image.open('settings.png')
renderset = ImageTk.PhotoImage(loadset, master = root)
loadhlp = Image.open('help.png')
renderhlp = ImageTk.PhotoImage(loadhlp, master = root)
loadabt = Image.open('about.png')
renderabt = ImageTk.PhotoImage(loadabt, master = root)
btnn = Button(w,image= rendern,command = newpage,padx=2)
btnn.pack(side= 'left',anchor= 'w')
btnf = Button(w,image= renderf,command = openf,padx=2)
btnf.pack(side= 'left',anchor= 'w')
btns = Button(w,image= renderws,command =save,padx=2)
btns.pack(side= 'left',anchor= 'w')
btnp = Button(w,image= renderpr,padx=2)
btnp.pack(side= 'left',anchor= 'w')
btn2 = Button(w,image= render6,padx=2)
btn2.pack(side= 'left',anchor= 'w')
btn3 = Button(w,image= render7,padx=2)
btn3.pack(side= 'left',anchor= 'w')
btn8 = Button(w,image= renderst,padx=2)
btn8.pack(side= 'left',anchor= 'w')
btn9 = Button(w,image= renderzi,padx=2)
btn9.pack(side= 'left',anchor= 'w')
btn10 = Button(w,image= renderzo,padx=2)
btn10.pack(side= 'left',anchor= 'w')
btn11 = Button(w,image= renderza,padx=2)
btn11.pack(side= 'left',anchor= 'w')
btn12 = Button(w,image= renderze,padx=2)
btn12.pack(side= 'left',anchor= 'w')
btnm = Button(w,image= renderm,padx=2)
btnm.pack(side= 'left',anchor= 'w')
btnrep = Button(w,image= renderrep,padx=2)
btnrep.pack(side= 'left',anchor= 'w')
btndel = Button(w,image= renderdel,padx=2)
btndel.pack(side= 'left',anchor= 'w')
btncut = Button(w,image= rendercut,padx=2)
btncut.pack(side= 'left',anchor= 'w')
btncopy = Button(w,image= rendercopy,padx=2)
btncopy.pack(side= 'left',anchor= 'w')
btnpaste = Button(w,image= renderpaste,padx=2)
btnpaste.pack(side= 'left',anchor= 'w')
btnem = Button(w,relief = 'flat',bg = 'orange',padx=0)
btnem.pack(side= 'right',anchor= 'w')
btnhlp = Button(w,image= renderhlp,padx=2)
btnhlp.pack(side= 'right',anchor= 'w')
btnabt = Button(w,image= renderabt,padx=2, command = abt)
btnabt.pack(side= 'right',anchor= 'w')
btnset = Button(w,image= renderset,padx=2, command = getColor)
btnset.pack(side= 'right',anchor= 'w')

#----------------------------------------------------------------------------------------------------------------
loadelec = Image.open('elec.png')
renderelec = ImageTk.PhotoImage(loadelec, master = root)
loadbat = Image.open('battery.png')
renderbat = ImageTk.PhotoImage(loadbat, master = root)
loadres = Image.open('resistor.png')
renderres = ImageTk.PhotoImage(loadres, master = root)
loadled = Image.open('led.png')
renderled = ImageTk.PhotoImage(loadled, master = root)
loadtrans = Image.open('transistor.png')
rendertrans = ImageTk.PhotoImage(loadtrans, master = root)
loadcap = Image.open('capacitor.png')
rendercap = ImageTk.PhotoImage(loadcap, master = root)
loadosc = Image.open('osci.png')
renderosc = ImageTk.PhotoImage(loadosc, master = root)
loadrel = Image.open('relay.png')
renderrel = ImageTk.PhotoImage(loadrel, master = root)
loadsen = Image.open('sensor.png')
rendersen = ImageTk.PhotoImage(loadsen, master = root)
loadpro = Image.open('processor.png')
renderpro = ImageTk.PhotoImage(loadpro, master = root)
btnelec = Button(x,image= renderelec,relief= 'flat',padx=2)
btnelec.pack(side= 'left',anchor= 'w')
btnbat = Button(x,image= renderbat,relief= 'flat',padx=2)
btnbat.pack(side= 'left',anchor= 'w')
btnres = Button(x,image= renderres,relief= 'flat',padx=2)
btnres.pack(side= 'left',anchor= 'w')
btnled = Button(x,image= renderled,relief= 'flat',padx=2)
btnled.pack(side= 'left',anchor= 'w')
btntrans = Button(x,image= rendertrans,relief= 'flat',padx=2)
btntrans.pack(side= 'left',anchor= 'w')
btncap = Button(x,image= rendercap,relief= 'flat',padx=2)
btncap.pack(side= 'left',anchor= 'w')
btnosc = Button(x,image= renderosc,relief= 'flat',padx=2)
btnosc.pack(side= 'left',anchor= 'w')
btnrel = Button(x,image= renderrel,relief= 'flat',padx=2)
btnrel.pack(side= 'left',anchor= 'w')
btnsen = Button(x,image= rendersen,relief= 'flat',padx=2)
btnsen.pack(side= 'left',anchor= 'w')
btnpro = Button(x,image= renderpro,relief= 'flat',padx=2)
btnpro.pack(side= 'left',anchor= 'w')
sb = Spinbox(x,from_ =0, to = 10)
sb.pack(side= 'left',anchor= 'w')
#-----------------------------------------------------------------------------------------------------------------
btnf = Button(y,height = 2,text="Simulation",padx= 16, bd = 2, fg='orange', font =('courier',10, 'bold'),bg = '#FFFACD')
btnf.pack(side= 'left',anchor= 'w')
btng = Button(y,height = 2,text="Real Time",padx= 16, bd = 2, fg='orange', font =('courier',10, 'bold'),bg = '#FFFACD')
btng.pack(side= 'left',anchor= 'w')
#----------------------------------------------------------------------------------------------------------------
'''
def newpage():
    global filename
    root.title('Untitled Shugar-eSim')
    filename = None
    canvas.delete(1.0,'end')
def openf():
    filename = askopenfilename(defaultextension = '.png',filetypes = [('All Files','*.*'),('Text files','.')])
    if filename == '':
        filename = None
    else:
        load = Image.open(filename)
        render = ImageTk.PhotoImage(load, master = root)
        canvas.create_image(50,50, image=render)
        filename.close()
def save():
    global filename
    if filename=='':
             filename= asksaveasfilename(filetypes = [('All Files',('.png'))])
             if filename=='':
                filename= None
             else:
                s = open(filename,'w')
                s.write(canvas.get(1.0,'end'))
                filename.close()
    else:
            s = open(filename,'w')
            s.write(canvas.get(1.0,'end'))
            filename.close()
def saveas():
    global filename
    filename= asksaveasfilename(filetypes = [('All Files',('.png'))])
    if filename == '':
        filename = None
    else:
        s = open(filename,'w')
        s.write(canvas.get(1.0,'end'))
        filename.close()
loadn = Image.open('newfile.png')
rendern = ImageTk.PhotoImage(loadn, master = root)
menubar = Menu(frm1)
fileMenu = Menu(menubar, tearoff=0,bg='white')
fileMenu.add_command(label = 'Copy',command=newpage, accelerator = 'Ctrl+C',image= rendern,compound= 'left')
fileMenu.add_command(label = 'Paste',command=openf , accelerator = 'Ctrl+V',image= rendern,compound= 'left')
fileMenu.add_separator()
fileMenu.add_command(label = 'Undo',command=save , accelerator = 'Ctrl+Z',image= rendern,compound= 'left')
fileMenu.add_command(label = 'Redo',command=saveas, accelerator = 'Ctrl+Shift+Z',image=rendern, compound='left')
menubar.add_cascade(label = 'View',menu = fileMenu,underline = 0)
frm1.config()
'''
#----------------------------------------------------------------------------------------------------------------
root.mainloop()