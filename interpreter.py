import tkinter as tk
from tkinter import filedialog
import subprocess

# Create the main window
root = tk.Tk()
root.title("C- Interpreter")

# Create a terminal-like text box for displaying output
terminal_text = tk.Text(root, wrap=tk.WORD, height=20, width=80)
terminal_text.grid(column=0, row=0, padx=10, pady=10)

# Function to load a file
def load_file():
    file_path = filedialog.askopenfilename(
        title="Open C- File",
        filetypes=[("C- Files", "*.cm"), ("All Files", "*.*")]
    )
    if file_path:
        try:
            with open(file_path, 'r') as file:
                file_content = file.read()
                terminal_text.delete(1.0, tk.END)  # Clear existing text
                terminal_text.insert(tk.END, file_content)
        except Exception as e:
            terminal_text.insert(tk.END, f"Error loading file: {e}\n")

# Function to run the interpreter
def run_interpreter():
    # This is where you'd run the interpreter logic
    # For now, we'll simulate running a file using subprocess
    file_path = filedialog.askopenfilename(
        title="Select C- File to Run",
        filetypes=[("C- Files", "*.cm"), ("All Files", "*.*")]
    )
    if file_path:
        try:
            # Simulate running the C- interpreter with the selected file
            # Replace this command with the actual command to run your interpreter
            result = subprocess.run(['python3', 'interpreter.py', file_path], capture_output=True, text=True)
            terminal_text.insert(tk.END, result.stdout)
            if result.stderr:
                terminal_text.insert(tk.END, f"Error: {result.stderr}\n")
        except Exception as e:
            terminal_text.insert(tk.END, f"Error running interpreter: {e}\n")

# Create buttons for loading and running code
load_button = tk.Button(root, text="Load File", command=load_file)
load_button.grid(column=0, row=1, padx=10, pady=5)

run_button = tk.Button(root, text="Run Code", command=run_interpreter)
run_button.grid(column=0, row=2, padx=10, pady=5)

# Start the Tkinter loop
root.mainloop()
