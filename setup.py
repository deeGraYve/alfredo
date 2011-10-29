#!/usr/bin/env python
# encoding: utf-8
from setuptools import setup
import os
import sys

setup(
  name="alfredo",
  version="0.1",
  url="https://github.com/daltonmatos/alfredo",
  license="3-BSD",
  description="Alfredo is a gtalk bot born so serve you.",
  author="Dalton Barreto",
  author_email="daltonmatos@gmail.com",
  long_description=open('README.rst').read(),
  packages=['alfredo'],
  scripts=['scripts/alfredo'],
  install_requires = ['plugnplay', 'xmpppy'],
  classifiers = [
    "License :: OSI Approved :: BSD",
    "Operating System :: OS Independent",
    "Programming Language :: Python",
    "Topic :: Software Development :: Libraries :: Application Frameworks"
    ])

