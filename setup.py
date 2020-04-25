from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='openpyxl-dictreader',
    version='0.1.0',
    description='A simple package to read openpyxl worksheets like a csv DictReader',
    long_description=readme,
    author='Frank Oprel',
    url='https://github.com/foprel/openpyxl-dictreader',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)