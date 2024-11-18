import tkinter as tk
import time
import json

letters="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!?.,'()"
high="bfdghjklpqtABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!?()"
low="gjpqy"
upnn="'"
downnn=".,"
drawings={}
rep=2

class DrawingApp:
    def __init__(self, root, lett):
        self.writing=True
        self.root = root
        self.root.title("Draw the character \""+lett+"\"")
        self.root.state("zoomed")
        self.canvas = tk.Canvas(root, bg="white")
        self.canvas.pack(fill=tk.BOTH, expand=True)
        self.root.update_idletasks()
        self.canvas.config(width=self.root.winfo_width(), height=self.root.winfo_height())
        self.canvas.pack()
        self.sx=9999999999999999999999
        self.sy=9999999999999999999999
        self.final=[]

        self.is_drawing = False
        self.last_action_time = None
        self.trail = []
        self.timer_id = None
        self.canvas.bind("<ButtonPress-1>", self.start_drawing)
        self.canvas.bind("<B1-Motion>", self.draw)
        self.canvas.bind("<ButtonRelease-1>", self.stop_drawing)

    def start_drawing(self, event):
        self.is_drawing = True
        self.trail.append(("START", (event.x, event.y)))
        self.reset_timer()
        self.sx=min(self.sx, event.x)
        self.sy=min(self.sy, event.y)

    def draw(self, event):
        if self.is_drawing:
            x, y = event.x, event.y
            self.trail.append(("NORMAL", (x, y)))
            self.canvas.create_oval(x - 2, y - 2, x + 2, y + 2, fill="black")
        self.reset_timer()
        self.sx=min(self.sx, event.x)
        self.sy=min(self.sy, event.y)

    def stop_drawing(self, event):
        self.is_drawing = False
        self.last_action_time = time.time()
        self.trail.append(("STOP", (event.x, event.y)))
        self.start_timer()
        self.sx=min(self.sx, event.x)
        self.sy=min(self.sy, event.y)

    def start_timer(self):
        if self.timer_id:
            self.root.after_cancel(self.timer_id)
        self.timer_id = self.root.after(1000, self.close_window)

    def reset_timer(self):
        if self.timer_id:
            self.root.after_cancel(self.timer_id)
            self.timer_id = None

    def close_window(self):
        self.root.quit()
        self.root.destroy()
        self.writing=False
    
    def data(self):
        for i in self.trail:
            self.final.append((i[0], (i[1][0]-self.sx,i[1][1]-self.sy)))
        return self.final

def letter(lett):
    root = tk.Tk()
    app = DrawingApp(root, lett)
    root.mainloop()
    while app.writing:
        pass
    return app.data()

if __name__ == "__main__":
    for l in letters:
        drawings[l]=[]
        for i in range(rep):
            drawings[l].append(letter(l))
    
    for d in drawings:
        h=5
        sh=0
        if d in high:
            h=10
        if d in low:
            sh=-5
        mx=0
        mn=9999999999
        if d in upnn:
            h=3
            sh=7
        elif d in downnn:
            h=3
        for i in range(rep):
            for point in range(len(drawings[d][i])):
                mx=max(drawings[d][i][point][1][1], mx)
                mn=min(drawings[d][i][point][1][1], mn)
            m=abs(mx)+abs(mn)
            for point in range(len(drawings[d][i])):
                drawings[d][i][point]=(drawings[d][i][point][0], (drawings[d][i][point][1][0]*h/m, sh+(m-drawings[d][i][point][1][1])*h/m))



with open("font.json", "w") as f:
    json.dump(drawings, f, ensure_ascii=False, indent=4)