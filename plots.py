from processing import *
fig, axs = plt.subplots(2, 2, figsize=(10, 8))

# Example Plots
axs[0, 0].plot(Te_0_ex)
axs[0, 0].set_xlabel('Time')
axs[0, 0].set_ylabel('Electron Temp')

axs[0, 1].plot(tite_ex)
axs[0, 1].set_xlabel('Time')
axs[0, 1].set_ylabel('tite')

axs[1, 0].plot(taue_ex)
axs[1, 0].set_xlabel('Time')
axs[1, 0].set_ylabel('Confinement')

axs[1, 1].plot(ni_0_ex)
axs[1, 1].set_xlabel('Time')
axs[1, 1].set_ylabel('Ion Density')
plt.tight_layout()
plt.savefig("Example_plots")
plt.close()

# Final 

plt.plot(TP_ex)
plt.ylabel("Triple Product")
plt.xlabel("Time")
plt.savefig("TP_Time_plot")
plt.close()

plt.scatter(np.arange(1, 41, 2), np.array(TP_means)/1e22)
plt.ylabel("Triple Product")
plt.xlabel("Power")
plt.savefig("TP_Power_plot")
plt.close()
