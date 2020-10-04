# ================================================================
#   FUNCTIONS:
# ================================================================


def sin_val():

    # list of sine values (more info in src/main-source.txt)
    ls_sin = [0.0, 0.08, 0.18, 0.27, 0.35, 0.44, 0.5, 0.58, 0.66, 0.71, 0.77, 0.81, 0.86, 0.90, 0.93, 0.96, 0.98, 0.99, 1.0,
             0.99, 0.98, 0.96, 0.93, 0.90, 0.86, 0.81, 0.77, 0.71, 0.66, 0.58, 0.5, 0.44, 0.35, 0.27, 0.18, 0.08, 0.0,
             -0.08, -0.18, -0.27, -0.35, -0.44, -0.5, -0.58, -0.66, -0.71, -0.77, -0.81, -0.86, -0.90, -0.93, -0.96, -0.98, -0.99, -1.0,
             -0.99, -0.98, -0.96, -0.93, -0.90, -0.86, -0.81, -0.77, -0.71, -0.66, -0.58, -0.5, -0.44, -0.35, -0.27, -0.18, -0.08, -0.0]

    # returns a list of sine values
    return ls_sin


def angle(ls):

    # noting the main variables used for defining the angles
    a = 0
    b = 5

    # list of angle values which is starting from a 0 degree angle
    ls_ang = [0]

    # defining the lenth of ls_sin list
    N = len(ls)

    # loop that adds the definied variables and adds them to the angel list
    for i in range(1, N):
        a = a+b
        ls_ang.append(a)

    # returns the list of angles (for every fifth angle) 
    return ls_ang
