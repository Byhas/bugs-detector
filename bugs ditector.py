import tkinter as tk
from tkinter import filedialog
import subprocess

class BugDetector:
    def __init__(self, master):
        self.master = master
        self.master.title("Python Bug Detector")

        self.file_path = tk.StringVar()
        self.text = tk.Text(self.master, height=20, width=60)
        self.text.pack()

        browse_button = tk.Button(self.master, text="Browse", command=self.browse_file)
        browse_button.pack()

        detect_button = tk.Button(self.master, text="Detect Bugs", command=self.detect_bugs)
        detect_button.pack()

    def browse_file(self):
        self.file_path.set(filedialog.askopenfilename())

    def detect_bugs(self):
        if not self.file_path.get():
            self.text.insert(tk.END, "Please select a file to detect bugs.\n")
        else:
            process = subprocess.Popen(f"pylint {self.file_path.get()}", stdout=subprocess.PIPE, shell=True)
            output, _ = process.communicate()
            self.text.delete(1.0, tk.END)
            self.text.insert(tk.END, output.decode())

if __name__ == "__main__":
    root = tk.Tk()
    app = BugDetector(root)
    root.mainloop()
