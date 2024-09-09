import tkinter as tk
from cm_editor import Editor

root = tk.Tk()
root.title("C- Editor")

# Create an instance of Editor and pass the root window
editor = Editor(root)
editor.text.pack(expand=True, fill=tk.BOTH)

menu = tk.Menu(root)
root.config(menu=menu)
file_menu = tk.Menu(menu)
menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Open", command=editor.open_file)
file_menu.add_command(label="Save", command=editor.save_file)
file_menu.add_command(label="Exit", command=root.quit)

root.mainloop()