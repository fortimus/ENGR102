def gate_and(input1, input2):
    """ an AND gate (input1 ^ input2) """
    gate1 = input1 and input2
    return bool(gate1)
                
# Homework 3: Z-Score Python Script (Group Homework)
	
#################
#  SAMPLE DATA  #
#################

# First data set: a list of positive integers (not a normal distribution)
population1 = [14, 28, 96, 97, 21, 29, 29, 4, 58, 
               42, 25, 97, 49, 33, 75, 53, 14, 53, 
               45, 87, 75, 66, 62, 55, 57, 44, 44, 
               94, 19, 96, 12, 59, 86, 88, 61, 68, 
               37, 64, 19, 46, 68, 98, 19, 54, 65, 
               30, 1, 82, 76, 3]
	
# Second data set: a list of negative and positive integers (normal distribution)
population2 = [-16, 10, -15, -6, -5, -20, -11, 9, -9,
               -7, 5, -14, 6, -10, -22, -19, 21, 11, 
               -18, -13, -24, -21, 14, 19, 20, 13, 16, 
               8, 4, 3, 18, 22, 17, 7, -12, -3, 
               23, -8, 2, -2, -4, 1, 12, -25, -1,
               15, 0, -23, -17, 24]
	
# Third data set: a list of positive integers (normal distribution)
population3 = [125, 475, 275, 550, 350, 325, 575, 
               25, 225, 150, 425, 75, 175, 650, 
               600, 625, 675, 250, 100, 0, 375, 
               500, 400, 450, 300, 525, 50, 200]

#################
#  FUNCTIONS    #
#################

def mean(data_set):
    """
    This function will return the mean of the data_set(population)
    **Do not change this function**
    """
    return sum(data_set)/len(data_set)

def stdev(data_set, avg):
    """
    This function will return the standard deviation of the data_set(population), given the mean of the data_set (avg)
    **Do not change this function**
    """
    variance = sum([(integer - avg) ** 2 for integer in data_set])/len(data_set)
    # return the square root of the variance calculation 
    return variance ** .5
	
def least(data_set):
    """
    Returns the least value in the data_set(population)
    **Do not change this function**
    """
    return min(data_set)
	
def greatest(data_set):
    """
    Returns the greatest value in the data_set(population)
    **Do not change this function**
    """
    return max(data_set)
	# Your grader will use this function to help them verify your code

def test_z_score_function():
    pop1_avg = mean(population1)
    pop1_sd = stdev(population1, pop1_avg)
    
    mean_z_score_p1 = z_score(pop1_avg, pop1_avg, pop1_sd)
    
    pop2_greatest = greatest(population2)
    pop2_avg = mean(population2)
    pop2_sd = stdev(population2, pop2_avg)
    
    greatest_z_score_p2 = z_score(pop2_greatest, pop2_avg, pop2_sd)
    
    print("The z-score of the mean of population1 is", mean_z_score_p1)
    print("The z-score of the greatest value of population2 is", greatest_z_score_p2)
  
#######################################################
# YOUR CODE GOES BELOW THIS BOX.                      #
#                                                     #
# Complete the following z_score function.            #
# You may call the functions above,	                  #
#   but do not define any others (except for testing) #
# You may use arithmetic operators                    #
#  (i.e., +, -, *, **, /) but not Python Boolean      #
#  (call the provided functions instead)              #
#                                                     #
# Be sure to include names of the group members that  #
# participated in the group assignment work           #
#######################################################

def z_score(x, mu, sigma):
    """
    x is the population item
    mu is the population mean
    sigma is the population standard deviation
    
    Returns the z-score of x
    """
    
    # Participating group member names go in this comment
    # Saxon Payne, Michael Fort, Joshua Titchener
    
    # Your code goes between this comment and the return
    
    # Based on function description and inputs, assume that x, mu, sigma are single values and that mean and std deviation are already calculated
    score = (x-mu)/sigma

    return score



#Automated testing

population4 = {-78,-90,-21,-9,-98,-70,-84,-99,-5,-43,-14,
    -95,-89,-18,-95,-71,-66,-97,-38,-9,-5,-6,-19,-88,-75,
    -40,-79,-16,-37,-96,-10,-4,-79,-79,-50,-75,-87,-45,-6,
    -11,-77,-34,-25,-48,-51,-78,-85,-58,-91,-54,}

population5 = {6,-43,-31,44,30,42,-10,-27,-32,16,-27,8,-20,
    36,-27,47,30,9,32,20,}


test_populations = [population1,population2,population3,population4,population5]

def unit_test_z_score(test_populations):
    
    loop = 1

    for population in test_populations:
        average = mean(population)
        deviation = stdev(population,average)

        print("Population ",loop)
        print("Average: ",average)
        print("StdDev: ",deviation)

        print("z-Scores:")
        print("Sample: z-Score")
        for sample in population:
            print(sample,": ",z_score(sample,average,deviation))
        
        loop = loop + 1
        print()
        print()


unit_test_z_score(test_populations)
