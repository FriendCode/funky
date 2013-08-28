#!/usr/bin/python

try:
    from setuptools import setup, Extension
    has_setuptools = True
except ImportError:
    from distutils.core import setup, Extension
    has_setuptools = False

version_string = '0.0.2'


setup_kwargs = {}

setup(name='funky',
      description='A bunch of functionnal tools',
      keywords='tool functionnal pure python funky',
      version=version_string,
      url='https://github.com/FriendCode/funky.git',
      license='MIT',
      author="Aaron O'Mullan",
      author_email='aaron.omullan@friendco.de',
      long_description="""
      Funky is a package of some useful functionnal constructs for python.
      """,
      packages=['funky'],
      **setup_kwargs
)
