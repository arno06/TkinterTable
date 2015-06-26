from tkinter import *
from tkinter import ttk
from extraui import *


def parse(f, sep=";"):
    data = []
    keys = []
    i = 0
    for line in f:
        i += 1
        d = [value.replace("\n", "").replace('"', '') for value in line.split(sep)]
        if i == 1:
            keys = d
            continue
        item = {}
        for i, k in enumerate(keys):
            item[k] = d[i]
        data.append(item)
    return data

window = Tk()
window.columnconfigure(0, weight=1)
window.rowconfigure(1, weight=1)

main_panel = ttk.Frame(window, padding=(5, 5, 5, 5))
main_panel.grid(column=0, row=0, sticky=(N, S, E, W))
main_panel.columnconfigure(0, weight=1)
main_panel.rowconfigure(1, weight=1)

label = ttk.Label(main_panel, text="toto")
label.grid(column=0, row=0)

table = Table(window)
table.grid(column=0, row=1, sticky=(N, S, E, W))

f = open('../data/sample.csv', 'r')

table.data = parse(f)

window.mainloop()