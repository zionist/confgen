from distutils.core import setup
from setuptools import setup, find_packages

setup( name='confgen',
    version='0.1',
    description='Simple nginx conf gen tool',
    author='slaviann',
    author_email='slaviann@gmail.com',
    packages=find_packages(),
      #install_requires=[
      #    'dpkt-fix',
      #],
    scripts=['bin/confgen'],

    )
