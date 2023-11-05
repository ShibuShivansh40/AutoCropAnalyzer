

# import everything from tkinter module
from tkinter import *
import subprocess
from tkinter import messagebox

def command_running(): 
        messagebox.showinfo('Process Status','Process has started!')
        return subprocess.Popen(args=['python', r'/home/face-ams-lite/RiceAgeFinder/Simultaneous_Realy&Stepper.py'])
 
# create a tkinter window
root = Tk()
root.title("Auto Crop Analyzer Results")
 
# Open window having dimension 100x100
root.geometry('400x200') 
 
# Create a Button
btn = Button(root, text = 'Run the Machine!', bd = '5', bg='cyan', anchor = CENTER, justify=CENTER, padx = 10, pady = 10,
             command = command_running).pack(side = 'top') 
# .pack -> Set the position of button on the top of window. 
 
root.mainloop()