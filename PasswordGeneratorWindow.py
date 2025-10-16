from tkinter import *
import random
import string
from tkinter import messagebox

class PasswordGeneratorWindow:
    def __init__(self, master):
        self.master = master
        self.master.title("Password Generator")
        self.master.geometry("400x350")
        self.master.resizable(True, True)

        self.label_length = Label(master, text="Password Length:")
        self.label_length.pack(pady=10)

        self.entry_length = Entry(master)
        self.entry_length.pack(pady=5)

        self.var_uppercase = IntVar()
        self.check_uppercase = Checkbutton(master, text="Include Uppercase Letters", variable=self.var_uppercase)
        self.check_uppercase.pack()

        self.var_lowercase = IntVar()
        self.check_lowercase = Checkbutton(master, text="Include Lowercase Letters", variable=self.var_lowercase)
        self.check_lowercase.pack()

        self.var_digits = IntVar()
        self.check_digits = Checkbutton(master, text="Include Digits", variable=self.var_digits)
        self.check_digits.pack()

        self.var_special = IntVar()
        self.check_special = Checkbutton(master, text="Include Special Characters", variable=self.var_special)
        self.check_special.pack()

        self.button_generate = Button(master, text="Generate Password", command=self.generate_password)
        self.button_generate.pack(pady=10)

        self.text_password = Text(master, height=2, width=30)
        self.text_password.pack(pady=5)

        self.button_copy = Button(master, text="Copy to Clipboard", command=self.copy_to_clipboard)
        self.button_copy.pack(pady=5)

        self.button_save = Button(master, text="Save Password", command=self.save_password)
        self.button_save.pack(pady=5)

    def generate_password(self):
        try:
            length = int(self.entry_length.get())
            if length <= 0:
                raise ValueError
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid positive integer for password length.")
            return

        char_pool = ""
        if self.var_uppercase.get():
            char_pool += string.ascii_uppercase
        if self.var_lowercase.get():
            char_pool += string.ascii_lowercase
        if self.var_digits.get():
            char_pool += string.digits
        if self.var_special.get():
            char_pool += string.punctuation

        if not char_pool:
            messagebox.showerror("No Character Types Selected", "Please select at least one character type.")
            return
        password = ''.join(random.choice(char_pool) for _ in range(length))
        self.text_password.delete(1.0, END)
        self.text_password.insert(END, password)
        self.text_password.config(state=DISABLED)

    def copy_to_clipboard(self):
        password = self.text_password.get(1.0, END).strip()
        if password:
            self.master.clipboard_clear()
            self.master.clipboard_append(password)
            messagebox.showinfo("Copied", "Password copied to clipboard.")
        else:
            messagebox.showwarning("No Password", "No password to copy. Please generate one first.")
    def save_password(self):
        password = self.text_password.get(1.0, END).strip()
        if password:
            with open("saved_passwords.txt", "a") as file:
                file.write(password + "\n")
            messagebox.showinfo("Saved", "Password saved to saved_passwords.txt.")
        else:
            messagebox.showwarning("No Password", "No password to save. Please generate one first.")
if __name__ == "__main__":
    root = Tk()
    app = PasswordGeneratorWindow(root)
    root.mainloop()

