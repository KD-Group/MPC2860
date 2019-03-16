#!/usr/bin/env python
"""
setup.py file for motion module
"""

from setuptools import Extension, find_packages, setup
from setuptools.command.build_py import build_py

MOTION_EXT = Extension(
    name='_motion_2860',
    sources=[
        'src/motion_2860.i',
    ],
    library_dirs=['src'],
    libraries=['MPC2860'],
    swig_opts=['-c++'],
)


# Build extensions before python modules,
# or the generated SWIG python files will be missing.
class BuildPy(build_py):
    def run(self):
        self.run_command('build_ext')
        super(build_py, self).run()


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
      packages=find_packages('src'),
      package_dir={'': 'src'},
      package_data={'src': ['*.h', '*.dll', '*.lib', '*.txt', '*.pyd']},
      ext_modules=[MOTION_EXT],
      cmdclass={
          'build_py': BuildPy,
      },

      python_requires='>=3.4',
      )
