
import numpy as np

import matplotlib.pyplot as plt

import yaml

from group_theory import active_modes
from surface_normal import plane_normal

import rotation_matrix
import xy_rotation


def polarised_rotation(hkl, zaxis, file_path=r"Raman-Tensors.yaml",
                       filepath=r"irreps.yaml", plot_title=None, theta=None,
                       cross=False):
    """Obtain the rotated tensors given an angle of rotation in the xy plane. 
    
    Otherwise, create an overlapping plot of the polar plots of all
    Raman-active vibrational modes to visualise the angle-dependence of
    Raman intensities.

    Arguments:
        hkl -- the Miller indices of the crystal surface, a 3 x 1 NumPy array.
        zaxis -- the experimental collection axis, a 3 x 1 NumPy array.
        file_path -- file path containing the Raman tensors.
        filepath -- file path containing information of the normal modes
        in dictionary format, including the Mulliken symbols and their
        band indices.
        plot_title -- optional title for the polar plots.
        theta -- the in-plane rotation angle in degrees.
        cross -- specifies a cross or parallel polarisation configuration,
        parallel configuration as default.
    """
    
    active_tensors = []
    bands = []
    
    with open(file_path, 'r') as r_tensors:
        tensors = yaml.load(r_tensors, Loader=yaml.CLoader)

        # get the active band indices and subsequently, active Raman tensors.
        
        active_bands = active_modes('raman', filepath)
        
        for activity in tensors['raman_activities']:  
            if activity['band_index'] in active_bands:
                active_tensors.append(activity['raman_tensor'])
                bands.append(activity['band_index'])

    # if an in-plane rotation has been given.

    if theta is not None:

        # find the normal to the crystal plane of interest and rotate it into
        # and around the z axis, apply the same to each Raman active tensor.
        
        normal = plane_normal(hkl)
        rot_matrix = rotation_matrix(normal, zaxis)
        
        rot_xy = xy_rotation(theta)
        rotation = rot_matrix @ rot_xy
        
        rotated_tensors = []        

        for tensor in active_tensors:
            temp = rotation * tensor * np.linalg.inv(rotation)
            rotated_tensors.append(temp)

        # save rotated tensors to a .dat file.

        theta_rad = np.pi * theta / 180
        h, k, l = hkl

        with open(f'Rotated_Raman_Tensors_[{h}{k}{l}]_'
                  f'{theta}deg.dat', 'w') as output_tensors:

            output_tensors.write(f"crystal_surface: [{h} {k} "
                                 f"{l}]\n")
            output_tensors.write(f"theta: {theta} degrees\n")
            output_tensors.write(f"theta: {theta_rad} radians\n")

            for band, tensor in zip(bands, rotated_tensors):
                output_tensors.write(f"\nband_index: {band}\n")
                output_tensors.write(f"raman_tensor:\n {tensor}\n")

        return rotated_tensors

    # if an in-plane rotation has not been given.

    elif theta is None:

        # generate the polar plot of intensity for each theta angle 0 - 2pi for
        # each Raman active tensor.
        
        theta = np.arange(0, 2 * np.pi, 0.01745)
        
        ei = np.array([0, 1, 0])
        es_para = np.array([0, 1, 0]).reshape(-1, 1)
        es_cross = np.array([1, 0, 0]).reshape(-1, 1)

        # find the rotation matrix into the z axis.

        normal = plane_normal(hkl)
        rot_matrix = rotation_matrix(normal, zaxis)
        
        # specify cross or parallel polarisation configuration.
        
        es = None
        
        if not cross:
            es = es_para
        
        else:
            es = es_cross
        
        # prepare a single figure for the plots of each tensor.
        
        fig, ax = plt.subplots(sharex=True, sharey=True,
                               subplot_kw={'projection': 'polar'})
        ax.set_rticks([])
        ax.set_title(plot_title, loc='center', va='bottom')
        ax.grid(True)
        
        for tensor in active_tensors:
            
            intensity = []
            
            for angle in theta:

                # find the rotation matrix into the z axis and calculate the
                # intensity.

                rot_xy = xy_rotation(angle)
                rotation = rot_matrix @ rot_xy
                
                temp = np.square(np.linalg.norm(ei * rotation * tensor *
                                                np.linalg.inv(rotation) * es)
                                 )

                intensity.append(temp)
            
            # get the irrep label of the mode and add it to the legend.
            
            irrep_label = None
            bandindex = None
            
            with open(file_path, 'r') as r_tensors:
                tensors = yaml.load(r_tensors, Loader=yaml.CLoader)
                
                for activity in tensors['raman_activities']:
                    if tensor == activity['raman_tensor']:
                        bandindex = activity['band_index']

            with open(filepath, 'r') as modes:
                irreps = yaml.load(modes, Loader=yaml.CLoader)
                
                for mode in irreps['normal_modes']:
                    if bandindex in mode['band_indices']:
                        irrep_label = mode['ir_label']
            
            ax.plot(theta, intensity, label=irrep_label)
        
        # set the legend location.
        
        angle = np.deg2rad(0)
        ax.legend(loc="center left", bbox_to_anchor=(.6 + np.cos(angle)/2,
                                                     .6 + np.sin(angle)/2))
        
        return plt.show()
    
    else:
        pass
