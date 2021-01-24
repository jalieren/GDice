from tkinter import *
import random
import time

# window params
root = Tk()
root.title('GDice')
root.geometry('600x550')

# making canvas
canvas = Canvas(root, width = 512, height = 512)
canvas.pack()

# dice images
cube1 = PhotoImage(file='dice1.png')
cube2 = PhotoImage(file='dice2.png')
cube3 = PhotoImage(file='dice3.png')
cube4 = PhotoImage(file='dice4.png')
cube5 = PhotoImage(file='dice5.png')
cube6 = PhotoImage(file='dice6.png')

def dice():
	canvas.delete('all')
	num = random.randint(1, 6) # random number
	if num == 1:
		canvas.create_image(0, 0, anchor = NW, image = cube1) # 1

	elif num == 2:
		canvas.create_image(0, 0, anchor = NW, image = cube2) # 2

	elif num == 3:
		canvas.create_image(0, 0, anchor = NW, image = cube3) # 3

	elif num == 4:
		canvas.create_image(0, 0, anchor = NW, image = cube4) # 4

	elif num == 5:
		canvas.create_image(0, 0, anchor = NW, image = cube5) # 5

	elif num == 6:
		canvas.create_image(0, 0, anchor = NW, image = cube6) # 6
	
# button
button = Button(root, text = 'Go', width = 10, height = 1, command = dice)
button.pack(side = 'top')

root.mainloop()