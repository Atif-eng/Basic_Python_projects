import tkinter as tk

class DrawingApp:
    def __init__(self, root):
        self.root = root
        self.canvas = tk.Canvas(root, width=800, height=600)
        self.canvas.pack()
        self.canvas.bind("<1>", self.start_drawing)
        self.canvas.bind("<B1-Motion>", self.draw_line)
        self.old_x, self.old_y = 0, 0
        self.line_width = 5
        self.color = 'black'
        self.create_menu()

    def start_drawing(self, event):
        self.old_x, self.old_y = event.x, event.y

    def draw_line(self, event):
        self.canvas.create_line(self.old_x, self.old_y, event.x, event.y, 
                                width=self.line_width, fill=self.color)
        self.old_x, self.old_y = event.x, event.y

    def create_menu(self):
        menubar = tk.Menu(self.root)
        self.root.config(menu=menubar)
        filemenu = tk.Menu(menubar)
        menubar.add_cascade(label="File", menu=filemenu)
        filemenu.add_command(label="Clear", command=self.canvas.delete("all"))
        filemenu.add_command(label="Exit", command=self.root.quit)

        colormenu = tk.Menu(menubar)
        menubar.add_cascade(label="Color", menu=colormenu)
        for color in ['black', 'red', 'blue']:
            colormenu.add_command(label=color.capitalize(), command=lambda c=color: self.change_color(c))

        sizemenu = tk.Menu(menubar)
        menubar.add_cascade(label="Size", menu=sizemenu)
        for size in [1, 5, 10]:
            sizemenu.add_command(label=str(size), command=lambda s=size: self.change_size(s))

    def change_color(self, color):
        self.color = color

    def change_size(self, size):
        self.line_width = size

if __name__ == "__main__":
    root = tk.Tk()
    app = DrawingApp(root)
    root.mainloop()
