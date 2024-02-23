import tkinter as tk

class Menu2Page(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        # Use a string identifier instead of MainPage
        back_button = tk.Button(self, text="Back to Main", command=lambda: controller.show_frame("MainPage"))  
        back_button.pack(side="top", anchor="nw")
        
        label = tk.Label(self, text="Menu 2")
        label.pack(pady=10, padx=10)
        

# Sample usage of the Menu2Page
if __name__ == "__main__":
    app = tk.Tk()
    app.geometry("800x600")
    page = Menu2Page(app, None)
    page.pack(fill="both", expand=True)
    app.mainloop()



