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


def euclidean_dist(x1,x2):
    """
    
    :param x1: 
    :param x2: 
    :return:  Euclidean distance between the two
    """
    diff = np.subtract(x1,x2)
    sqr = np.square(diff)
    return sqr.sum()


def task1():
    #create the covariance matrix
    covar = np.zeros ((100,100))
    np.fill_diagonal (covar, 1)

    #and the mean vector
    mean = np.zeros (100)

    #create 3000 data points
    # all_data = np.random.multivariate_normal (mean, covar, 3000)
    # TODO: COMMENT BELOW OUT WHEN NOT DEBUGGING!
    all_data = np.random.multivariate_normal (mean, covar, 100)

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

    #the priority queue of outliers. Stores tuples: (a,b)
    # where a is the weight, and b is the element
    outliers = []
    all_data_mut = all_data.copy()
    #YOUR CODE HERE!
    for i1 in range(len(all_data)):
        x = all_data_mut[i1]
        max_heap = []
        # stores single numerical elements
        # note: invert the value of all elements popped into this heap to maintain a max-heap
        not_outlier = False
        for i2 in range(len(all_data_mut)):
            x2 = all_data_mut[i2]
            if np.array_equal(x, x2):
                continue
            dist = euclidean_dist(x, x2)
            hq.heappush(max_heap, dist)
            max_heap_size = len(max_heap)
            o_size = len(outliers)
            if max_heap_size> k:
                # remove max
                max_elem = hq.heappop(max_heap)
            if max_heap_size == k and o_size == m and \
                            hq.nlargest(1,max_heap) < hq.nsmallest(1, max_heap):
                # discard x1 because not an outlier
                not_outlier = True
                break
        if not not_outlier:
            # we don't want to discard
            elem = (hq.heappop(max_heap), i1)
            hq.heappush(outliers, elem)
        else:
            all_data_mut.pop(i1)
        if len(outliers) > m:
            # pop from outliers
            hq.heappop(outliers)


    # Compute data point distance with Euclidean distance (L2 norm)
    print("--- %s seconds ---" % (time.time() - start_time))
    print("Length outliers: %d " % len(outliers))
    #print the outliers...
    for outlier in outliers:
      print (outlier)

    return outliers


task1()

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

