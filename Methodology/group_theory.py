
import yaml


def active_modes(spectrumtype, filepath=r"irreps.yaml"):
    """ Return the band indices for IR or Raman active vibrational modes
    using group theory principles.

    Arguments:
        spectrumtype -- the type of spectrum desired, allowed values:
            'ir', 'raman'.
        filepath -- file path containing information of the normal modes in
        dictionary format, including the crystal point group and band indices.
    """
    
    # generate a dictionary of IR and Raman active IRREPs.
    
    point_groups = {
        # Point group C_1.
        '1': {},
        # Point group C_i.
        '-1': {'IR': ["Au"],
               'Raman': ["Ag"]
               },
        # Point group C_2.
        '2': {'IR': ["A", "B"],
              'Raman': ["A", "B"]
              },
        # Point group C_s.
        'm': {'IR': ["A'", "A''"],
              'Raman': ["A'", "A''"]
              },
        # Point group C_2h.
        '2/m': {'IR': ["Au", "Bu"],
                'Raman': ["Ag", "Bg"]
                },
        # Point group D_2.
        '222': {'IR': ["B1", "B2", "B3"],
                'Raman': ["A", "B1", "B2", "B3"]
                },
        # Point group C_2v.
        'mm2': {'IR': ["A1", "B1", "B2"],
                'Raman': ["A1", "A2", "B1", "B2"]
                },
        # Point group D_2h.
        'mmm': {'IR': ["B1u", "B2u", "B3u"],
                'Raman': ["Ag", "B1g", "B2g", "B3g"]
                },

        # Point group C_4.
        '4': {'IR': ["A", "1E", "2E"],
              'Raman': ["A", "B", "1E", "2E"]
              },
        # Point group S_4.
        '-4': {'IR': ["B", "1E", "2E"],
               'Raman': ["A", "B", "1E", "2E"]
               },
        # Point group C_4h.
        '4/m': {'IR': ["Au", "1Eu", "2Eu"],
                'Raman': ["Ag", "Bg", "1Eg", "2Eg"]
                },
        # Point group D_4.
        '422': {'IR': ["A2", "E"],
                'Raman': ["A1", "B1", "B2", "E"]
                },
        # Point group C_4v.
        '4mm': {'IR': ["A1", "E"],
                'Raman': ["A1", "B1", "B2", "E"]
                },
        # Point group D_2d.
        '-42m': {'IR': ["B2", "E"],
                 'Raman': ["A1", "B1", "B2", "E"]
                 },
        # Point group D_4h.
        '4/mmm': {'IR': ["A2u", "E"],
                  'Raman': ["A1g", "B1g", "B2g", "Eg"]
                  },
        # Point group C_3.
        '3': {'IR': ["A", "1E", "2E"],
              'Raman': ["A", "1E", "2E"]
              },

        # Point group C_3i.
        '-3': {'IR': ["Au", "1Eu", "2Eu"],
               'Raman': ["Ag", "1Eg", "2Eg"]
               },
        # Point group D_3.
        '32': {'IR': ["A2", "E"],
               'Raman': ["A1", "E"]
               },
        # Point group C_3v.
        '3m': {'IR': ["A1", "E"],
               'Raman': ["A1", "E"]
               },
        # Point group D_3d.
        '-3m': {'IR': ["A2u", "Eu"],
                'Raman': ["A1g", "Eg"]
                },
        # Point group C_6.
        '6': {'IR': ["A", "2E1", "1E1"],
              'Raman': ["A", "1E2", "2E2", "2E1", "1E1"]
              },
        # Point group C_3h.
        '-6': {'IR': ["A''", "2E'", "1E'"],
               'Raman': ["A'", "2E'", "1E'", "2E''", "1E''"]
               },
        # Point group C_6h.
        '6/m': {'IR': ["Au", "2E1u", "1E1u"],
                'Raman': ["Ag", "1E2g", "2E2g", "2E1g", "1E1g"]
                },
        # Point group D_6.
        '622': {'IR': ["A2", "E1"],
                'Raman': ["A1", "E2", "E1"]
                },

        # Point group C_6v.
        '6mm': {'IR': ["A1", "E1"],
                'Raman': ["A1", "E2", "E1"]
                },
        # Point group D_3h.
        '-6m2': {'IR': ["A''2", "E'"],
                 'Raman': ["A'1", "E'", "E''"]
                 },
        # Point group D_6h.
        '6/mmm': {'IR': ["A2u", "E1u"],
                  'Raman': ["A1g", "E2g", "E1g"]
                  },
        # Point group T.
        '23':  {'IR': ["T"],
                'Raman': ["A", "1E", "2E", "T"]
                },
        # Point group T_h.
        'm-3': {'IR': ["Tu"],
                'Raman': ["Ag", "1Eg", "2Eg", "Tg"]
                },
        # Point group O.
        '432': {'IR': ["T1"],
                'Raman': ["A1", "E", "T2"]
                },
        # Point group T_d.
        '-43m': {'IR': ["T2"],
                 'Raman': ["A1", "E", "T2"]
                 },
        # Point group O_h.
        'm-3m': {'IR': ["T1u"],
                 'Raman': ["A1g", "Eg", "T2g"]
                 },
    }

    # obtain and return active band indices and irrep labels from a yaml file.

    with open(filepath, 'r') as modes:
        irreps = yaml.load(modes, Loader=yaml.CLoader)
        
        active_irreps = []
        point_group = str(irreps['point_group'])
        
        if point_group in point_groups:
            if str(spectrumtype) == 'ir':
                active_irreps = point_groups[point_group]['IR']
            elif str(spectrumtype) == 'raman':
                active_irreps = point_groups[point_group]['Raman']

        band_indices = []
        
        for mode in irreps['normal_modes']:
            if mode['ir_label'] in active_irreps:
                band_indices.append(mode['band_indices'])
    
    return band_indices
