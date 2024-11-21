import tkinter as tk
from tkinter import ttk
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def plot_waves():
    for widget in plot_frame.winfo_children():
        widget.destroy()

    # input values 
    freq1 = float(freq1_entry.get())
    amp1 = float(amp1_entry.get())
    phase1 = float(phase1_entry.get())
    freq2 = float(freq2_entry.get())
    amp2 = float(amp2_entry.get())
    phase2 = float(phase2_entry.get())
    
   
    Y1 = amp1 * np.exp(1j * phase1)  # Phasor for wave 1
    Y2 = amp2 * np.exp(1j * phase2)  # Phasor for wave 2
    
    # Find the x and y components of each phasor
    Y1x = amp1 * np.cos(phase1)
    Y1y = amp1 * np.sin(phase1)
    
    Y2x = amp2 * np.cos(phase2)
    Y2y = amp2 * np.sin(phase2)
    
    #components
    X_total = Y1x + Y2x
    Y_total = Y1y + Y2y
    
    # magnitude
    RR=(X_total**2 + Y_total**2)  # Magnitude
    R=np.sqrt(RR)
    theta = np.arctan2(Y_total, X_total)  # Phase
    
    # Generate the time values and the waves
    t = np.linspace(0, 2 * np.pi, 1000)
    wave1 = amp1 * np.cos(freq1 * t + phase1)
    wave2 = amp2 * np.cos(freq2 * t + phase2)
    resultant_wave = R * np.cos(freq1 * t + theta)  # Resultant wave in time domain
    
    fig, axs = plt.subplots(2, 2, figsize=(10, 6), gridspec_kw={'height_ratios': [1, 1]})
    fig.patch.set_facecolor('black')  # Set background color for the whole figure

    for i, ax in enumerate(axs.flat):
        ax.set_facecolor('black')
        ax.grid(True, color='green', linestyle='--', linewidth=0.5)
        ax.tick_params(colors='green', which='both')
        ax.spines['bottom'].set_color('green')
        ax.spines['top'].set_color('green')
        ax.spines['right'].set_color('green')
        ax.spines['left'].set_color('green')
    
    # Wave 1 
    axs[0, 0].plot(t, wave1, color='lime')
    axs[0, 0].set_title('Wave 1', color='lime')

    #  Wave 2 
    axs[0, 1].plot(t, wave2, color='orange')
    axs[0, 1].set_title('Wave 2', color='orange')

    # Resultant Wave 
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

    canvas = FigureCanvasTkAgg(fig, master=plot_frame)
    canvas.draw()
    canvas.get_tk_widget().pack()

    # equations box
    wave1_equation = f"Wave 1: y1(t) = {amp1} * sin({freq1} * t + {phase1})"
    wave2_equation = f"Wave 2: y2(t) = {amp2} * sin({freq2} * t + {phase2})"
    resultant_equation = f"Resultant: y(t) = {R:.2f} * sin({freq1} * t + {theta:.2f})"

    eq_label1.config(text=wave1_equation)
    eq_label2.config(text=wave2_equation)
    eq_label3.config(text=resultant_equation)

root = tk.Tk()
root.title("Oscilloscope Wave Parameters")

input_frame = ttk.Frame(root)
input_frame.grid(row=0, column=0, padx=10, pady=10)

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

submit_btn = ttk.Button(input_frame, text="Plot Waves", command=plot_waves)
submit_btn.grid(column=0, row=6, columnspan=2)

plot_frame = ttk.Frame(root)
plot_frame.grid(row=0, column=1, padx=10, pady=10)

equation_frame = ttk.LabelFrame(root, text="Wave Equations")
equation_frame.grid(row=1, column=1, padx=10, pady=10)

eq_label1 = ttk.Label(equation_frame, text="")
eq_label1.pack()

eq_label2 = ttk.Label(equation_frame, text="")
eq_label2.pack()

eq_label3 = ttk.Label(equation_frame, text="")
eq_label3.pack()

root.mainloop()
