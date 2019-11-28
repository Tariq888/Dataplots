import matplotlib.pyplot as plt, numpy as np

gdp_lab = [ 1000*2, 2000*3, 3000*4, 4000*5]

life_exp = [ 100*2300, 200*30, 400*23, 500*29]
np_pop = [ 100, 200, 300 ,1000]

np_pop = np_pop * 2 
plt.scatter(gdp_lab, life_exp, s = np_pop)
plt.xscale('log')
xlab = " Sample its X,axis"
ylab = " Sample its Y,axis"
title = 'Show information'
tick_vul = [1000, 10000, 100000]
tick_lab = [ '1k' , '10k', '100k']
plt.text = (1550, 112 ,'PAKISTAN')
plt.text = (1292,12, 'Turkey')

plt.xticks(tick_vul, tick_lab)

plt.xlabel(ylab)
plt.ylabel(xlab)
plt.title(title)
plt.grid()
plt.show()
