import os
from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext

import numpy as np

incdirs = [os.path.join(os.getcwd()), np.get_include()]  # DIFF: removed 'src'

ext_modules = [
    Extension("rect.rectangle", ['src/rectangle.cpp', "rect/rectangle.pyx", ],
    	      include_dirs=incdirs, language="c++"),

    Extension("rect.xdress_extra_types", ["rect/xdress_extra_types.pyx"], # DIFF: s/rect/xdress/
              include_dirs=incdirs, language="c++"),

    # FIXME: we are compiling the object file for rectangle twice
    Extension("rect.dtypes", ['src/rectangle.cpp', "rect/dtypes.pyx"],
              include_dirs=incdirs, language="c++"),

    Extension("rect.stlcontainers", ['src/rectangle.cpp', "rect/stlcontainers.pyx"],
              include_dirs=incdirs, language="c++"),
   ]

setup(
  name = 'rect',
  cmdclass = {'build_ext': build_ext},
  ext_modules = ext_modules,
  packages = ['rect']
)
