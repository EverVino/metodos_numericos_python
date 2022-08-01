import numpy as np

def edo_reactores(C):
    ## Definimos constantes
    tau = 5
    k = 0.12
    ca0 = 20
    
    dC = np.zeros(len(C))

    dC[0] = 1/tau*(ca0-C[0])-k*C[0]
    dC[1] = -1/tau*C[1]+k*C[0]
    dC[2] = 1/tau*(C[0]-C[2])-k*C[1]
    dC[3] = 1/tau*(C[1]-C[3])+k*C[1]

    return dC 
