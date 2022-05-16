from setuptools import setup


with open("README.md") as f:
    readme = f.read()

with open("LICENSE") as f:
    license = f.read()

requirements = [
    "openpyxl==2.6.4 ; python_version < '3.0' ",
    "openpyxl~=3.0.3 ; python_version >= '3.0' ",
]


setup(
    name="openpyxl-dictreader",
    version="0.1.8",
    description="A simple package to read openpyxl worksheets like a csv DictReader",
    long_description=readme,
    long_description_content_type="text/markdown",
    author="Frank Oprel",
    author_email="oprel.fj@gmail.com",
    url="https://github.com/foprel/openpyxl-dictreader",
    install_requires=requirements,
    license=license,
    py_modules=["openpyxl_dictreader"],
)
