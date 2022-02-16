import tkinter

root = tkinter.Tk()
root.title("Draw Road")
canvas = tkinter.Canvas(width = 800, height= 600, bg = "blue")
canvas.pack()

canvas.create_rectangle(0, 300, 800, 600, fill = "green")

BORD_COL = ["white", "silver", "gray", "azure4", "gray30", "gray20", "gray10", "black"]

h = 2
y = 300

for i in range(1, 25):
    w = i * i * 1.5
    x = 400 - w / 2
    
    col = BORD_COL[i % len(BORD_COL)]
    canvas.create_rectangle(x, y, x + w, y + h, fill = col)

    y = y + h
    h = h + 1

root.mainloop()