import matplotlib.pyplot as plt


values = [27,30,33 ,36,39,42,45,48,50,53,56,58,61,64,66,68,71,73,75,78,]
plt.plot(values, marker='+',label='April 26-2020')
oven_temps = [30, 56,82 ,106,120]
plt.plot(oven_temps, label='preheat',marker='1')

beef_internal_temps = [48, 51, 54, 56, 57, 58, 58, 58, 58, 58, 58,58,58,58,59,\
	59,60,61,61,62,62,63, 64, 64, 65, 65,66,66,67,67, 68, 68, 69, 69, 70, 70,\
	70, 71, 71, 72, 72, 72,72,73,73,73,73,73,73,73, 73,73, 73, 73, 73, 73]

plt.axvline(35, label='oven off')
print(f'Total cooking time is {len(beef_internal_temps)} minutes')
plt.plot(beef_internal_temps, label='beef cooking', marker='x')

plt.hlines(120, len(oven_temps)-1, len(oven_temps)+len(beef_internal_temps), color='orange')
plt.axhline(71, label='medium')
plt.axhline(62, label='medium rare', color='r')
plt.title('Beef for dinner yyyyyummmy in de tummy  :)')
plt.ylabel('Temerature/deg c')
plt.xlabel('minutes')
plt.legend()
plt.show()





