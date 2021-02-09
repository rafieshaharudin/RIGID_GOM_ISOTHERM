# Aim : To plot the evolution of number of water molecules adsorbed and its rolling average

set title 'Number of water molecules adsorbed'
set ylabel 'N'
set xlabel 'Number of MC steps'
set key bottom right
plot 'r' u 1:4 w lp lw 2.0 lc 'black' title 'N water adsorbed'
replot 'N_WATER' u 1:5 w lp lw 2.0 lc 'blue' title 'Rolling average'

pause -1 'ENTER TO EXIT'
