# -*- coding: utf-8 -*-

'''
This program is showing how does a quadratic function look like on the graph
or canvas.

What is a quadratic function?
    A quadratic function is a mathematical function that shows squared values of
    any number x:

        f(x) = (a * b + c) * x^2


    The function above, is an example of a quadratic function.


    The thing that characterizes this function, is that one of the values are squared,
    like in this example, x is squared and thats why its called a quadratic function
'''


#========================================================================================
# IMPORTS:
#========================================================================================

from matplotlib import pyplot as plt



#========================================================================================
# FUNCTIONS:
#========================================================================================

def function(a, b, c):

    # creating a linear equation and returinig the value of it:
    e = a*b + c

    return e


def loop(func, ls):

    # setting up an empty list:
    ls_y = []

    # appending the linear equation and multiplying it by x^2:
    for x in ls:
        a = func*x**2

        # appending hte values of ls_y list:
        ls_y.append(a)

    return ls_y



#========================================================================================
# MAIN:
#========================================================================================

# creating a list which has the values of x:
ls_x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


# generating the values for the linear quadratic function:
func = function(2, 3, 1)


# generating values of quadratic functions and adding them to a list:
ls_y = loop(func, ls_x)


# displaying the graph canvas:
plt.plot(ls_y, marker='o')


# displaying the grid on the canvas:
plt.grid(True)


# showing the graph:
plt.show()
