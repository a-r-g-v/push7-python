from setuptools import setup

setup(
    name='push7',
    version='0.0.1',
    description='Python API Client for Push7',
    license="MIT",
    keywords="push7",
    author='a_r_g_v',
    author_email='info@arg.vc',
    url='https://github.com/a-r-g-v/push7-python',
    test_suite='tests',
    packages=['push7'],
    install_requires=['requests', 'simplejson', 'six', 'enum34'])
