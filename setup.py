"""
Module: setup.py

The setup script for the Python SDK package.
This makes it installable through pip.

Dependancies:
    setuptools: Used to package the Python SDK.
"""

from setuptools import setup


setup(
    name='python-sdk',
    version='0.1.0',
    author='Luke Robertson',
    author_email='luke.robertson@networkdirection.net',
    description=(
        """
        A Python SDK for interacting with Docker container projects
        via REST API
        """
    ),
    packages=['sdk'],
    install_requires=[
        'requests',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
