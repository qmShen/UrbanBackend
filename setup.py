# -*- coding:utf-8 -*-
import sys
sys.path.append('./src')
from distutils.core import setup
from urbanbackend import __version__

setup(name='urbanbackend',
      version=__version__,
      description='empty python project template',
      long_description=open("README.md").read(),
      author='qmShen',
      author_email='joyshen06@gmail.com',
      packages=['pyempty'],
      package_dir={'urbanbackend': 'src/urbanbackend'},
      package_data={'urbanbackend': ['stuff']},
      license="Public domain",
      platforms=["any"],
      url='https://github.com/qmShen/UrbanBackend')
