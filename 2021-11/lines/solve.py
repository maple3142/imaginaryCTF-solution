import tkinter as tk
import json

with open("image.json") as f:
    img = json.load(f)["image"]

app = tk.Tk()
app.title("flag")

cvs = tk.Canvas(app, width=img["width"], height=img["height"])
cvs.pack()

lineWidth = img["lineThickness"]
for line in img["lines"]:
    sx = line["from"]["x"]
    sy = line["from"]["y"]
    tx = line["to"]["x"]
    ty = line["to"]["y"]
    cvs.create_line(sx, sy, tx, ty, width=lineWidth)

app.mainloop()

# ictf{budg3t_v3ct0r_graph1c5}
