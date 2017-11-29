reset
set terminal X11 enhanced font "arial,18"
set style line 1 lt 1 lw 1.5
set style line 2 lt 2 lw 1.5
set style line 3 lt 3 lw 1.5

set xlabel "E - E_{Fermi} (eV)"
set ylabel "DOS (states/atom*eV)"

plot 'DOS86' using 1:2 with lines ls 1 title "LDOS 86 s",     'DOS86' using 1:3 with lines ls 2 title "LDOS 86 p",     'DOS86' using 1:6 with lines ls 3 title "LDOS 86 d"
pause -1

# Uncomment to export eps file
#set term post eps color enhanced
#set output "LDOS86.eps"
#replot


