set title 'Pressure inside GOM in Z'
set ylabel 'Pressure (bar)'
set xlabel 'Time (ps)'
set yrange [-5e3:5e3]
plot 'presZZ.txt' u 1:2  w lp lw 1.5 lc 'black' title 'Chempot8'
replot 'presZZ.txt' u 1:3  w lp lw 1.5 lc 'red' title 'Rolling Average'

pause -1 'Enter to EXIT'
