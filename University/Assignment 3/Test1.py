import numpy as np


'''
def initialise_array(array):
    for i in range(0,array.shape[0]):
        for j in range(0,array.shape[1]):
            array[i][j]=False
'''
def move_particle(rnval,c):
    # Move left
    if(rnval==0):
        return c[0]-1,c[1]
    elif(rnval==1):
        return(c[0]+1,c[1])
    elif(rnval==2):
        return(c[0],c[1]-1)
    else:
        return(c[0],c[1]+1)



pos=np.ndarray(shape=2,dtype=int)

pos[0]=0
pos[1]=0


bounds=np.ndarray(shape=2,dtype=int)

bounds[0]=5
bounds[1]=5

for i in range(0,100):

    pos[0],pos[1]=move_particle(np.random.random_integers(0,3),pos)
    print("Current Position = ",pos[0],pos[1])