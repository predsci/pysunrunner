#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name="pysunrunner",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        'numpy==1.24.4',
        #'matplotlib==3.9.1',
        'scipy==1.9.1',
        'pillow==10.4.0',
    ],
    author="Predictive Science Inc., pyPLUTO routines by Dr. Bhargav Vaidya",
    author_email="pete@predsci.com, jriley@predsci.com, mbennun@predsci.com",
    description="A package for imaging and plotting data from sunrunner3D simulations",
    url="https://github.com/predsci/pysunrunner", 
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.9',
)

