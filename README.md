# Computational Phonon Spectroscopy

Computational Phonon Spectroscopy is a project that implements a method into the Phonopy-Spectroscopy[[1](#Ref1)] package (which simulates vibrational spectra with outputs from Phonopy[[2](#Ref2)] and VASP[[3](#Ref3)]) that models angle-resolved polarised Raman (ARPR) spectra to obtain information on crystal surface orientations that "normal" Raman spectroscopy cannot.

Prior to this implementation, Phonopy-Spectroscopy computed Raman and IR activities for all calculated vibrational modes, this project additionally adapted the package to detect active and inactive IR and Raman vibrational modes during setup to automatically discard those that are inactive.


## Features

* Identify and return IR- and Raman-active modes when setting up calculations using the principles of group theory.

* Mathematically derive and implement a method to simulate polarised Raman experiments to complement the Phonopy-Spectroscopy package.


## Installation

This project depends on the `NumPy`[[4](#Ref4)], `Matplotlib`[[5](#Ref5)], `os`[[6](#Ref6)] and `PyYAML`[[7](#Ref7)] packages.
All four packages can be installed into a Python environment using the Anaconda platform (`conda`) and/or from PyPI (via `pip`).

Please see the Phonopy-Spectroscopy `README.md` file for further installation instructions.


## Functions

The functionality of these code files have been incorporated into the Phonopy-Spectroscopy package and the methods used to write this code are detailed in Section 2 of the project report.

`group-theory`
Contains a lookup table to determine vibrationally active and inactive irreducible representations.

`surface-normal`
Obtains the unit normal vector of a crystal surface.

`rotation-matrix`
Contains code to rotate one vector `a` onto another vector `b`.

`xy-rotation`
Rotates a vector in the xy plane by a specified rotation angle.

`polarised-raman`
Contains a function that returns either rotated Raman tensors or polar plots for all Raman-active vibrational modes.


## Thesis

As part of a master's degree, the university required the separate submission of the project's report and literature review, both can be found below:

* [Literature Review](pending link)

* [Report](pending link)


## References

1. <a name="Ref1"></a>[https://github.com/skelton-group/Phonopy-Spectroscopy/](https://github.com/skelton-group/Phonopy-Spectroscopy/)
2. <a name="Ref2"></a>[https://phonopy.github.io/phonopy/](https://phonopy.github.io/phonopy/)
3. <a name="Ref3"></a>[http://www.vasp.at/](http://www.vasp.at/)
4. <a name="Ref4"></a>[http://www.numpy.org/](http://www.numpy.org/)
5. <a name="Ref5"></a>[http://www.matplotlib.org/](http://www.matplotlib.org/)
6. <a name="Ref6"></a>[http://www.docs.python.org/3/library/os.html/](http://www.docs.python.org/3/library/os.html/)
7. <a name="Ref7"></a>[http://pyyaml.org/wiki/PyYAML](http://pyyaml.org/wiki/PyYAML)}
