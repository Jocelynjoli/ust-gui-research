import tkinter as tk
from tkinter import ttk
import numpy as np
import matplotlib.pyplot as plt
'''Hello'''

def plot_waves():
    freq1 = float(freq1_entry.get())
    amp1 = float(amp1_entry.get())
    phase1 = float(phase1_entry.get())
    freq2 = float(freq2_entry.get())
    amp2 = float(amp2_entry.get())
    phase2 = float(phase2_entry.get())
    
    t = np.linspace(0, 2 * np.pi, 1000)

    wave1 = amp1 * np.sin(freq1 * t + phase1)
    wave2 = amp2 * np.sin(freq2 * t + phase2)
    resultant_wave = wave1 + wave2

    plt.figure(figsize=(10, 6))
    
    plt.subplot(3, 1, 1)
    plt.plot(t, wave1, label='Wave 1', color='blue')
    plt.title('Wave 1')
    plt.grid()

    plt.subplot(3, 1, 2)
    plt.plot(t, wave2, label='Wave 2', color='orange')
    plt.title('Wave 2')
    plt.grid()

    plt.subplot(3, 1, 3)
    plt.plot(t, resultant_wave, label='Resultant Wave', color='green')
    plt.title('Resultant Wave')
    plt.grid()

    plt.tight_layout()
    plt.show()

root = tk.Tk()
root.title("Wave Parameters Input")

ttk.Label(root, text="Wave 1 Frequency").grid(column=0, row=0)
freq1_entry = ttk.Entry(root)
freq1_entry.grid(column=1, row=0)

ttk.Label(root, text="Wave 1 Amplitude").grid(column=0, row=1)
amp1_entry = ttk.Entry(root)
amp1_entry.grid(column=1, row=1)

ttk.Label(root, text="Wave 1 Phase (radians)").grid(column=0, row=2)
phase1_entry = ttk.Entry(root)
phase1_entry.grid(column=1, row=2)

ttk.Label(root, text="Wave 2 Frequency").grid(column=0, row=3)
freq2_entry = ttk.Entry(root)
freq2_entry.grid(column=1, row=3)

ttk.Label(root, text="Wave 2 Amplitude").grid(column=0, row=4)
amp2_entry = ttk.Entry(root)
amp2_entry.grid(column=1, row=4)

ttk.Label(root, text="Wave 2 Phase (radians)").grid(column=0, row=5)
phase2_entry = ttk.Entry(root)
phase2_entry.grid(column=1, row=5)

submit_btn = ttk.Button(root, text="Plot Waves", command=plot_waves)
submit_btn.grid(column=0, row=6, columnspan=2)

root.mainloop()
