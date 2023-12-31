import os
import io
from setuptools import setup, find_packages

HERE = os.path.dirname(os.path.realpath(__file__))

README = os.path.join(HERE, "README.md")
with io.open(README, encoding="utf-8") as f:
    long_description = f.read()

VERSION = os.path.join(HERE, "molecule_schema", "version.py")
with io.open(VERSION, encoding="utf-8") as f:
    package = {}
    exec(f.read(), package)
    version = package["VERSION"]

setup(
    name="molecule-schema",
    version=version,
    description="Molecule Code First Schema",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/doitian/molecule-schema-python",
    author="ian",
    author_email="ian@nervos.org",
    license="MIT",
    packages=find_packages(),
    install_requires=[],
    scripts=[],
    zip_safe=False,
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Environment :: Console",
        "Topic :: File Formats",
    ],
    include_package_data=True,
)
