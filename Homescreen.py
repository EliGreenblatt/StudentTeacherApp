import tkinter as tk
from PIL import Image, ImageTk
import os

class HomeScreen:
    def __init__(self,root):
        self.root = root
        self.root.title("Home Screen")
        
        script_dir = os.path.dirname(os.path.abspath(__file__))
        image_path = os.path.join(script_dir, "Images", "background.png")
        
        
        self.b_img = tk.PhotoImage(file=image_path)
        
        b_label = tk.Label(root, image=self.b_img)
        b_label.place(relwidth=1, relheight=1)
        
        login_b = tk.Button(root, text="Login", command = self.login_click,width=13,height=2)
        login_b.place(x=150, y=280)        
        
        register_b = tk.Button(root, text="Register", command = self.register_blick,width=13,height=2)
        register_b.place(x=150, y=320)        

        
        window_width = 400
        window_height = 500
        self.root.geometry(f"{window_width}x{window_height}")

    def login_click(self):
        print("Button login pressed and eli is a genius wait whaaaaa")
    
    def register_blick(self):
        print("Button register clicked and no one likes evyatar") 
        
if __name__ == "__main__":
    root = tk.Tk()
    app = HomeScreen(root)
    root.mainloop()
    