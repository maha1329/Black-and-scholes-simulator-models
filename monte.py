import numpy as np
import matplotlib.pyplot as plt
def monte_carlo():
  np.random.seed(25)
  rets=np.random.randn(100000,5)*0.04/np.sqrt(5)
  rets.shape
  traces=np.cumprod(1+rets,1)*100
  for i in traces[:100,:]:
      plt.plot(i)
  plt.grid()
  plt.title('Le cone des prix avec 100000 fois de simulation de monte carlo')
  plt.xlabel('days',fontsize=12)
  plt.ylabel('valeur sous jacent',fontsize=12)
  plt.savefig('myplot.png')


