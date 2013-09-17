#!/usr/bin/env python2
# -*- encoding: utf-8 -*-
#   Author(s): Milan Falesnik   <milan@falesnik.net>
#                               <mfalesni@redhat.com>
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

from setuptools import setup
import os


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name="Run",
    version="1.0",
    author="Milan Falešník",
    author_email="milan@falesnik.net",
    description="Simple command runner",
    license="GPLv2",
    keywords="run command bash shell",
    url="http://python.falesnik.net/Run",
    packages=["Run"],
    long_description_read=read("README.md"),
    classifiers=[
        "Topic :: Utilities"
    ]
)
