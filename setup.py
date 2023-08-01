from setuptools import setup, find_packages
VERSION = '0.1'

setup(
	name='ChenLabPyLib', 
	version=VERSION,
	url='https://github.com/kevry/ChenLabPyLib',
	author='Kevin Delgado', 
	author_email='common.chenlab@gmail.com',
	packages=find_packages(),
    requires=['requests']
)