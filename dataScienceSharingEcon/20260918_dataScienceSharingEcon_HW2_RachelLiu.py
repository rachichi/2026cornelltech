# Prompt from HW2: Consider the two-server queueing system that you considered in the previous homework assignment. The customers arriving into the system join a single queue, wait for their turn, receive service from either one of the two servers and leave the system. The first server is faster than the second one. If an arriving customer finds both servers available, then it uses the first server. Otherwise, it simply uses whichever server is available. We are interested in simulating the behavior of this system with the intention of estimating
# • proportion of time that the first server is busy;
# • proportion of time both servers are busy; and
# • average amount of time that a customer spends in the system over the first 100 minutes.
# The interarrival times for the customers are exponentially distributed with mean 0.5 minutes. The service times at the first server are exponentially distributed with mean 0.8 minutes and the service times at the second server are exponentially distributed with mean 0.9 minutes. We assume that the queue can accommodate infinite number of customers and the system starts empty. Write a computer program that simulates the two-server queueing system with the probability distributions given above. Turn in your (commented) computer program. Make sure that your computer program computes the statistics of interest. Run your computer program and report the statistics of interest. You may want to check the posted solution of the previous homework to see how one could define the state variable and events in a two-server queueing system. It is perfectly fine if you fully follow the pseudo-code given in the solutions of the previous homework assignment queue.

def interArrTime():
    return t + IA

def s1Time():
    return

def s2Time():
    return


n = -1
def arrEvent():
    n++
    return

def dep1Event():
    return

def dep2Event():
    return