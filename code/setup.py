from distutils.core import setup, Extension
import numpy

setup(
    ext_modules=[
        Extension("model", ["model.c"],
                  include_dirs=[numpy.get_include()]),
    ],
)

