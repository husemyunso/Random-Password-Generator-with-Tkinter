import tkinter as tk
from tkinter import ttk
import random
import string


# Function to generate random password
def generate_password():
    try:
        length = int(password_length.get())
    except ValueError:
        label_result['text'] = "Enter a valid length!"
        return

    use_uppercase = var_uppercase.get()
    use_numbers = var_numbers.get()
    use_special = var_special.get()

    if length <= 0:
        label_result['text'] = "Length must be greater than 0!"
        return

    # Build the character pool based on user selection
    char_pool = string.ascii_lowercase
    if use_uppercase:
        char_pool += string.ascii_uppercase
    if use_numbers:
        char_pool += string.digits
    if use_special:
        char_pool += string.punctuation

    if not char_pool:
        label_result['text'] = "Select at least one character type!"
        return

    # Generate password
    password = ''.join(random.choice(char_pool) for _ in range(length))
    text_password.delete("1.0", tk.END)  # Clear previous password
    text_password.insert(tk.END, password)  # Insert new password


# Tkinter Setup
root = tk.Tk()
root.title("Random Password Generator")
root.geometry("400x350")
root.configure(bg="lightblue")

# Title
label_title = tk.Label(root, text="Random Password Generator", font=("Arial", 16, "bold"), bg="lightblue")
label_title.pack(pady=10)

# Password Length
frame_length = tk.Frame(root, bg="lightblue")
frame_length.pack(pady=10)

label_length = tk.Label(frame_length, text="Password Length:", font=("Arial", 12), bg="lightblue")
label_length.grid(row=0, column=0, padx=5)

password_length = ttk.Entry(frame_length, width=10)
password_length.grid(row=0, column=1, padx=5)

# Character Options
frame_options = tk.Frame(root, bg="lightblue")
frame_options.pack(pady=10)

var_uppercase = tk.BooleanVar()
check_uppercase = tk.Checkbutton(frame_options, text="Include Uppercase Letters", font=("Arial", 12), variable=var_uppercase, bg="lightblue")
check_uppercase.grid(row=0, column=0, sticky="w")

var_numbers = tk.BooleanVar()
check_numbers = tk.Checkbutton(frame_options, text="Include Numbers", font=("Arial", 12), variable=var_numbers, bg="lightblue")
check_numbers.grid(row=1, column=0, sticky="w")

var_special = tk.BooleanVar()
check_special = tk.Checkbutton(frame_options, text="Include Special Characters", font=("Arial", 12), variable=var_special, bg="lightblue")
check_special.grid(row=2, column=0, sticky="w")

# Generate Button
btn_generate = tk.Button(root, text="Generate Password", font=("Arial", 12, "bold"), bg="darkblue", fg="white", command=generate_password)
btn_generate.pack(pady=20)

# Password Display
text_password = tk.Text(root, height=2, width=30, font=("Arial", 12), wrap=tk.WORD)
text_password.pack(pady=10)

label_result = tk.Label(root, text="", font=("Arial", 10), bg="lightblue")
label_result.pack()

# Footer
label_footer = tk.Label(root, text="Created with ❤️ using Tkinter", font=("Arial", 10), bg="lightblue")
label_footer.pack(side="bottom", pady=10)

root.mainloop()
