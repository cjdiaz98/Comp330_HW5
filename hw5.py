import heapq as hq
import numpy as np
import time

# NOTE: Chris' Output'
# (21.240308803962975, 3002)
# (22.400311356557985, 3001)
# (25.074870468424841, 3005)
# (24.30004896822501, 3003)
# (23.902326257409541, 3004)

###################3
## TASK 1 ##

def task1():
    #create the covariance matrix
    covar = np.zeros ((100,100))
    np.fill_diagonal (covar, 1)

    #and the mean vector
    mean = np.zeros (100)

    #create 3000 data points
    all_data = np.random.multivariate_normal (mean, covar, 3000)

    #now create the 20 outliers
    for i in range (1, 20):
      mean.fill (i)
      outlier_data = np.random.multivariate_normal (mean, covar, i)
      all_data = np.concatenate ((all_data, outlier_data))

    #k for kNN detection
    k = 10

    #the number of outliers to return
    m = 5

    #start the timer
    start_time = time.time()

    #the priority queue of outliers
    outliers = []

    #YOUR CODE HERE!

    # Compute data point distance with Euclidean distance (L2 norm)

    print("--- %s seconds ---" % (time.time() - start_time))

    #print the outliers...
    for outlier in outliers:
      print (outlier)



#########################
##  TASK 2 ##
# Chris' Output:
# (21.240308803962975, 2085)
# (22.400311356557985, 198)
# (24.30004896822501, 3162)
# (25.074870468424841, 51)
# (23.902326257409541, 50)'

def task2():
    global all_data
    np.random.shuffle(all_data)

    