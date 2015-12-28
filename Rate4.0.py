import matplotlib.pyplot as plt
import numpy as np
import time

t0=time.time()

q,span=48000,83		# q: frequency span: duration in seconds, l: lenght in number of samples 
x,y=120,157		# x is the time of injection and y is the time of the begining of the fragment
o=(y-x)+10		# The standarization is put the injection at 10 seconds

peak_index=[]
peak_index.append((np.loadtxt('Analysis/AnalysisFiles/peak_index_03pos.txt')/q)+o)
peak_index=[x for y in peak_index for x in y]

plt.hist(peak_index,span,(0,140),histtype='stepfilled',alpha=0.3)
plt.xlabel('Seconds')
plt.ylabel('Peaks/Second')
'''
q,span=48000,31		# q: frequency span: duration in seconds, l: lenght in number of samples 

peak_index=[]
peak_index.append(np.loadtxt('Analysis/AnalysisFiles/peak_index_niconeg.txt')/q)
peak_index=[x for y in peak_index for x in y]

plt.hist(peak_index,span,(0,31),histtype='stepfilled',alpha=0.3)
plt.xlabel('Seconds')
plt.ylabel('Peaks/Second')
'''

print time.time()-t0

plt.show()






