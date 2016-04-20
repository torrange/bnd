from distutils.core import setup
from Cython.Build import cythonize

setup(
  name = 'torrange bayespell',
  ext_modules = cythonize("checker.pyx"),
)
