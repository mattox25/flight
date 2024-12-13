from processing import *


# # Example Plots
# axs[0, 0].plot(Te_0_ex)
# axs[0, 0].set_xlabel('Time')
# axs[0, 0].set_ylabel('Electron Temp')

# axs[0, 1].plot(tite_ex)
# axs[0, 1].set_xlabel('Time')
# axs[0, 1].set_ylabel('tite')

# axs[1, 0].plot(taue_ex)
# axs[1, 0].set_xlabel('Time')
# axs[1, 0].set_ylabel('Confinement')

# axs[1, 1].plot(ni_0_ex)
# axs[1, 1].set_xlabel('Time')
# axs[1, 1].set_ylabel('Ion Density')
# plt.tight_layout()
# plt.savefig("Example_plots")
# plt.close()

# plt.plot(TP_ex)
# plt.ylabel("Triple Product")
# plt.xlabel("Time")
# plt.savefig("TP_Time_plot")
# plt.close()

fig, axs = plt.subplots(2, 3, figsize=(10, 8))
# x_range = [float(i) for i in indexes2]
x_range = np.arange(0.5, 10.5, 0.5)

trip_prod = np.array(TP_means)
yerr = np.array(TP_err)
# plt.errorbar(x_range, trip_prod, TP_err, fmt='o', markersize=4, 
#              ecolor='red', capsize=3)
# plt.ylabel("Triple Product")
# plt.xlabel("Power (MW)")
# plt.savefig("TP vs Power plot 2")
# plt.close()
# print(f'The maximum TP value is {max(trip_prod)} +/- {TP_err[np.argmax(trip_prod)]} at {x_range[np.argmax(trip_prod)]} MW')


# Plots against power
axs[0, 0].errorbar(x_range, Te0_means, Te0_err, fmt='o', markersize=3, 
             ecolor='red', capsize=3)
axs[0, 0].set_ylabel('Electron Temperature ')

axs[0, 1].errorbar(x_range, Ti0_means, Ti0_err, fmt='o', markersize=3, 
             ecolor='red', capsize=3)
axs[0, 1].set_ylabel('Ion Temperature')

axs[0, 2].errorbar(x_range, beta_means, beta_err, fmt='o', markersize=3, 
             ecolor='red', capsize=3)
axs[0, 2].set_ylabel('Beta')

axs[1, 0].errorbar(x_range, taue_means, taue_err, fmt='o', markersize=4, 
             ecolor='red', capsize=3)
axs[1, 0].set_ylabel('Confinement Time (s)')
axs[1, 0].set_xlabel('Power (MW)')

axs[1, 1].errorbar(x_range, ni0_means, ni0_err, fmt='o', markersize=4, 
             ecolor='red', capsize=3)
axs[1, 1].set_ylabel('Ion Density')
axs[1, 1].set_xlabel('Power (MW)')

axs[1, 2].errorbar(x_range, trip_prod, TP_err, fmt='o', markersize=4, 
             ecolor='red', capsize=3)
axs[1, 2].set_ylabel("Triple Product")
axs[1, 2].set_xlabel('Power (MW)')

plt.tight_layout()
# plt.subplots_adjust(hspace=0) 
plt.savefig("Parameter Plots vs Power")
plt.close()

