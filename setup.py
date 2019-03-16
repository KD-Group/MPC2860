#!/usr/bin/env python
"""
setup.py file for motion module
"""

import os
import shutil
from setuptools import Extension, find_packages, setup
from setuptools.command.build_py import build_py


def copy_ext_modules():
    ext_module_path = 'build/lib.win32-3.4/_motion_2860.pyd'
    if os.path.exists(ext_module_path):
        shutil.copy(ext_module_path, 'MPC2860/_motion_2860.pyd')


MOTION_EXT = Extension(
    name='_motion_2860',
    sources=[
        'MPC2860/motion_2860.i',
    ],
    library_dirs=['MPC2860'],
    libraries=['MPC2860'],
    swig_opts=['-c++'],
)


# Build extensions before python modules,
# or the generated SWIG python files will be missing.
class BuildPy(build_py):
    def run(self):
        self.run_command('build_ext')
        super(build_py, self).run()


copy_ext_modules()

setup(name='MPC2860',
      version='0.1',
      author="SF Zhou, WingC",
      author_email="1018957763@qq.com",
      description="""Python module for MPC2860""",
      license='GPL',
      classifiers=[
          'Development Status :: 3 - Alpha',
          'Intended Audience :: Developers',

          'License :: OSI Approved :: GNU Affero General Public License v3',
          'Programming Language :: Python :: 3',
      ],
      cmdclass={
          'build_py': BuildPy,
      },
      packages=find_packages(),
      package_dir={'MPC2860': 'MPC2860'},
      ext_modules=[MOTION_EXT],
      # If key is '' means any package('MPC2860 means only include in MPC2860 package)
      # contains *.dll or *.lib or *.txt files, include them:
      package_data={'MPC2860': ['*.dll', '*.lib', '*.txt', '*.pyd']},
      include_package_data=True,

      python_requires='>=3.4',
      )
