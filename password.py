import heapq
import tkinter as tk
from tkinter import messagebox

# Function to compute password strength score
def compute_strength(password):
    score = sum([
        any(ch.isdigit() for ch in password),
        any(ch.islower() for ch in password),
        any(ch.isupper() for ch in password),
        any(ch in "!@#$%^&*()_-+=" for ch in password),
        len(password) >= 8
    ])
    return score

# Function to classify passwords using heap
def classify_password(password):
    strength_score = compute_strength(password)
    heap = [(strength_score, password)]
    heapq.heapify(heap)
    
    _, pwd = heapq.heappop(heap)

    # Determine strength category and give tips
    if strength_score <= 2:
        return "Weak", "Try adding uppercase, numbers, symbols, and using at least 8 characters."
    elif strength_score == 3:
        return "Medium", "You're almost there! Add a symbol or a capital letter."
    else:
        return "Strong", "Great! Your password is strong."

# Function to analyze password and update UI
def process_input():
    password = password_entry.get().strip()

    if not password:
        output_var.set("Please enter a password.")
        result_label.config(fg="black")
        return

    strength, tip = classify_password(password)
    output_var.set(f"Password Strength: {strength}")

    # Change color based on strength
    if strength == "Weak":
        result_label.config(fg="red")
        messagebox.showinfo("Tip", tip)
    elif strength == "Medium":
        result_label.config(fg="orange")
        messagebox.showinfo("Tip", tip)
    else:
        result_label.config(fg="green")

# Function to show/hide password
def toggle_password():
    if show_var.get():
        password_entry.config(show="")
    else:
        password_entry.config(show="*")

# Tkinter GUI setup
app = tk.Tk()
app.title("Enhanced Password Strength Analyzer")
app.geometry("420x280")

# Widgets
tk.Label(app, text="Enter your password:").pack(pady=5)

password_entry = tk.Entry(app, width=40, show="*")
password_entry.pack(pady=5)

# Checkbox to show/hide password
show_var = tk.BooleanVar()
tk.Checkbutton(app, text="Show Password", variable=show_var, command=toggle_password).pack(pady=2)

# Analyze button
tk.Button(app, text="Analyze Strength", command=process_input).pack(pady=10)

# Output label
output_var = tk.StringVar()
result_label = tk.Label(app, textvariable=output_var, font=("Arial", 12, "bold"))
result_label.pack(pady=10)

# Run the app
app.mainloop()
