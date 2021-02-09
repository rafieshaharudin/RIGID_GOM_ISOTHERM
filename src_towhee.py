# Aim : To compile number of water molecules from towhee_output file from each cycle

from pandas import DataFrame
import os
from tkinter import Tcl


f99 = open('N_WATER', 'w')
f99.write('# steps   energy(kJ/mol) P(bar)   N_water  Rolling_average\n ')

# open empty list to append collected data later

file_list = []
SOL_list = []
Ener = []
Pres = []
N_water = []
count = 0

# find file in  directory that ends with ".txt" and sort in correct sequence (require correct address location)

for filename in os.listdir(''):
	if filename.endswith('.txt'):
		file_list.append(filename)
		new_list = Tcl().call('lsort', '-dict', file_list)

# read lines with required data from sorted towhee_output file 

for file in new_list:
	f = open(file).readlines()
	for line in f:
		if 'B:' in line:
			SOL_list.append(line)

# collect useful data and store in list

for line in SOL_list:
	s = line.split()
	# convert energy from K to kJ/mol
	e = float(s[3]) * 8.31446261815324 / 1000
	Ener.append(e)
	# convert P from kPa to bar
	p = float(s[5]) / 100
	Pres.append(p)
	# store number of water adsorbed
	n = int(s[6])
	N_water.append(n)

# create MC steps for each block printed out (varies depending on block size)

for line in enumerate(SOL_list):
	count += 10000

t = list((range(500000, count+500000, 500000)))

# Make list of accumulating average number of water molecules

df_list_water = DataFrame(N_water, columns = ['number of water'])
#df_acc_average = df_list_water.rolling(window = 10).mean()  # to calculate rolling average based on number of windows 
df_acc_average = df_list_water.expanding().mean()  # to calculate cumulative average from the first window
acc_average = df_acc_average['number of water'].values.tolist()


# write collected data into one file for futher analysis

for i, j, k, l, m in zip(t, Ener, Pres, N_water, acc_average):
 f99.write(str("%12d" % (i)) + str("%11.2E" % (j)) + str("%11.2E" % (k)) + str("%6d" % (l)) + str("%10.2f\n" % (m)))

f99.close()

print("      ")
print("******")
print("DONE!!")
print("******")
print("      ")

exit
