from Tkinter import *
import threading
import os
from threading import Thread
master = Tk()

L1 = Label(master, text="URL:")
L1.pack()
e = Entry(master)
e.pack()

e.focus_set()

def callback():
  link = e.get()
  os.system("youtube-dl "+ link)

def abort():
  print "Aborting...."
  os.system("killall youtube-dl")

link = e.get()
thread1 = Thread(target = callback, args = ())
thread2 = Thread(target = abort, args = ())

download_button = Button(master, text="Download", width=25, bd=2,command=thread1.start)
download_button.pack()
cancel_button = Button(master, text="Cancel", width=25, bd=2,command=thread2.start)
cancel_button.pack()

mainloop()
e = Entry(master, width=1000)
e.pack()

text = e.get()