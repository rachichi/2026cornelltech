import matplotlib.pyplot as plt
import numpy as np

#Problem 2 - Counting, 33 points
## (a) - 15 points
def C(N, m):
    # base cases
    if N == 0:
        return 1                            # if N has reached 0, then this is valid
    if len(m) == 0:
        return 0                            # if m is empty then we have run out of denominations
    if N < 0:
        return 0                            # if N is negative then we have overshot the target
    
    # setup
    num_coins = len(m)                      # get the length of m
    largest = m[num_coins - 1]              # get the largest denomination

    # recursive cases
    without_Sm = C(N, m[0 : num_coins-1])   # do the withouts first (exclude largest denomination entirely but not change target N unchanged). this will run until base case is reached.
    with_Sm    = C(N - largest, m)          # use one coin of the largest denomination, still allowed to use it again, so m unchanged

    return without_Sm + with_Sm

#test cases 
print (C(10, [1,5,10])) 
# 1. C(10,[1,5,10])
#   -> without_Sm[1] = C(10, [1,5]) = without_Sm[2] + with_Sm[2] = 3
#   2. C(10, [1,5])
#       -> without_Sm[2] = C(10, [1]) = without_Sm[3] + with_Sm[3] = 1
#       3. C(10, [1])
#           -> without_Sm[3] = C(10, []) = 0
#           -> with_Sm[3] = C(9, [1]) = ... = 1
#       -> with_Sm[2] = (5, [1,5]) = without_Sm[4] + with_Sm[4] = 2
#       4. (5, [1,5])
#           -> without_Sm[4] = (5,[1]) = ... = 1
#           -> with_Sm[4] = (0, [1,5]) = 1   
#   -> with_Sm[1] = C(0, [1,5,10]) = 1 
# Final Output = without_Sm[1] + with_Sm[1] = 4

print (C(2, [1, 2]))
# 1. C(2, [1,2]).
#   -> without_Sm[1] = C(2, [1]) =  without_Sm[2] + with_Sm[2] = 1
#   2. C(2,[1]).
#       -> without_Sm[2] = C(2, []) = 0
#       -> with_Sm[2] = C(1, [1]) = without_Sm[3] + with_Sm[3] = 1
#       3. C[1, [1]]
#           -> without_Sm[3] = C[1, []] = 0
#           -> with_Sm[3] = C[0, [1]] = 1
#   -> with_Sm[1]: Call C(0, [1, 2]) = 1
# Final Output = without_Sm[1] + with_Sm[1] = 2

## (b) - 5 points
print(C(213, [1,5,10,25]))
### 1670 ways 

## (c) - 5 points
###create wrapper function that only calls it once
def C_firstround(N, m):
    num_coins = len(m)
    largest = m[num_coins - 1]
    without_Sm = C(N, m[0 : num_coins-1])
    with_Sm    = C(N - largest, m)
    return without_Sm, with_Sm, without_Sm / (without_Sm + with_Sm)

print(C_firstround(213, [1,5,10,25]))
#   -> without_Sm = C(213, [1,5,10]) = 484
#   -> with_Sm = C(213, [1,5,10,25]) = 1186
# 0.2898203592814371

## (d) -
x_val = list()
y_val = list()
for i in range (25, 500, 3):
    x_val.append(i)
    y_val.append(C_firstround(i,[1,5,10,25])[2])

# print (x_val)
# print(y_val)

plt.scatter(x_val, y_val)
plt.xlabel("N")
plt.ylabel("Fraction of Counts Using Only [1,5,10]")
plt.show()