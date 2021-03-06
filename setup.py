# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='ooex',
    version='0.0.1',
    description='ooex package: practicing object oriented design in python',
    long_description=readme,
    author='Max Joseph',
    author_email='maxwellbjoseph@gmail.com',
    url='https://github.com/mbjoseph/oo-ex',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)
