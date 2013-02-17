#!/usr/bin/python
# Setup file for dulwich_paramiko

try:
    from setuptools import setup, Extension
    has_setuptools = True
except ImportError:
    from distutils.core import setup, Extension
    has_setuptools = False

version_string = '0.0.1'


setup_kwargs = {}

setup(name='funky',
      description='A bunch of functionnal tools',
      keywords='tool functionnal pure python funky',
      version=version_string,
      url='git+ssh://git@friendco.de:friendcode/funky.git',
      license='MIT',
      author="Aaron O'Mullan",
      author_email='aaron.omullan@gmail.com',
      long_description="""
      Funky is a package of some useful functionnal constructs for python.
      """,
      packages=['funky'],
      **setup_kwargs
)
