import tkinter as tk
from operation_menu import Menu2Page
from conversion_menu import Menu3Page

class SampleApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.configure(bg="red")

        # Create a container to hold the frames
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        # Create and add multiple frames (pages) to the frames dictionary
        for F in (MainPage, Menu2Page, Menu3Page):
            frame = F(container, self)
            self.frames[F.__name__] = frame  # Use the name of the class as the identifier
            frame.grid(row=0, column=0, sticky="nsew")

        # Show the initial frame (MainPage)
        self.show_frame("MainPage")  # Use string identifier

        self.resizable(False, False)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

# Define individual pages (frames)
class MainPage(tk.Frame):
    def __init__(self, parent, controller):
        
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Main Menu")
        label.pack(pady=50, padx=100)
        button1 = tk.Button(self, text="Go to Menu 2", command=lambda: controller.show_frame("Menu2Page"))  # Use string identifier
        button1.pack(padx=10, pady=10)
        button2 = tk.Button(self, text="Go to Menu 3", command=lambda: controller.show_frame("Menu3Page"))  # Use string identifier
        button2.pack(padx=10, pady=10)
        quit_button = tk.Button(self, text="Quit", command=controller.destroy)
        quit_button.pack(padx=10, pady=10)

if __name__ == "__main__":
    app = SampleApp()
    app.geometry("800x600")
    app.mainloop()

