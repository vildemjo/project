import numpy as np
import matplotlib.pyplot as plt


# Read data: 
force,drift,press,toten,cutoff = np.loadtxt("result.txt",unpack=True, skiprows=1)

n = len(toten)-1

delta_toten = np.zeros(n)
small_cutoff = np.zeros(n)
delta_press = np.zeros(n)
delta_force = np.zeros(n)
limit = np.zeros(n)

for i in range(n):
   delta_toten[i] = np.abs(toten[i+1]-toten[i])
   delta_press[i] = np.abs(press[i+1]-press[i])
   delta_force[i] = np.abs(force[i+1]-force[i])
   small_cutoff[i] = cutoff[i]
   limit[i] = np.log10(3*10**(-3))

plt.rcParams.update({'font.size': 14})

plt.figure(1);
plt.title("Total energy vs. cut-off energy")
plt.ylabel(r"$|E_{tot}| \, [eV]$")
plt.xlabel(r"$E_{cut-off} \, [eV]$")
plt.plot(cutoff,toten,'-o')
plt.tight_layout()
plt.savefig("totencurve.pdf")


plt.figure(2);
plt.title("Change in total energy vs. cut-off energy")
plt.ylabel(r"$\log(|\Delta E_{tot}|) \, [\log(eV)]$")
plt.xlabel(r"$E_{cut-off} \, [eV]$")
plt.plot(small_cutoff, np.log10(delta_toten),"-o")
plt.plot(small_cutoff, limit,"--", label="3 meV")
plt.legend()
plt.tight_layout()
plt.savefig("deltatotencurve.pdf")


plt.figure(3);
plt.title("Change in pressure vs. cut-off energy")
plt.ylabel(r"$|\Delta P| \, [kbar]$")
plt.xlabel(r"$E_{cut-off} \, [eV]$")
plt.plot(small_cutoff, delta_press,"-o")
plt.plot(small_cutoff, [3 for i in range(n)],"--", label="3 kbar")
plt.legend()
plt.tight_layout()
plt.savefig("deltapresscurve.pdf")

plt.figure(4);
plt.title("Change in force vs. cut-off energy")
plt.ylabel(r"$|\Delta F| \, [eV/Aa]$")
plt.xlabel(r"$E_{cut-off} \, [eV]$")
plt.plot(small_cutoff, delta_force,"-o")
plt.plot(small_cutoff, [0.05 for i in range(n)],"--", label="0.05 eV/Aa")
plt.plot(small_cutoff, [0.005 for i in range(n)],"--", label="0.005 eV/Aa")
plt.legend(loc=2)
plt.tight_layout()
plt.savefig("deltaforcecurve.pdf")
plt.show()
