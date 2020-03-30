# VideoApplication Basic Module
import os
import tkinter
from tkinter.ttk import *
from tkinter import *
# Window Module
win=tkinter.Tk()
win.title("Movie Finder")
scrl=tkinter.Scrollbar(win)
scrl.grid(row=1,column=1)
mylist=Listbox(win,height=50,width=100,yscrollcommand=scrl.set)

# Location
global loc
loc='c:/'
loc1='d:/'
loc2='e:/'
loc3='f:/'
loc4='g:/'

# List containg result
global r_list
r_list=[]

# NotADirectoryError List
de_list=[]

# PermissionError List
pe_list=[]

# Main Function to check files
def check(loc='.'):
    global r_list
    
    try :
        lof=os.listdir(loc)#lods = List Of all files
        for i in lof :
            #print (i)
            file=os.path.splitext(i)[1]
            if file=='.mkv' or file=='.webm' or file=='.mpg' or file=='.mp2' or file=='.mpeg' or file=='.mpe' or file=='.mpv' or file=='.ogg' or file=='.mp4' or file=='.m4a' or file=='.avi' or file=='.wmv' or file=='.mov' or file=='.qt' or file=='.flv' or file=='.swf' or file=='.avchd':
                r_list.append(loc+'/'+i)
                mylist.insert(END,i)
                
            elif os.path.splitext(i)[1]=='':
                check(loc+'/'+i)

    except NotADirectoryError :
        de_list.append(loc)

    except PermissionError :
        pe_list.append(loc)
        
    except :
        print (' File does not exist : ',loc )
def main():
    global loc
    #check(loc)
    check(loc1)
    check(loc2)
    check(loc3)
    check(loc4)
    mylist.grid(row=1,column=0)
    scrl.config(command=mylist.yview)
    m=len(r_list)
def ref():
    global r_list
    print (len(r_list))
    while len(r_list)>0:
        mylist.delete(END)
        r_list.pop()
    mylist.delete(END)
    r_list=[]
    
start_button=Button(win,text='Start Scanning',command=main,width=50)
ref_button=Button(win,text='Clear',command=ref,width=50)
start_button.grid(row=0,column=0)
ref_button.grid(row=0,column=1)


print ('Done ')
win.mainloop()
file.close()
