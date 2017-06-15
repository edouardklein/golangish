from setuptools import setup, find_packages
from codecs import open
from os import path

__version__ = '0.0.1'

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()


install_requires = ['sphinx', 'doctest', 'flake8']  # FIXME: Explicit requirements here
dependency_links = []  # FIXME: For packages not in pypi http://python-packaging.readthedocs.io/en/latest/dependencies.html#packages-not-on-pypi

setup(
    name='FIXME',
    version=__version__,
    description='FIXME',
    long_description=long_description,
    url='FIXME',
    download_url='https://github.com/edouardklein/FIXME/tarball/' + __version__,
    license='FIXME',
    classifiers=[
        'FIXME'
    ],
    keywords='FIXME',
    packages=find_packages(exclude=['docs', 'tests*']),
    include_package_data=True,
    author='Edouard Klein',
    install_requires=install_requires,
    dependency_links=dependency_links,
    author_email='edouardklein -at- gmail.com'
)
