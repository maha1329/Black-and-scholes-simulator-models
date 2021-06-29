import numpy as np
import matplotlib.pyplot as plt
np.random.seed(25)
rets=np.random.randn(100000,5)*0.04/np.sqrt(5)
rets.shape
traces=np.cumprod(1+rets,1)*100
plt.hist(traces[:,1],bins=40)
plt.title('Distribution des prix finaux')
plt.xlabel('les prix finaux')
plt.ylabel('comptes')
plt.savefig('hist.png')
