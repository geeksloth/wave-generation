import matplotlib.pyplot as plt
import numpy as np


samplingRate = 100   # samples per second
time_start = 0      # x-axis, generally starts at Zero
time_stop = 1       # x-axis, time

step = 1.0/samplingRate
t = np.arange(time_start, time_stop, step)

# wave_1 generation
frequency = 1
amplitude = 3
wave_1 = amplitude * np.sin( 2 * np.pi * frequency * t)

# wave_2 generation
frequency = 4
amplitude = 1
wave_2 = amplitude * np.sin( 2 * np.pi * frequency * t)

# wave_3 generation
frequency = 7   
amplitude = 0.5
wave_3 = amplitude * np.sin( 2 * np.pi * frequency * t)

# sum all waves together
wave = wave_1 + wave_2 + wave_3

# plotting
fig, axs = plt.subplots(2, 2)
axs[0, 0].plot(t, wave_1)
axs[0, 0].set_title('wave_1')
axs[0, 1].plot(t, wave_2, 'tab:orange')
axs[0, 1].set_title('wave_2')
axs[1, 0].plot(t, wave_3, 'tab:green')
axs[1, 0].set_title('wave_3')
axs[1, 1].plot(t, wave, 'tab:red')
axs[1, 1].set_title('wave')

for ax in axs.flat:
    ax.set(xlabel='time', ylabel='magnitude')

# Hide x labels and tick labels for top plots and y ticks for right plots.
for ax in axs.flat:
    ax.label_outer()

plt.show()