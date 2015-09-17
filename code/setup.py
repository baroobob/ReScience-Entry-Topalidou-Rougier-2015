from distutils.core import setup, Extension
from Cython.Build import cythonize
import numpy

cythonize("model.pyx")

setup(
    ext_modules=[
        Extension("model", ["model.c"], include_dirs=[numpy.get_include()])
    ]
)


