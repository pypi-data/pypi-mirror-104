***********************************
Requirements / Installation
***********************************

Retarded 3-layer Greens Tensors for pyGDM2 based on a fortran implementation by Gérard Colas des Francs.

pyGDM2 is available on `pypi <https://pypi.python.org/pypi/pygdm2/>`_ and `gitlab <https://gitlab.com/wiechapeter/pyGDM2>`_. 

Detailed documentation with many examples is can be found at the `pyGDM2 documentation website <https://wiechapeter.gitlab.io/pyGDM2-doc/>`_. See also the `documentation paper on arXiv (1802.04071) <https://arxiv.org/abs/1802.04071>`_ or a more `theoretical review about the GDM method <https://doi.org/10.1088/0034-4885/68/8/R05>`_.






Requirements
================================

Python
------------------
    - **python** (3.5+, `python <https://www.python.org/>`_)
    - **numpy** (`numpy <http://www.numpy.org/>`_)
    - **numba** (`numba <https://numba.pydata.org/>`_)
    - **python headers** (under linux install the package *python-dev* or *python-devel*)


Fortran
------------------
    - *fortran* compiler (tested with **gfortran**. `gcc <https://gcc.gnu.org/fortran/>`_)
    - **f2py** (comes with **numpy**. `link <http://www.numpy.org/>`_)


Optional Python packages
-------------------------------------
    - **scipy** >= v0.17.0, lower versions supported with restrictions (*Strongly recommended*. Used for standard solver LU decomposition and several tools. `scipy <https://www.scipy.org/>`_)



Installation under linux
=============================================

Via pip
-------------------------------

Install from pypi repository via

.. code-block:: bash
    
    $ pip install pygdm2_retard



Via setup script
-------------------------------

The easiest possibility to compile pyGDM2_retard is via the 
setup-script, which uses the extended *distutils* from *numpy*. 

To install the pyGDM2_retard module, run in the source directory:

.. code-block:: bash
    
    $ pip3 install -U .

or

.. code-block:: bash
    
    $ python3 setup.py install

To install as a user installation without administrator rights:

.. code-block:: bash
    
    $ pip3 install -U . --user

To install to a entirely free, user-defined location, use the *prefix* option:

.. code-block:: bash
    
    $ python3 setup.py install --prefix=/some/specific/location


To only compile without installation, use

.. code-block:: bash
    
    $ python3 setup.py build


        


Installation under windows
=============================================

For windows, we recommend `Anaconda <https://www.anaconda.com/download/#windows>`_ in which pyGDM can be installed easily via pip. On pip we provide python 3.5+ windows binaries of the pyGDM2_retard module 

Via pip
-------------------------------

We provide a 64bit windows binary on the pypi repository (tested on Win7 and Win10). Install via

.. code-block:: bash
    
    $ pip install pygdm2_retard

    
Compile using the Anaconda distribution (tested with anaconda3)
------------------------------------------------------------------------------------------
    
1. get the repo (e.g. download from gitlab)

2. install gcc compiler:

   .. code-block:: bash
    
        $ conda install m2w64-toolchain libpython

3. compile fortran parts:

   .. code-block:: bash
    
        $ python setupy.py build

4. install:

   .. code-block:: bash
    
        $ python setupy.py install





Installation under Mac OS X
=============================================

Should work under anaconda python as described above for compilation on windows.



Authors
=========================

fortran implementation
-------------------------
   - G\. Colas des Francs

python interface
------------------------
   - P\. R. Wiecha




   


