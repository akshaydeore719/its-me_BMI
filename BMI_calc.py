import tkinter as tk

def calculate_bmi():
    weight = float(weight_entry.get())
    height = float(height_entry.get())
    bmi = weight / (height ** 2)
    category = categorize_bmi(bmi)
    result_label.config(text=f"BMI: {bmi:.2f} ({category})")

def categorize_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Normal weight"
    elif 25 <= bmi < 30:
        return "Overweight"
    else:
        return "Obese"

# GUI setup
root = tk.Tk()
root.title("BMI Calculator")

weight_label = tk.Label(root, text="Weight (kg):")
weight_label.grid(row=0, column=0)

weight_entry = tk.Entry(root)
weight_entry.grid(row=0, column=1)

height_label = tk.Label(root, text="Height (m):")
height_label.grid(row=1, column=0)

height_entry = tk.Entry(root)
height_entry.grid(row=1, column=1)

calculate_button = tk.Button(root, text="Calculate", command=calculate_bmi)
calculate_button.grid(row=2, columnspan=2)

result_label = tk.Label(root, text="")
result_label.grid(row=3, columnspan=2)

root.mainloop()
