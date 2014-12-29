#!/usr/bin/env python

#setup.py build_ext --inplace

import os, os.path, platform
from setuptools import setup, Extension

LEAP_SDK_DIR = r'../LeapSDK'
LEAP_LIB = 'libLeap.dylib'

def copy_files_to_package():
    import shutil
    shutil.copy(
        os.path.join(LEAP_SDK_DIR, 'lib', LEAP_LIB),
        'Leap')

    shutil.copy(
        os.path.join(LEAP_SDK_DIR, 'include', 'Leap.i'),
        'Leap')
    print('copied files to package')
    

module = Extension('Leap._Leap',
                   sources=['Leap/Leap.i'],
                   swig_opts=['-c++', '-I'+os.path.join(LEAP_SDK_DIR, 'include')],
                   include_dirs = [os.path.join(LEAP_SDK_DIR, 'include'),],
                   libraries=['Leap'],
                   library_dirs=['Leap',],
                   )

copy_files_to_package()
setup(name = 'Leap',
      description = 'Leap Motion SDK Python wrapper',
      packages=['Leap'],
      ext_modules = [module],
      package_data={'Leap': [LEAP_LIB,]},
      )
