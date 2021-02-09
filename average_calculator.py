#Aim: To calculate desired properties from output file

# load numpy in anaconda

import numpy as np

# define desired variables

pressure = np.loadtxt(fname='presZZ.txt',usecols = 1, skiprows = 800)
n_water = np.loadtxt(fname='SRC_MC.txt',usecols = 3, skiprows = 800) # WARNING : need to recheck number of skips !!
# calculate and print desired stats

print(' ')
print(' ')
print(' ')
print(' ')
print(' ##################################### ')
print(' pressure_last200 =','%5.2f' % np.average(pressure),'bar')
print(' std_dev_P =','%5.2f' % np.std(pressure),'bar')
print(' N_water =','%5.2f' % np.average(n_water),'molecules')
print(' std_dev_N =','%5.2f' % np.std(n_water),'molecules')
print(' ##################################### ')
print(' ')
print(' ')
print(' ')
print(' ')

exit
