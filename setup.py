#!/usr/bin/env python3

from setuptools import setup
import os


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name='tmc',
    version='0.3.0',
    description='TestMyCode client',
    long_description=read("README.md"),
    author='Juhani Imberg',
    author_email='juhani@imberg.com',
    url='http://github.com/JuhaniImberg/tmc.py/',
    license='MIT',
    packages=['tmc'],
    entry_points={
        'console_scripts': [
            'tmc = tmc.__main__:main',
            'tmc3 = tmc.__main__:main'
        ]
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Console",
        "Environment :: Console :: Curses",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4"
    ],
    install_requires=[
        "requests == 2.2.1",
        "argh == 0.25.0",
        "peewee == 2.2.5"
    ],
)
