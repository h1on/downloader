from os import name
import setuptools
from setuptools import version

setuptools.setup(
    name="google-image-downloader",
    version="1.0",
    license="MIT",
    author="h1on",
    author_email="c01066033993@gmail.com",
    description="Download images from any website",
    long_description=open('README.md').read(),
    url="https://github.com/h1on/downloader",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
)
