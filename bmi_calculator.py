import tkinter as tk
from tkinter import messagebox
from datetime import datetime

# ---------------- FUNCTION ----------------
def calculate_bmi():
    try:
        name = name_entry.get().strip()
        phone = phone_entry.get().strip()
        age = age_entry.get().strip()
        height_cm = float(height_entry.get())
        weight = float(weight_entry.get())
        gender = gender_var.get()

        # Validation
        if name == "" or phone == "" or age == "":
            messagebox.showerror("Error", "Please fill all fields.")
            return

        if not phone.isdigit() or len(phone) != 10:
            messagebox.showerror("Error", "Enter valid 10-digit phone number.")
            return

        if not age.isdigit():
            messagebox.showerror("Error", "Age must be numeric.")
            return

        if height_cm <= 0 or weight <= 0:
            messagebox.showerror("Error", "Height and Weight must be positive.")
            return

        # Convert height to meters
        height_m = height_cm / 100

        # BMI Calculation
        bmi = weight / (height_m * height_m)

        # Categorization
        if bmi < 18.5:
            category = "Underweight"
        elif bmi < 25:
            category = "Normal"
        elif bmi < 30:
            category = "Overweight"
        else:
            category = "Extremely Obese"

        # Display result
        bmi_value_label.config(text=f"{bmi:.2f}")
        result_label.config(text=category)

        # Save to file
        with open("bmi_records.txt", "a") as file:
            file.write(
                f"{datetime.now()} | {name} | {phone} | {age} | {gender} | BMI: {bmi:.2f} | {category}\n"
            )

        # Simulated SMS confirmation
        messagebox.showinfo(
            "SMS Sent",
            f"Hello {name},\n\nYour BMI is {bmi:.2f}\nCategory: {category}\n\n(Result saved & SMS simulated)"
        )

    except ValueError:
        messagebox.showerror("Error", "Please enter valid numeric values.")


# ---------------- UI DESIGN ----------------
window = tk.Tk()
window.title("BMI Calculator")
window.geometry("420x720")
window.configure(bg="#e6e6e6")
window.resizable(False, False)

# Card
card = tk.Frame(window, bg="white")
card.place(relx=0.5, rely=0.5, anchor="center", width=380, height=680)

# Title
tk.Label(card, text="BMI Calculator",
         font=("Segoe UI", 20, "bold"),
         fg="#2d8cf0", bg="white").pack(pady=20)

# Name
tk.Label(card, text="User Name", bg="white",
         font=("Segoe UI", 11)).pack()
name_entry = tk.Entry(card, font=("Segoe UI", 12))
name_entry.pack(pady=8, ipadx=10, ipady=6)

# Phone
tk.Label(card, text="Mobile Number", bg="white",
         font=("Segoe UI", 11)).pack()
phone_entry = tk.Entry(card, font=("Segoe UI", 12))
phone_entry.pack(pady=8, ipadx=10, ipady=6)

# Age
tk.Label(card, text="Age", bg="white",
         font=("Segoe UI", 11)).pack()
age_entry = tk.Entry(card, font=("Segoe UI", 12))
age_entry.pack(pady=8, ipadx=10, ipady=6)

# Height
tk.Label(card, text="Height (cm)", bg="white",
         font=("Segoe UI", 11)).pack()
height_entry = tk.Entry(card, font=("Segoe UI", 12))
height_entry.pack(pady=8, ipadx=10, ipady=6)

# Weight
tk.Label(card, text="Weight (kg)", bg="white",
         font=("Segoe UI", 11)).pack()
weight_entry = tk.Entry(card, font=("Segoe UI", 12))
weight_entry.pack(pady=8, ipadx=10, ipady=6)

# Gender Selection
gender_var = tk.StringVar(value="Male")

gender_frame = tk.Frame(card, bg="white")
gender_frame.pack(pady=10)

tk.Radiobutton(gender_frame, text="Male",
               variable=gender_var, value="Male",
               bg="white", font=("Segoe UI", 11)).pack(side="left", padx=15)

tk.Radiobutton(gender_frame, text="Female",
               variable=gender_var, value="Female",
               bg="white", font=("Segoe UI", 11)).pack(side="left", padx=15)

# Calculate Button
tk.Button(card, text="Calculate BMI",
          bg="#2d8cf0", fg="white",
          font=("Segoe UI", 13, "bold"),
          command=calculate_bmi).pack(pady=20, ipadx=20, ipady=8)

# Result Section
tk.Label(card, text="BMI:",
         bg="white",
         font=("Segoe UI", 12, "bold")).pack()

bmi_value_label = tk.Label(card, text="--",
                           bg="white",
                           font=("Segoe UI", 18))
bmi_value_label.pack()

tk.Label(card, text="Result:",
         bg="white",
         font=("Segoe UI", 12, "bold")).pack(pady=5)

result_label = tk.Label(card, text="--",
                        bg="white",
                        font=("Segoe UI", 16))
result_label.pack()

window.mainloop()
