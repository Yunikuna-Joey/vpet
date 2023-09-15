import tkinter as tk 

# creating a window 
root = tk.Tk()
root.geometry('400x400')

# create a canvas to display the pet 
canvas = tk.Canvas(root, width=200, height=200)
canvas.pack()

# find a way to load pet images and animations


# main loop to update pet state 

def update_pet(): 
    # update pet's animations / behavior here  
    root.after(100, update_pet)

update_pet() 

root.mainloop() 