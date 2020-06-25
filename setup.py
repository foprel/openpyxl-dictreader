from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

requirements = [
    "et-xmlfile==1.0.1",
    "jdcal==1.4.1",
    "openpyxl==3.0.3",
    ]

setup(
    name='openpyxl-dictreader',
    version='0.1.2',
    description='A simple package to read openpyxl worksheets like a csv DictReader',
    long_description=readme,
    author='Frank Oprel',
    author_email="oprel.fj@gmail.com",
    url='https://github.com/foprel/openpyxl-dictreader',
    install_requires=requirements,
    license=license,
    py_modules=["openpyxl_dictreader"]
)

