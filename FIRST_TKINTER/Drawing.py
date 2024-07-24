from tkinter import *

# Create the main window
window = Tk()

# Set up the Canvas
c = Canvas(window, width=500, height=500)
c.pack()

# Create the dotted lines
c.create_line(0, 0, 500, 500, width=5, fill="violet", dash=(3, 3))
c.create_line(500, 0, 0, 500, width=5, fill="violet", dash=(3, 3))

# Calculate the center of the canvas
center_x = 500 // 2
center_y = 500 // 2

# Define the size of the rectangle
rect_width = 100
rect_height = 100

# Calculate the top-left and bottom-right coordinates of the rectangle
top_left_x = center_x - rect_width // 2
top_left_y = center_y - rect_height // 2
bottom_right_x = center_x + rect_width // 2
bottom_right_y = center_y + rect_height // 2

# Create the rectangle
c.create_rectangle(top_left_x, top_left_y, bottom_right_x, bottom_right_y,fill="red", outline="black", width=5)

# Start the Tkinter main loop
window.mainloop()
