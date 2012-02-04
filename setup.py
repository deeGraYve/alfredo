#!/usr/bin/env python
# encoding: utf-8
from setuptools import setup
import os
import sys

with open('README.rst') as f:
    long_description = f.read()

setup(
  name="alfredo",
  version="0.1",
  url="https://github.com/daltonmatos/alfredo",
  license="3-BSD",
  description="Alfredo is a gtalk bot born so serve you.",
  author="Dalton Barreto",
  author_email="daltonmatos@gmail.com",
  long_description=long_description,
  packages=['alfredo'],
  scripts=['script/alfredo', 'script/ud'],
  install_requires = ['plugnplay', 'xmpppy', 'requests', 'beautifulsoup', 'simplejson'],
  classifiers = [
    "License :: OSI Approved :: BSD License",
    "Operating System :: OS Independent",
    "Programming Language :: Python",
    "Topic :: Software Development :: Libraries :: Application Frameworks"
    ])

