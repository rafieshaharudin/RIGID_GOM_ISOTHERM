from pandas import DataFrame

f1 = open('pres_ZZ.xvg').readlines()[24:]
f99 = open('presZZ.txt', 'w')

pZ = []
time = []

for line in f1:
        s = line.split()
        pZ.append(s[1])
        time.append(s[0])

df_pressure_Z = DataFrame(pZ, columns = ['pressure in Z'])
#df_acc_average = df_pressure_Z.rolling(window = 10).mean()  # to calculate rolling average based on number of windows
df_acc_average = df_pressure_Z.expanding().mean()  # to calculate cumulative average from the first window
acc_average = df_acc_average['pressure in Z'].values.tolist()


f99.write('# time (ps)	pressure (bar)	rolling_average (bar)\n')
for i, j, k, in zip(time, pZ, acc_average):
 f99.write(str("%8.2f" % (float(i))) + str("%18.2E" % (float(j))) + str("%18.2E\n" % (float(k))))

f99.close()

exit
