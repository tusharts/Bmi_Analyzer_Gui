import tkinter as tk

def calculate_bmi():
    name = name_entry.get()
    weight = float(weight_entry.get())
    height = float(height_entry.get()) / 100  # Convert height from cm to meters

    # Calculate BMI
    BMI = weight / (height * height)
    result_label.config(text=f"Your BMI is: {BMI:.2f}")

    # Determine BMI category and display corresponding message
    if BMI < 18.5:
        category = "underweight"
    elif BMI < 24.9:
        category = "normal weight"
    elif BMI < 29.9:
        category = "overweight"
    elif BMI < 34.9:
        category = "obese"
    elif BMI < 39.9:
        category = "severely obese"
    else:
        category = "morbidly obese"

    message_label.config(text=f"{name}, you are {category}.")

# Create main window
window = tk.Tk()
window.title("BMI Calculator")

# Create input fields and labels
name_label = tk.Label(window, text="Enter your name:")
name_label.grid(row=0, column=0, sticky="w")
name_entry = tk.Entry(window)
name_entry.grid(row=0, column=1)

weight_label = tk.Label(window, text="Enter your weight in kilograms:")
weight_label.grid(row=1, column=0, sticky="w")
weight_entry = tk.Entry(window)
weight_entry.grid(row=1, column=1)

height_label = tk.Label(window, text="Enter your height in centimeters:")
height_label.grid(row=2, column=0, sticky="w")
height_entry = tk.Entry(window)
height_entry.grid(row=2, column=1)

calculate_button = tk.Button(window, text="Calculate BMI", command=calculate_bmi)
calculate_button.grid(row=3, columnspan=2)

# Display BMI result and message
result_label = tk.Label(window, text="")
result_label.grid(row=4, columnspan=2)

message_label = tk.Label(window, text="")
message_label.grid(row=5, columnspan=2)

# Start the GUI event loop
window.mainloop()
