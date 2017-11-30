import numpy as np
import matplotlib.pyplot as plt


# Read data: 
force1,drift1,press1,toten1,kdens = np.loadtxt("result_kpoints.txt",unpack=True, skiprows=10)

force2,drift2,press2,toten2,kdens2 = np.loadtxt("result_kpoints2.txt",unpack=True, skiprows=1)

n = len(toten1)
m = n-1

toten_rel = np.zeros(n)
press_rel = np.zeros(n)
force_rel = np.zeros(n)
delta_toten_rel = np.zeros(m)
delta_press_rel = np.zeros(m)
delta_force_rel = np.zeros(m)
small_kdens = np.zeros(m)

for i in range(n):
   toten_rel[i] = np.abs(toten1[i]-toten2[i])
   press_rel[i] = np.abs(press1[i]-press2[i])
   force_rel[i] = np.abs(force1[i]-force2[i])

for i in range(m):
   delta_toten_rel[i] = np.abs((toten1[i+1]-toten1[i])-(toten2[i+1]-toten2[i]))
   delta_press_rel[i] = np.abs((press1[i+1]-press1[i])-(press2[i+1]-press2[i]))
   delta_force_rel[i] = np.abs((force1[i+1]-force1[i])-(force2[i+1]-force2[i]))
   small_kdens[i] = kdens[i]
   
plt.rcParams.update({'font.size': 14})

plt.figure();
plt.title("Relative change in difference energy")
plt.ylabel(r"$|\Delta E_{rel}| \, [meV]$")
plt.xlabel(r"k-point density $[\AA^{-1}]$")
plt.semilogy(small_kdens,delta_toten_rel,'-o')
plt.plot(kdens, [10**(-3) for i in range(n)],"--", label="1 meV")
plt.plot(kdens, [3*10**(-3) for i in range(n)],"--", label="3 meV")
#plt.ylim([min(delta_toten_rel)*10**3-50, max(delta_toten_rel)*10**3 ])
plt.legend()
plt.tight_layout()
plt.savefig("deltatotencurverel_kpoints_O2.pdf")

plt.figure(figsize=(6,7));
plt.subplot(2,1,1)
plt.title("Relative change in pressure")
plt.ylabel(r"$|\Delta P_{rel}| \, [kbar]$")
plt.xlabel(r"k-point density $[\AA^{-1}]$")
plt.semilogy(small_kdens, delta_press_rel,"-o")
plt.plot(kdens, [3 for i in range(n)],"--", label="3 kbar")
plt.plot(kdens, [1 for i in range(n)],"--", label="1 kbar")
plt.legend()
plt.tight_layout()

plt.subplot(2,1,2)
plt.title("Relative change in force")
plt.ylabel(r"$|\Delta F_{rel}| \, [eV/\AA]$")
plt.xlabel(r"k-point density  $[\AA^{-1}]$")
plt.semilogy(small_kdens, delta_force_rel,"-o")
plt.plot(kdens, [0.005 for i in range(n)],"--", label=r"0.005 eV/$\AA$")
plt.plot(kdens, [0.01 for i in range(n)],"--", label=r"0.01 eV/$\AA$")
plt.ylim([5*10**(-4), 5*10**(-1)])
plt.legend()
plt.tight_layout()
plt.savefig("deltaforcepressrel_kpoints_O2.pdf")
plt.show()
