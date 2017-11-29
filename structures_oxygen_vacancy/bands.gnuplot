set xtics ("V" 0.0, "Y" 0.54675, "{/Symbol G}" 1.0935, "M" 2.24493, "A" 3.45314, "L" 4.60456)
set terminal X11 enhanced font 'arial,18'
set ylabel 'E - E_{Fermi} (eV)'
set xlabel 'k points'
unset key
set grid xtics

# Uncomment to produce eps figure
#set term post eps color enhanced font 'arial,18'
#set output 'bands.eps'

plot 'bands' using 1:2 with lines lt -1
pause -1
