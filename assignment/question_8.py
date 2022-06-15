#question 8

import numpy as np
import matplotlib.pyplot as plt 

dim = 2  
#dim =10         # The number of dimensions
n = int(1e5)       # The number of Monte Carlo trials
Zn = 0
for i in range(n):
    '''    
    x1 = np.random.uniform()
    x2 = np.random.uniform()
    R = np.sqrt(x1**2 + x2**2)'''  #for 2-D
    
    x = np.random.uniform( 0, 1, dim )    # volume of a 9-D sphere: x1^2+x2^2+x3^2+x4^2+x5^2+x6^2+x7^2+x8^2+x9^2 < R^2
    sq_R = 0
    for j in range(dim):
       sq_R = sq_R + x[j]**2      # random values for x1, x2, x3, ..., x8
    dR = np.sqrt(sq_R)            # Calculate distance from the orgin
    if dR <= 1:        
        Zn += 1 
Vol = 2** dim *Zn/n    #dim = 2 and dim = 10               # calculation of the sphere volume
 
print('The volume of a', dim, 'D sphere from the Monte Carlo simulation is', Vol )

