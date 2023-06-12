
import numpy as np


def rotation_matrix(a, b):
    """ Define a rotation matrix 'R', that rotates a numpy array 3D vector
    'a' onto another numpy array 3D vector 'b'.

    Arguments:
        a -- the 3D vector to be rotated, a 3 x 1 NumPy array.
        b -- the 3D vector 'a' is being rotated into, a 3 x 1 NumPy array.
    """

    # obtain the axis of rotation normal to the ab plane and the angle of
    # rotation, phi.

    a = np.array(a, dtype=np.float64) / np.linalg.norm(a)
    b = np.array(b, dtype=np.float64) / np.linalg.norm(b)
    x = np.cross(a, b)

    cos_phi = np.dot(a, b)
    sin_phi = np.linalg.norm(x)
    
    # obtain the skew-symmetric cross product matrix and find the rotation
    # matrix using Rodrigues' formula.

    k = np.matrix([[0, -x[2], x[1]],
                   [x[2], 0, -x[0]],
                   [-x[1], x[0], 0]],
                  dtype=np.float64
                  )

    size = len(a)
    i = np.identity(size)
    
    # check if the vectors are parallel or orthogonal to each other.
    
    minimum = 1.0e-10
    
    if np.abs(cos_phi - 1.0) < minimum:
        r = i
    elif np.abs(cos_phi + 1.0) < minimum:
        r = -i
    else:
        r = i + (k * sin_phi) + ((k @ k) * (1 - cos_phi))
    
    return r
