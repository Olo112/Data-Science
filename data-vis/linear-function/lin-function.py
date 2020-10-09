# -*- coding: utf-8 -*-

'''
description:
    This program is showing how does a linear function look like on the graph
    (or canvas).

    What is a linear function?
        A linear function is a mathematical function that shows values of
        any number a and/or b:

            f(x) = a*x + b


        But as we get the second number which in this case is going to be y, where
        y is the value of the function:

            y = f(x) = a*x + b


        The function above, is an example of a linear function.


        The thing that characterizes this function, is that one of the values are squared,
        like in this example, x is one of the coordinates and the second coordinate is y. Its called
        a linear function because the equation is in the power of one ( equation^2 ).
'''



#======================================================================
#   IMPORTS:
#======================================================================

from matplotlib import pyplot as plt



#======================================================================
#   FUNCTIONS:
#======================================================================




#======================================================================
#   FUNCTIONS:
#======================================================================

# function that creates list of y values:
def function(a, b, ls_x):

    # creating an empty list:
    ls_y = []

    # looping through the ls_x list which is given as an arguemnt:
    for x in ls_x:

        # creating the linear equation:
        e = (a*x) + b

        # appending the value of the equation to ls_y:
        ls_y.append(e)

    # returning te values of ls_y list:
    return ls_y



#======================================================================
#   MAIN:
#======================================================================

# creating a list with values of x:
ls_x = [0, 1, 2]


# generating a list with values of y and assigning it to the quad_vals variable:
quad_vals = function(2, 1, ls_x)


# checking of the list is right:
print('quad_vals =', quad_vals)


# ploting  the values of quad_vals list:
plt.plot(quad_vals)


# showing the grid on the plot:
plt.grid(True)


# showing the plot:
plt.show()



#======================================================================
#   END OF FILE
#======================================================================
