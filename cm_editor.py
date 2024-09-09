import tkinter as tk
from tkinter import filedialog, messagebox
from config import COLORS, KEYWORDS
from __interpreter__.interpreter import execute_code

class Editor:
    def __init__(self, root):
        self.root = root
        self.text = tk.Text(root, wrap=tk.WORD, font=("Consolas", 12))
        self.text.bind('<KeyRelease>', self.on_key_release)
        self.highlight_code()

        # Create output window
        self.output_window = tk.Toplevel(root)
        self.output_window.title("Output")
        self.output_text = tk.Text(self.output_window, wrap=tk.WORD, font=("Consolas", 12))
        self.output_text.pack(expand=True, fill=tk.BOTH)
        self.output_window.withdraw()  # Hide the window initially

    def open_file(self):
        filepath = filedialog.askopenfilename(filetypes=[("C- Files", "*.cm"), ("All Files", "*.*")])
        if filepath:  # Ensure a file was selected
            with open(filepath, 'r') as file:
                self.text.delete(1.0, tk.END)
                self.text.insert(tk.END, file.read())
                self.highlight_code()

    def save_file(self):
        filepath = filedialog.asksaveasfilename(defaultextension=".cm", filetypes=[("C- Files", "*.cm"), ("All Files", "*.*")])
        if filepath:  # Ensure a file path was provided
            with open(filepath, 'w') as file:
                file.write(self.text.get(1.0, tk.END))

    def run_code(self):
        code = self.text.get(1.0, tk.END)
        result = execute_code(code)
        self.output_text.delete(1.0, tk.END)  # Clear previous output
        if result is not None:
            self.output_text.insert(tk.END, f"Result: {result}")
        self.output_window.deiconify()  # Show the output window

    def highlight_code(self):
        self.text.tag_remove('keyword', '1.0', tk.END)
        self.text.tag_remove('comment', '1.0', tk.END)
        self.text.tag_remove('string', '1.0', tk.END)
        
        for keyword in KEYWORDS:
            start_pos = '1.0'
            while True:
                start_pos = self.text.search(keyword, start_pos, stopindex=tk.END, nocase=True, count=1)
                if not start_pos:
                    break
                end_pos = f"{start_pos}+{len(keyword)}c"
                self.text.tag_add('keyword', start_pos, end_pos)
                start_pos = end_pos

        self.text.tag_configure('keyword', foreground=COLORS['keyword'])
        self.text.tag_configure('comment', foreground=COLORS['comment'])
        self.text.tag_configure('string', foreground=COLORS['string'])

    def on_key_release(self, event):
        self.highlight_code()
