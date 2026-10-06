import tkinter as tk

ROWS, COLS, SIZE = 10, 10, 50
grid = [[' ' for _ in range(COLS)] for _ in range(ROWS)]
colors = {}

def draw_grid():
    for i in range(ROWS):
        for j in range(COLS):
            color = colors.get((i, j), "white")
            canvas.create_rectangle(j * SIZE, i * SIZE, (j+1)*SIZE, (i+1)*SIZE, fill=color, outline="black")

def flood_fill(x, y, target, replacement):
    if x < 0 or x >= ROWS or y < 0 or y >= COLS:
        return
    if colors.get((x, y), "white") != target:
        return
    if colors.get((x, y), "white") == replacement:
        return

    colors[(x, y)] = replacement
    flood_fill(x+1, y, target, replacement)
    flood_fill(x-1, y, target, replacement)
    flood_fill(x, y+1, target, replacement)
    flood_fill(x, y-1, target, replacement)

def on_click(event):
    x, y = event.y // SIZE, event.x // SIZE
    if (x, y) in borders:
        return
    target = colors.get((x, y), "white")
    flood_fill(x, y, target, "blue")
    canvas.delete("all")
    draw_grid()

root = tk.Tk()
root.title("Flood Fill")

canvas = tk.Canvas(root, width=COLS * SIZE, height=ROWS * SIZE)
canvas.pack()
canvas.bind("<Button-1>", on_click)

# Create border at column 5
borders = {(i, 5) for i in range(ROWS)}
for pos in borders:
    colors[pos] = "black"

draw_grid()
root.mainloop()
