import tkinter as tk
from tkinter import filedialog
import os

class TextEditor:
    def __init__(self, master):
        self.master = master
        master.title("Text Editor")
        master.geometry("800x800")
        
        self.button_frame = tk.Frame(master, width=100)
        self.button_frame.pack(side=tk.LEFT, fill=tk.Y)
        self.text_frame = tk.Frame(master, width=700)
        self.text_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        self.open_button = tk.Button(self.button_frame, text="Open", command=self.open_file)
        self.open_button.pack(side=tk.TOP, pady=10, padx=20)
        self.save_button = tk.Button(self.button_frame, text="Save", command=self.save_file)
        self.save_button.pack(side=tk.TOP, pady=10, padx=20)
        
        self.text = tk.Text(self.text_frame)
        self.text.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        self.master.minsize(800, 800)
        self.text.config(width=800)
        
        master.bind("<Configure>", self.resize_text)
        self.file_path = None
        
    def open_file(self):
        self.file_path = filedialog.askopenfilename()
        if self.file_path:
            self.text.delete("1.0", tk.END)
            with open(self.file_path, "r") as input_file:
                text = input_file.read()
                self.text.insert(tk.END, text)
            
    def save_file(self):
        if self.file_path:
            text = self.text.get("1.0", tk.END)
            with open(self.file_path, "w") as output_file:
                output_file.write(text)
        else:
            file_path = filedialog.asksaveasfilename(defaultextension=".txt")
            if file_path:
                self.file_path = file_path
                text = self.text.get("1.0", tk.END)
                try:
                    with open(file_path, "w") as output_file:
                        output_file.write(text)
                except OSError:
        
                    folder_path = os.path.dirname(file_path)
                    os.makedirs(folder_path, exist_ok=True)
                    with open(file_path, "w") as output_file:
                        output_file.write(text)
    
    def resize_text(self, event):
        self.text.config(width=event.width-100)
        
window = tk.Tk()
text_editor = TextEditor(window)
window.mainloop()