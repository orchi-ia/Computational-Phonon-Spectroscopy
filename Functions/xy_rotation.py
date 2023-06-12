
import numpy as np


def xy_rotation(theta):
    """ Obtain the matrix that rotates in the xy plane with an angle of theta.

    Arguments:
        theta -- the angle of rotation.
    """
    
    # define angles and return the rotation matrix around the z axis.
    
    cos_theta = np.cos(theta)
    sin_theta = np.sin(theta)
    
    r_xy = np.matrix([[cos_theta, -sin_theta, 0],
                     [sin_theta, cos_theta, 0],
                     [0, 0, 1]]
                     )
    
    return r_xy
