import random
import numpy as np
import matplotlib.pyplot as plt

#This is a test-case generator for training. 
def linList(b_0, b_1, var): #Points follow y* = mx* + b + e, e is norm(0, sqrt(var))
    xlist = []
    ylist = []    


    for i in range (0, 30):
        x = 10*random.random()
        error = np.random.normal(0, var) 
        y = b_1*x + b_0 + error
        xlist.append(x)
        ylist.append(y)
    plt.scatter(xlist,ylist, c = "red")
    print("Linlist generated successfully")
    return [xlist, ylist]

def lsrl_plot( xlist, ylist, var ):

    #Calculating mean of x-inputs
    x_bar = 0
    x_count = len(xlist)
    for i in range (0, len(xlist)):
        x_bar += xlist[i]
    x_bar = (1.0*x_bar)/x_count
    
    #calculating mean of y-inputs
    y_bar = 0
    y_count = len(ylist);
    for i in range (0, len(ylist)):
        y_bar += ylist[i]
    y_bar = (1.0*y_bar)/y_count

    #calculating b_1, x^1 coefficient
    n_sum = 0
    d_sum = 0
    r_denoma = 0
    r_denomb = 0
    for i in range (0, len(ylist)):
        n_sum += (ylist[i] - y_bar) * (xlist[i] - x_bar)
        d_sum += (xlist[i] - x_bar) * (xlist[i] - x_bar)
        r_denoma += (xlist[i] - x_bar)**2
        r_denomb += (ylist[i] - y_bar)**2
    b_1 = (1.0*n_sum)/(d_sum)
    
    #Standard Error of b_1, confidence interval 
    seb1square = var * (1/r_denoma)
    seb1 = seb1square ** 0.5
    seb1_lower = b_1 - 2*seb1
    seb1_upper = b_1 + 2*seb1

    #calculating b_0, constant
    b_0 = y_bar - b_1 * x_bar

    #Standard Error of b_0
    seb0square = var* (1/len(ylist) + x_bar**2/(r_denoma))
    seb0 = seb0square**0.5
    seb0_lower = b_0 - 2*seb0
    seb0_upper = b_0 + 2*seb0

    #Correlation Coefficient
    r = (1.0*n_sum)/((r_denoma**0.5)*(r_denomb**0.5))

    if (r**2 < 0.7 and r**2 > 0.4):
        print("Warning: there is not a strong linear correlation (r^2 = " + str(r**2) + ")")
    elif (r**2 <= 0.4):
        print("Warning: there is not a strong linear correlation (r^2 = " + str(r**2) + ")")
    else: 
        print("Strong correlation by r^2")
    
    if (0 >= seb1_lower and 0 <= seb1_upper and var != 0):
        print("Warning: there is a weak correlation with x (CI, B_1)")

    #Graph interface:
    x = np.linspace(0,12,100)
    y = b_1*x+b_0
    plt.plot(x, y, '-r', label='y=' + str(round(b_1, 3)) + '*x+' + str(round(b_0, 3)))
    plt.title('r = ' + str(round(r, 3)))
    plt.suptitle('Least Squares Regression')
    plt.xlabel('x', color='#1C2833')
    plt.ylabel('y', color='#1C2833')
    plt.legend(loc='upper left')
    print('b_0: [' + str(round(seb0_lower, 3)) + ', ' + str(round(seb0_upper, 3)) + ']')
    print('b_1: [' + str(round(seb1_lower, 3)) + ', ' + str(round(seb1_upper, 3)) + ']')
    plt.grid()
    plt.show()



training = linList(1, 3, 5) #Generate training set of form (b_0, b_1, error): y' = b_1 * x' + b_0 + e
lsrl_plot(training[0], training[1], 5) #Generate Least-Squares Regression Line (unknown variance = 0)




