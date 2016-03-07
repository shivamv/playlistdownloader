from Tkinter import *
import os
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
  os.system("pkill -9 youtube-dl")


download_button = Button(master, text="Download", width=25, bd=2,command=callback)
download_button.pack()
cancel_button = Button(master, text="Cancel", width=25, bd=2,command=abort)
cancel_button.pack()

mainloop()
e = Entry(master, width=1000)
e.pack()

text = e.get()