print("\n\n ----ESERCIZIO 4-----")
#per diagonalizzare una matrice si utilizza il sottomodulo linalg di numpy con  
import numpy as np
autovalori,autovettori=np.linalg.eig(M) #calcola entrambi contemporaneamente 
autoval=np.linalg.eigvals(M) #calcola solo gli autovalori