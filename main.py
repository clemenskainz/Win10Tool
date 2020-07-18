import threading
import tkinter as tk
from tkinter import ttk

def gui():
    def tabSetup():
        tabControl = ttk.Notebook(root)

        tab1 = ttk.Frame(tabControl)
        tab2 = ttk.Frame(tabControl)
        tab3 = ttk.Frame(tabControl)

        tabControl.add(tab1, text="WLAN")
        tabControl.add(tab2, text="Bluetooth")
        tabControl.add(tab3, text="Volume")

        tabControl.pack(expand=1, fill="both")

    height = "400"
    width = "600"

    root = tk.Tk()

    root.title("Common Settings")
    root.geometry(f"{width}x{height}")
    root.minsize(500, 300)
    root.iconbitmap(r"icon.ico")

    tabSetup()

    root.mainloop()

guiT = threading.Thread(target=gui)

guiT.start()