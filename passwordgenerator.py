import tkinter as tk
import random
import string

def generate_password():
    length = int(entry_length.get())
    complexity = int(entry_complexity.get())
    
    characters = ''
    
    if var_uppercase.get():
        characters += string.ascii_uppercase
        
    if var_lowercase.get():
        characters += string.ascii_lowercase
        
    if var_digits.get():
        characters += string.digits
        
    if var_special.get():
        characters += string.punctuation
        
    password = ''.join(random.choice(characters) for _ in range(length))
    
    lbl_generated.config(text="Generated Password: "+ password)
    
def reset_fields():
    entry_length.delete(0, tk.END)
    entry_complexity.delete(0, tk.END)
    lbl_generated.config(text="")
    var_uppercase.set(False)
    var_lowercase.set(False)
    var_digits.set(False)
    var_special.set(False)
    
root = tk.Tk()
root.title("Password Generator")

root.geometry("400x300")

lbl_length = tk.Label(root, text="Password Length:")
lbl_length.grid(row=0, column=0, padx=10, pady=5)
entry_length = tk.Entry(root)
entry_length.grid(row=0, column=1, padx=10, pady=5)

lbl_complexity = tk.Label(root, text="Password Complexity:(1: Low, 2: Medium, 3: High):")
lbl_complexity.grid(row=1, column=0, padx=10, pady=5)
entry_complexity = tk.Entry(root)
entry_complexity.grid(row=1, column=1, padx=10, pady=5)

var_uppercase = tk.BooleanVar()
chk_uppercase = tk.Checkbutton(root, text="Include Uppercase", variable=var_uppercase)
chk_uppercase.grid(row=2, column=0, columnspan=2, padx=10, pady=5, sticky="n")

var_lowercase = tk.BooleanVar()
chk_lowercase = tk.Checkbutton(root, text="Include Lowercase", variable=var_lowercase)
chk_lowercase.grid(row=3, column=0, columnspan=2, padx=10, pady=5, sticky="n")

var_digits = tk.BooleanVar()
chk_digits = tk.Checkbutton(root, text="Include Digits", variable=var_digits)
chk_digits.grid(row=4, column=0, columnspan=2, padx=10, pady=5, sticky="n")

var_special = tk.BooleanVar()
chk_special = tk.Checkbutton(root, text="Include Special Characters", variable=var_special)
chk_special.grid(row=5, column=0, columnspan=2, padx=10, pady=5, sticky="n")

btn_generate = tk.Button(root, text="Generate Password", command=generate_password)
btn_generate.grid(row=6, column=0, padx=10, pady=5)

btn_reset = tk.Button(root, text="Reset", command=reset_fields)
btn_reset.grid(row=6, column=1, padx=10, pady=5)

lbl_generated = tk.Label(root, text="")
lbl_generated.grid(row=7, columnspan=2, padx=10, pady=5)

root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_rowconfigure(2, weight=1)
root.grid_rowconfigure(3, weight=1)
root.grid_rowconfigure(4, weight=1)
root.grid_rowconfigure(5, weight=1)

root.mainloop()