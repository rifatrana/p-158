#bad Geometry error
from tkinter import * 
root=Tk()
root.title("Geometry Error")

try:
    root.geometry("600")
except:
       print("Bad geometry error,only one dimension passesed in geometry instead of two")
        
root.mainloop()    
