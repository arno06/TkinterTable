from tkinter import ttk
from tkinter import *


class Table(ttk.Frame):
    def __init__(self, master):
        ttk.Frame.__init__(self, master)
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.canvas = Canvas(self, borderwidth=0, background="#ffffff")
        sb = ttk.Scrollbar(self, orient="vertical", command=self.canvas.yview)
        sb.grid(column=1, row=0, sticky=(N, S, E, W))
        self.canvas.configure(yscrollcommand=sb.set)
        self.canvas.grid(column=0, row=0, sticky=(N, S, E, W))
        self.canvas.columnconfigure(0, weight=1)
        self.canvas.rowconfigure(0, weight=1)
        self.content = ttk.Frame(self.canvas)
        self.content.grid(column=0, row=0, sticky=(N, S, E, W))
        self._data = None
        self.interior_id = self.canvas.create_window(0,0, window=self.content, anchor="nw")
        self.content.bind("<Configure>", self.frame_configure_handler)
        self.canvas.bind('<Configure>', self.canvas_configure_handler)

        ttk.Style().configure('OddRow.TLabel', background='#fff')

    def canvas_configure_handler(self, event):
        if self.content.winfo_reqwidth() != self.canvas.winfo_width():
            self.canvas.itemconfigure(self.interior_id, width=self.canvas.winfo_width())

    def frame_configure_handler(self,  event):
        self.canvas.configure(scrollregion=self.canvas.bbox('all'))
        size = (self.content.winfo_reqwidth(), self.content.winfo_reqheight())
        self.canvas.config(scrollregion="0 0 %s %s" % size)
        if self.content.winfo_reqwidth() != self.canvas.winfo_width():
            self.canvas.config(width=self.content.winfo_reqwidth())

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        self._data = value
        self.draw()

    def draw(self):
        columns = list(self._data[0].keys())
        col = 0
        for c in columns:
            ttk.Label(self.content, text=c, padding=(7, 7, 7, 7)).grid(column=col, row=0, sticky=(N, S, W, E))
            self.content.columnconfigure(col, weight=1)
            col += 1
        row = 1
        for line in self._data:
            style = '' if row % 2 else 'OddRow.TLabel'
            col = 0
            for c in columns:
                ttk.Label(self.content, text=line[c], style=style, padding=(5, 5, 5, 5)).grid(column=col, row=row, sticky=(N, S, W, E))
                col += 1
            row += 1