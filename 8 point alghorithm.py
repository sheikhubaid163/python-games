import tkinter as tk

# Constants
WIDTH, HEIGHT = 400, 300
BORDER_COLOR = "black"
FILL_COLOR = "blue"
BACKGROUND_COLOR = "white"

# Create GUI window
root = tk.Tk()
root.title("Basic Paint Application")

canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg=BACKGROUND_COLOR)
canvas.pack()

# Draw rectangle
rect = canvas.create_rectangle(100, 50, 300, 200, outline=BORDER_COLOR, width=3, fill=BACKGROUND_COLOR)


# Flood fill function (horizontal and vertical only)
def flood_fill(x, y, target_color, new_color):
    stack = [(x, y)]

    while stack:
        cx, cy = stack.pop()
        pixel = canvas.find_closest(cx, cy)  # Get closest pixel

        if canvas.itemcget(pixel, "fill") != target_color:
            continue

        canvas.itemconfig(pixel, fill=new_color)

        # Spread in 4 directions (horizontal & vertical)
        stack.extend([(cx + 1, cy), (cx - 1, cy), (cx, cy + 1), (cx, cy - 1)])


# Mouse click event handler
def on_click(event):
    x, y = event.x, event.y
    coords = canvas.coords(rect)

    # Check if click is inside rectangle
    if coords[0] < x < coords[2] and coords[1] < y < coords[3]:
        flood_fill(x, y, BACKGROUND_COLOR, FILL_COLOR)


# Bind mouse click event
canvas.bind("<Button-1>", on_click)

root.mainloop()
