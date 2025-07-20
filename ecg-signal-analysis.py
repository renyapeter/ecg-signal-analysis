import pandas as pd
import matplotlib.pyplot as plt
import os
print(os.getcwd())


# Load the synthetic ECG file
data = pd.read_csv("synthetic_ecg_sample.csv")

# Check structure
print(data.head())

# Plot ECG signal
plt.figure(figsize=(10, 4))
plt.plot(data['Time'], data['ECG'])
plt.title("Synthetic ECG Signal")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.grid(True)
plt.show()
from scipy.signal import find_peaks

# Extract ECG signal
ecg = data['ECG']

# Detect peaks (you can tune distance/height as needed)
peaks, _ = find_peaks(ecg, distance=200)
peak_times=data['Time'][peaks]
rr_intervals=peak_times.diff()
clean_rr=rr_intervals.dropna()
heart_rates=60/clean_rr
average_bpm=heart_rates.mean()
print("Average heart rate is=",average_bpm)


# Plot signal with peaks marked
plt.figure(figsize=(10, 4))
plt.plot(data['Time'], ecg, label="ECG Signal")
plt.plot(data['Time'][peaks], ecg[peaks], "rx", label="Detected Peaks")
plt.title("ECG Signal with R-Peak Detection")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.legend()
plt.grid(True)
plt.show()

#to plot heart rates over time
plt.figure(figsize=(10,4))
plt.plot(peak_times[1:],heart_rates,label="Heart rates")
plt.xlabel("Time")
plt.ylabel("heart rates")
plt.title("Heart rates over time")
plt.legend()
plt.grid(True)
plt.show()

#to display heart rate above each R-peak
print(f"ECG amplitude min: {ecg.min()}, max: {ecg.max()}")

plt.plot(data['Time'], ecg, label="ECG Signal")
plt.plot(data['Time'][peaks], ecg[peaks], "rx", label="Detected Peaks")
for i in range(len(heart_rates)):
    x=peak_times.iloc[i+1]
    y=ecg[peaks[i+1]]
    bpm=heart_rates.iloc[i]
    plt.text(x, y + 0.5, f"{round(bpm)}", fontsize=10, color='red', fontweight='bold')


plt.title("ECG Signal with Heart Rate Annotations")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()



