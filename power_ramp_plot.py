
from power_ramp_processing import *

fig, axs = plt.subplots(2, 3, figsize=(10, 8), sharex=True)
max = -1
min = 40
peak_index = 69
# Example Plots
axs[0, 0].scatter(pnbi[mask], Te0[mask])
axs[0, 0].axvline(x=3e6, color='g', linestyle='--', label='3MW')
axs[0, 0].axvline(pnbi[peak_index], color='r', linestyle='--', label=f'{np.round(pnbi[peak_index]/1e6, 2)}MW')
axs[0, 0].legend()
axs[0, 0].set_ylabel('Electron Temp')

axs[0, 1].scatter(pnbi[mask], Ti0[mask])
axs[0, 1].axvline(x=3e6, color='g', linestyle='--', label='3MW')
axs[0, 1].axvline(pnbi[peak_index], color='r', linestyle='--', label=f'{np.round(pnbi[peak_index]/1e6, 2)}MW')
axs[0, 1].set_ylabel('Ion Temp')
axs[0, 1].legend()

axs[0, 2].scatter(pnbi[mask], beta[mask])
axs[0, 2].axvline(pnbi[peak_index], color='r', linestyle='--', label=f'{np.round(pnbi[peak_index]/1e6, 2)}MW')
axs[0, 2].axvline(x=3e6, color='g', linestyle='--', label='3MW')
axs[0, 2].set_ylabel('Beta')
axs[0, 2].legend()

axs[1, 0].scatter(pnbi[mask], taue[mask])
axs[1, 0].axvline(x=3e6, color='g', linestyle='--', label='3MW')
axs[1, 0].axvline(pnbi[peak_index], color='r', linestyle='--', label=f'{np.round(pnbi[peak_index]/1e6, 2)}MW')
axs[1, 0].set_xlabel('Power')
axs[1, 0].set_ylabel('Confinement')

axs[1, 1].scatter(pnbi[mask], ni0[mask])
axs[1, 1].axvline(x=3e6, color='g', linestyle='--', label='3MW')
axs[1,1].axvline(pnbi[peak_index], color='r', linestyle='--', label=f'{np.round(pnbi[peak_index]/1e6, 2)}MW')
axs[1, 1].set_xlabel('Power')
axs[1, 1].set_ylabel('Ion Density')


axs[1, 2].scatter(pnbi[mask], TP[mask])
axs[1, 2].axvline(pnbi[peak_index], color='r', linestyle='--', label=f'{np.round(pnbi[peak_index]/1e6, 2)}MW')
axs[1, 2].axvline(x=3e6, color='g', linestyle='--', label='3MW')
axs[1, 2].set_xlabel('Power')
axs[1, 2].set_ylabel("Triple Product")

plt.tight_layout()
plt.subplots_adjust(hspace=0)
plt.savefig("power_ramp_plots\power_ramp_plots")
plt.close()

print(TP[peak_index])