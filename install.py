import os
import threading
from threading import Thread
def install_celery():
  os.system("sudo apt-get install python-celery")
  from celery import chord
task1=os.system("sudo add-apt-repository ppa:nilarimogard/webupd8")
task2=os.system("sudo apt-get update")
task3=os.system("sudo apt-get install youtube-dl")
task4=os.system("sudo apt-get install gnome-panel")
task5=os.system("sudo gnome-desktop-item-edit --create-new ~/Desktop")
def callback():
  os.system("sudo apt-get install python-tk")
  result=chord(task1,task2,task3,task4,task5)
  result.get()
thread1 = Thread(target = install_celery, args = ())
thread1.start
callback()
