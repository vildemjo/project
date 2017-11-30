import numpy as np
import matplotlib.pyplot as plt


# Read data: 
force1,drift1,press1,toten1,cutoff = np.loadtxt("result.txt",unpack=True, skiprows=1)

force2,drift2,press2,toten2,cutoff2 = np.loadtxt("result2.txt",unpack=True, skiprows=1)

n = len(toten1)
m = n-1

toten_rel = np.zeros(n)
press_rel = np.zeros(n)
force_rel = np.zeros(n)
delta_toten_rel = np.zeros(m)
delta_press_rel = np.zeros(m)
delta_force_rel = np.zeros(m)
small_cutoff = np.zeros(m)

for i in range(n):
   toten_rel[i] = np.abs(toten1[i]-toten2[i])
   press_rel[i] = np.abs(press1[i]-press2[i])
   force_rel[i] = np.abs(force1[i]-force2[i])

for i in range(m):
   delta_toten_rel[i] = np.abs((toten1[i+1]-toten1[i])-(toten2[i+1]-toten2[i]))
   delta_press_rel[i] = np.abs((press1[i+1]-press1[i])-(press2[i+1]-press2[i]))
   delta_force_rel[i] = np.abs((force1[i+1]-force1[i])-(force2[i+1]-force2[i]))
   small_cutoff[i] = cutoff[i]
   
plt.rcParams.update({'font.size': 14 })

plt.figure();
plt.title("Relative change in difference energy")
plt.ylabel(r"$|\Delta E_{rel}| \, [eV]$")
plt.xlabel(r"$E_{cut-off} \, [eV]$")
plt.semilogy(small_cutoff,delta_toten_rel,'-o')
plt.plot(cutoff, [10**(-3) for i in range(n)],"--", label="1 meV")
plt.plot(cutoff, [3*10**(-3) for i in range(n)],"--", label="3 meV")
#plt.ylim([min(delta_toten_rel)*10**3-50, max(delta_toten_rel)*10**3 ])
plt.legend()
plt.tight_layout()
plt.savefig("deltatotencurverel_O2.pdf")

plt.figure(figsize=(6,8));
plt.subplot(2,1,1)
plt.title("Relative change in pressure")
plt.ylabel(r"$|\Delta P_{rel}|$ [kbar]")
plt.xlabel(r"$E_{cut-off} \, [eV]$")
plt.semilogy(small_cutoff[1:], delta_press_rel[1:],"-o")
plt.plot(cutoff, [3 for i in range(n)],"--", label="3 kbar")
plt.plot(cutoff, [1 for i in range(n)],"--", label="1 kbar")
plt.legend()
plt.tight_layout()

plt.subplot(2,1,2)
plt.title("Relative change in force")
plt.ylabel(r"$|\Delta F_{rel}| \, [eV/\AA]$")
plt.xlabel(r"$E_{cut-off} \, [eV]$")
plt.semilogy(small_cutoff[1:], delta_force_rel[1:],"-o")
plt.plot(cutoff, [0.005 for i in range(n)],"--", label=r"0.005 eV/$\AA$")
plt.plot(cutoff, [0.01 for i in range(n)],"--", label=r"0.01 eV/$\AA$")
plt.legend()
plt.tight_layout()
plt.savefig("deltaforcepressrel_O2.pdf")
plt.show()
