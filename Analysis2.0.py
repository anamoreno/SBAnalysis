import matplotlib.pyplot as plt
import numpy as np
import time
t0=time.time()
								# Read audio samples
l=['SBAnalysis/FR/03-1.txt','SBAnalysis/FR/03-2.txt','SBAnalysis/FR/03-3.txt','SBAnalysis/FR/03-4.txt']	#Change txt file names (reading and writting)
#l=['FR/03-1.txt','FR/03-2.txt']
audio=[]
for x in l:
    audio.append(np.loadtxt(x))
audio=[x for y in audio for x in y]
desvest=np.around(np.std(audio),decimals=2)
l=len(audio)
								    # Haunt spikes
d,h=6*desvest,5*desvest						# Signals above d value are considered as depolarizations and bellow h as hyperpolarizations.         
det=[]								# The SNR for the SpikerBox is 4. (Timothy C. Marzullo, Gregory J. Gage [2])
for x in range (l):						# Find out the number of possitive maximum over the threshold
  if (audio[x]<-d) and (audio[x-1]>audio[x]<audio[x+1]):
    det.append(np.hstack((x,audio[x:x+25])))     		# 15 for 48.0 KHz
peak_index, peak_value=[],[]
for x in det:
  for y in x:
    if (y>h):
      peak_index.append(x[0])
      peak_value.append(x[1])
      break 
								    #Save data
f = open('SBAnalysis/AnalysisFiles/peak_index_03pos.txt','a')
for x in peak_index:
  f.write('%s \n' % x)
f.close()
f = open('SBAnalysis/AnalysisFiles/peak_value_03pos.txt','a')
for x in peak_value:
  f.write('%s \n' % x)
f.close()
print time.time()-t0
								  # Bibliography
# [1] http://docs.scipy.org/doc/numpy/reference/
# [2] http://www.plosone.org/article/info%3Adoi%2F10.1371%2Fjournal.pone.0030837
# [3] http://www.mcb80x.org/
# [4] http://www.funjournal.org/downloads/Ramos_Supplemental_Material.pdf
