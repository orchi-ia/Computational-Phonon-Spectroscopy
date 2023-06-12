
import numpy as np

import os


def plane_normal(hkl, filepath=r"POSCAR.vasp"):
    """
    Obtain the vector normal of a crystal surface, defined by (hkl) Miller
    indices, in real space using reciprocal space lattice vectors.
    
    Arguments:
        hkl -- the Miller indices of the crystal surface, a 3 x 1 NumPy array.
        filepath -- the crystal POSCAR file, must contain lattice vectors
        convertible to a 3 x 3 NumPy matrix.
    """
    
    # define lattice vectors and Miller indices.
    
    poscar = np.loadtxt(os.path.expanduser(filepath), skiprows=2, max_rows=3)

    a1, a2, a3 = poscar
    h, k, l = hkl
    
    # generate the reciprocal lattice vector.

    v = np.dot(a1, (np.cross(a2, a3)))

    b1 = np.cross(a2, a3) / v
    b2 = np.cross(a3, a1) / v
    b3 = np.cross(a1, a2) / v

    g = (h * b1) + (k * b2) + (l * b3)
    
    # convert reciprocal lattice vector into real space.
    # obtain the normal to the hkl plane and its relative primitive components.
    
    recip_metric = np.array([[np.dot(b1, b1), np.dot(b1, b2), np.dot(b1, b3)],
                             [np.dot(b2, b1), np.dot(b2, b2), np.dot(b2, b3)],
                             [np.dot(b3, b1), np.dot(b3, b2), np.dot(b3, b3)]]
                            )

    n1, n2, n3 = np.dot(recip_metric, hkl)

    temp = (n1 * a1) + (n2 * a2) + (n3 * a3)
    normal = temp / np.linalg.norm(temp)
    
    return normal
