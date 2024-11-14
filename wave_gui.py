import tkinter as tk
from tkinter import ttk
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def plot_waves():
    # Clear previous plots and equations
    for widget in plot_frame.winfo_children():
        widget.destroy()

    # Get the input values from the user
    freq1 = float(freq1_entry.get())
    amp1 = float(amp1_entry.get())
    phase1 = float(phase1_entry.get())
    freq2 = float(freq2_entry.get())
    amp2 = float(amp2_entry.get())
    phase2 = float(phase2_entry.get())
    
    # Generate the time values and the waves
    t = np.linspace(0, 2 * np.pi, 1000)
    wave1 = amp1 * np.sin(freq1 * t + phase1)
    wave2 = amp2 * np.sin(freq2 * t + phase2)
    resultant_wave = wave1 + wave2

    # Create a Matplotlib figure and axes with smaller size
    fig, axs = plt.subplots(3, 1, figsize=(4, 6))  # Adjust the size here

    # Plot Wave 1
    axs[0].plot(t, wave1, label='Wave 1', color='blue')
    axs[0].set_title('Wave 1')
    axs[0].grid()

    # Plot Wave 2
    axs[1].plot(t, wave2, label='Wave 2', color='orange')
    axs[1].set_title('Wave 2')
    axs[1].grid()

    # Plot the Resultant Wave
    axs[2].plot(t, resultant_wave, label='Resultant Wave', color='green')
    axs[2].set_title('Resultant Wave')
    axs[2].grid()

    fig.tight_layout()

    # Display the plot in the Tkinter Canvas
    canvas = FigureCanvasTkAgg(fig, master=plot_frame)  # Embed Matplotlib figure in `plot_frame`
    canvas.draw()
    canvas.get_tk_widget().pack()

    # Display the equations of the waves in the equations box
    wave1_equation = f"Wave 1: y1(t) = {amp1} * sin({freq1} * t + {phase1})"
    wave2_equation = f"Wave 2: y2(t) = {amp2} * sin({freq2} * t + {phase2})"
    resultant_equation = f"Resultant: y(t) = y1(t) + y2(t)"

    # Create labels for equations
    eq_label1.config(text=wave1_equation)
    eq_label2.config(text=wave2_equation)
    eq_label3.config(text=resultant_equation)

# Main GUI setup
root = tk.Tk()
root.title("Wave Parameters Input")

# Frame for the input fields
input_frame = ttk.Frame(root)
input_frame.grid(row=0, column=0, padx=10, pady=10)

# Input fields for wave parameters
ttk.Label(input_frame, text="Wave 1 Frequency").grid(column=0, row=0)
freq1_entry = ttk.Entry(input_frame)
freq1_entry.grid(column=1, row=0)

ttk.Label(input_frame, text="Wave 1 Amplitude").grid(column=0, row=1)
amp1_entry = ttk.Entry(input_frame)
amp1_entry.grid(column=1, row=1)

ttk.Label(input_frame, text="Wave 1 Phase (radians)").grid(column=0, row=2)
phase1_entry = ttk.Entry(input_frame)
phase1_entry.grid(column=1, row=2)

ttk.Label(input_frame, text="Wave 2 Frequency").grid(column=0, row=3)
freq2_entry = ttk.Entry(input_frame)
freq2_entry.grid(column=1, row=3)

ttk.Label(input_frame, text="Wave 2 Amplitude").grid(column=0, row=4)
amp2_entry = ttk.Entry(input_frame)
amp2_entry.grid(column=1, row=4)

ttk.Label(input_frame, text="Wave 2 Phase (radians)").grid(column=0, row=5)
phase2_entry = ttk.Entry(input_frame)
phase2_entry.grid(column=1, row=5)

# Submit button to trigger the plot
submit_btn = ttk.Button(input_frame, text="Plot Waves", command=plot_waves)
submit_btn.grid(column=0, row=6, columnspan=2)

# Frame for displaying the plot
plot_frame = ttk.Frame(root)
plot_frame.grid(row=0, column=1, padx=10, pady=10)

# Frame for displaying equations
equation_frame = ttk.LabelFrame(root, text="Wave Equations")
equation_frame.grid(row=1, column=1, padx=10, pady=10)

# Labels for displaying equations
eq_label1 = ttk.Label(equation_frame, text="")
eq_label1.pack()

eq_label2 = ttk.Label(equation_frame, text="")
eq_label2.pack()

eq_label3 = ttk.Label(equation_frame, text="")
eq_label3.pack()

root.mainloop()
