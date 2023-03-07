import os
from setuptools import find_packages, setup

NAME = 'stopwatch'
VERSION = '0.0.1'

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name=NAME,
    version=VERSION,
    author="Torsten Wylegala",
    author_email="mail@twyleg.de",
    description=("Simple stopwatch based on PyQt with QtQuick"),
    license="GPL 3.0",
    keywords="stopwatch pyqt qtquick",
    url="https://github.com/twyleg",
    packages=find_packages(),
    long_description=read('README.md'),
    install_requires=[],
    cmdclass={}
)