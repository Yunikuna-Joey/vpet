# Python GUI interpreter 
import tkinter as tk 

# Utilize PIL (Python Imaging Library) to load pet images and animations 
from PIL import Image, ImageTk

# import time to determine when to execute animations
import time

# creating a window 
root = tk.Tk()
root.geometry('400x400')

# create a canvas to display the pet 
canvas = tk.Canvas(root, width=200, height=200)
canvas.pack()

# find a way to load pet images and animations
use_image = Image.open('Toadpicture.png')
pet_image = ImageTk.PhotoImage(use_image)

pet_label = tk.Label(canvas, image=pet_image)
pet_label.image = pet_image
pet_label.pack()

# main loop to update pet state 
def animation(): 
    frames = [Image.open('Toadpicture.png'), Image.open('toad2.jpg')]
    # measured in milliseconds
    duration = 200  
    
    for frame in frames: 
        pet_label.config(image=ImageTk.PhotoImage(frame))
        pet_label.update()
        time.sleep(duration / 1000)

   
animation() 
# update_pet() 
root.mainloop() 