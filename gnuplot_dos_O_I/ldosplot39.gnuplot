reset
set terminal X11 enhanced font "arial,18"
set style line 1 lt 1 lw 1.5
set style line 2 lt 2 lw 1.5
set style line 3 lt 3 lw 1.5

set xlabel "E - E_{Fermi} (eV)"
set ylabel "DOS (states/atom*eV)"

plot 'DOS39' using 1:2 with lines ls 1 title "LDOS 39 s",     'DOS39' using 1:3 with lines ls 2 title "LDOS 39 p",     'DOS39' using 1:6 with lines ls 3 title "LDOS 39 d"
pause -1

# Uncomment to export eps file
#set term post eps color enhanced
#set output "LDOS39.eps"
#replot


