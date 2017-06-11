from setuptools import setup

import os


long_description = ""
if os.path.exists('README.md'):
    long_description = open('README.md').read()


setup(
    name='push7',
    version='0.0.4',
    description='Python API Client for Push7',
    long_description=long_description,
    license="MIT",
    keywords="push7",
    author='a_r_g_v',
    author_email='info@arg.vc',
    url='https://github.com/a-r-g-v/push7-python',
    test_suite='tests',
    packages=['push7'],
    install_requires=['requests', 'simplejson', 'six', 'enum34'])
