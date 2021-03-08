import os
from setuptools import setup, find_namespace_packages

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='buho-tags',
    version='0.1.0',
    packages=find_namespace_packages(include=['buho.*']),
    include_package_data=True,
    description='This project adds support for Tags.',
    long_description=README,
    url='git@github.com:pulpo-labs/buho-tags.git',
    author='David Vartanian',
    author_email='davidvartanian@posteo.de',
    classifiers=[
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.8',
    ],
    install_requires=[
        "Django >= 3.0.0",
        "graphene >= 2.1",
        "graphene-django >= 2.15.0",
        "graphene-federation >= 0.1.0"
    ]
)
