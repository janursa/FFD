import setuptools
import codecs
import os.path

def read(rel_path):
    here = os.path.abspath(os.path.dirname(__file__))
    with codecs.open(os.path.join(here, rel_path), 'r') as fp:
        return fp.read()

def get_version(rel_path):
    for line in read(rel_path).splitlines():
        if line.startswith('__version__'):
            delim = '"' if '"' in line else "'"
            return line.split(delim)[1]
    else:
        raise RuntimeError("Unable to find version string.")
def extract_longDiscription(file_name):
    with open(file_name, "r") as fh:
        long_description = fh.read()
    return long_description
setuptools.setup(
    name="barneySA",
    version=get_version("BarneySA/__init__.py"),
    author="Jalil Nourisa",
    author_email="jalil.nourisa@gmail.com",
    description="A general-purpose sensitivity analsysi library based on fractional factorial design and the analysis of variance",
    long_description=extract_longDiscription("README.md"),
    long_description_content_type="text/markdown",
    url="https://github.com/janursa/barneySA",
    packages=setuptools.find_packages(),
    install_requires=[ 'numpy >= 1.18.4', 'mpi4py >= 3.0.3', 'doepy >= 0.0.1'],
    classifiers=[
        "Programming Language :: Python :: 3",
        # "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
