#!/usr/bin/env python

from distutils.core import setup

setup(name='mypkg',
      version='1.0',
      description='Test project for dependabot',
      author='Adam Lynch',
      author_email='awlynch@gmail.com',
      url='',
      packages=['mypkg'],
      install_requires=[
        "movandi-comms==1.0.14",
        ]
     )