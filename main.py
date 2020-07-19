import threading
import queue
import tkinter as tk
from tkinter import ttk
import time

slider = None
volEntry = None

def gui():

    def setvolume():
        global slider
        global volEntry

        volume = volEntry.get()
        slider.set(volume)

    def audioSlider(tab1):
        global slider
        global volEntry

        slider = tk.Scale(tab1, from_=0, to=100, length=400, orient=tk.HORIZONTAL)
        slider.set(50)

        volEntry = tk.Entry(tab1)

        volButton = tk.Button(tab1, text="Set Volume", command=setvolume)

        slider.place(x=90, y=0)
        volEntry.place(x=92, y=60)
        volButton.place(x=230, y=57)


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

    #frame = tk.Frame(root)
    #frame.pack()

    root.title("Common Settings")
    root.geometry(f"{width}x{height}")
    root.resizable(0, 0)
    root.iconbitmap(r"icon.ico")


    root.mainloop()

def audio():
    global volEntry
    global slider
    oldSlider =  None

    while True:
        if slider != oldSlider:
            sliderData = slider.get()
            print(oldSlider)

            volEntry.delete(0, tk.END)
            volEntry.insert(0, str(sliderData))

            oldSlider = sliderData

        time.sleep(0.01)
    

guiT = threading.Thread(target=gui)
audioT = threading.Thread(target=audio)

guiT.start()
audioT.start()