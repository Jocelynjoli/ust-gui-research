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
    
    # Convert the phases from radians if necessary (they are assumed to be in radians here)
    
    # Calculate the phasors (complex numbers) for both waves
    Y1 = amp1 * np.exp(1j * phase1)  # Phasor for wave 1
    Y2 = amp2 * np.exp(1j * phase2)  # Phasor for wave 2
    
    # Add the phasors to get the resultant phasor
    Y_total = Y1 + Y2
    
    # Get the resultant amplitude and phase
    amp_res = np.abs(Y_total)  # Magnitude of the resultant phasor
    phase_res = np.angle(Y_total)  # Phase of the resultant phasor
    
    # Generate the time values and the waves
    t = np.linspace(0, 2 * np.pi, 1000)
    wave1 = amp1 * np.sin(freq1 * t + phase1)
    wave2 = amp2 * np.sin(freq2 * t + phase2)
    resultant_wave = amp_res * np.sin(freq1 * t + phase_res)  # Resultant wave in time domain
    
    # Create a 2x2 grid layout for subplots
    fig, axs = plt.subplots(2, 2, figsize=(10, 6), gridspec_kw={'height_ratios': [1, 1]})
    fig.patch.set_facecolor('black')  # Set background color for the whole figure

    # Configure the appearance of each axis
    for i, ax in enumerate(axs.flat):
        ax.set_facecolor('black')
        ax.grid(True, color='green', linestyle='--', linewidth=0.5)
        ax.tick_params(colors='green', which='both')
        ax.spines['bottom'].set_color('green')
        ax.spines['top'].set_color('green')
        ax.spines['right'].set_color('green')
        ax.spines['left'].set_color('green')
    
    # Plot Wave 1 (top left)
    axs[0, 0].plot(t, wave1, color='lime')
    axs[0, 0].set_title('Wave 1', color='lime')

    # Plot Wave 2 (top right)
    axs[0, 1].plot(t, wave2, color='orange')
    axs[0, 1].set_title('Wave 2', color='orange')

    # Plot the Resultant Wave (bottom, spanning both columns)
    axs[1, 0].remove()  # Remove the bottom-left axis
    axs[1, 1].remove()  # Remove the bottom-right axis
    ax_res = fig.add_subplot(2, 1, 2)  # Add a new subplot that spans both columns
    ax_res.set_facecolor('black')
    ax_res.plot(t, resultant_wave, color='cyan')
    ax_res.set_title('Resultant Wave', color='cyan')
    ax_res.grid(True, color='green', linestyle='--', linewidth=0.5)
    ax_res.tick_params(colors='green', which='both')
    ax_res.spines['bottom'].set_color('green')
    ax_res.spines['top'].set_color('green')
    ax_res.spines['right'].set_color('green')
    ax_res.spines['left'].set_color('green')

    fig.tight_layout()

    # Display the plot in the Tkinter Canvas
    canvas = FigureCanvasTkAgg(fig, master=plot_frame)
    canvas.draw()
    canvas.get_tk_widget().pack()

    # Display the equations of the waves in the equations box
    wave1_equation = f"Wave 1: y1(t) = {amp1} * sin({freq1} * t + {phase1})"
    wave2_equation = f"Wave 2: y2(t) = {amp2} * sin({freq2} * t + {phase2})"
    resultant_equation = f"Resultant: y(t) = {amp_res:.2f} * sin({freq1} * t + {phase_res:.2f})"

    # Create labels for equations
    eq_label1.config(text=wave1_equation)
    eq_label2.config(text=wave2_equation)
    eq_label3.config(text=resultant_equation)

# Main GUI setup
root = tk.Tk()
root.title("Oscilloscope Wave Parameters")

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
