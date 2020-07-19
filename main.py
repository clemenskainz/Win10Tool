import threading
import queue
import tkinter as tk
from tkinter import ttk
import time

slider = None

def gui():

    def audioSlider(tab1):
        global slider

        slider = tk.Scale(tab1, from_=0, to=200, length=400, orient=tk.HORIZONTAL)
        slider.set(50)
        slider.pack()


    def tabSetup():
        tabControl = ttk.Notebook(root)

        tab1 = ttk.Frame(tabControl)
        tab2 = ttk.Frame(tabControl)
        tab3 = ttk.Frame(tabControl)

        tabControl.add(tab1, text="Volume")
        tabControl.add(tab2, text="WLAN")
        tabControl.add(tab3, text="Bluetooth")

        audioSlider(tab1)

        tabControl.pack(expand=1, fill="both")

   

    height = "400"
    width = "600"

    root = tk.Tk()
    tabSetup()

    root.title("Common Settings")
    root.geometry(f"{width}x{height}")
    root.minsize(500, 300)
    root.iconbitmap(r"icon.ico")

    

    root.mainloop()

def audio():
    global slider

    while True:
        if slider != None:
            print(slider.get())
        time.sleep(0.05)
    

guiT = threading.Thread(target=gui)
audioT = threading.Thread(target=audio)

guiT.start()
audioT.start()