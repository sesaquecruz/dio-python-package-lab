from setuptools import setup, find_packages

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="image-processor",
    version="0.0.1",
    author="DIO Lab",
    description="Image Processor Package",
    long_description="Image Processor Package for DIO Lab",
    url="https://github.com/sesaquecruz/dio-python-package-lab",
    packages=find_packages(),
    install_requires=requirements,
    python_requires=">=3.8"
)
