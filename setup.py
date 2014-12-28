#!/usr/bin/env python

#setup.py build_ext --inplace

from distutils.core import setup, Extension

module = Extension('_Leap',
                   sources=['Leap.i'],
                   swig_opts=['-c++',],
                   libraries=['Leap'],
                   library_dirs=['.',],
                   )

setup(name = 'example',
      ext_modules = [module],
      py_modules = ['Leap'],
      )
