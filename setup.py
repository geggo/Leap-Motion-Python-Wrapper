#!/usr/bin/env python

#swig -c++ -python -o LeapPython.cpp -interface LeapPython Leap.i

from distutils.core import setup, Extension

#module = Extension('LeapPython',
#                   sources=['LeapPython.cpp'],
#                   )

module = Extension('LeapPython',
                   sources=['Leap.i'],
                   swig_opts=['-c++',]
                   )

setup(name = 'example',
      ext_modules = [module],
      py_modules = ['Leap'],
      )
