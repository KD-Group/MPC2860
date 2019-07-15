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


# pass cmdclass={'bdist_wheel': bdist_wheel} to set {abi tag} none
# wheel file format:
# {distribution}-{version}(-{build tag})?-{python tag}-{abi tag}-{platform tag}.whl
try:
    from wheel.bdist_wheel import bdist_wheel as _bdist_wheel
    class bdist_wheel(_bdist_wheel):
        def finalize_options(self):
            _bdist_wheel.finalize_options(self)
            self.root_is_pure = True
except ImportError:
    bdist_wheel = None


copy_ext_modules()

setup(name='MPC2860',
      version='0.3',
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
          'bdist_wheel': bdist_wheel,
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
