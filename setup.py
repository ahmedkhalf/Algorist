import re

from setuptools import find_packages, setup  # type: ignore
from setuptools.extern import packaging  # type: ignore

# Version info -- read without importing
with open("algorist/__init__.py", "rt", encoding="utf8") as f:
    version_re = re.search(r"__version__ = \"(.*?)\"", f.read())
    if version_re:
        version = version_re.group(1)
    else:
        raise ValueError("Could not determine package version")
    # Normalize version so `setup.py --version` show same version as twine.
    version = str(packaging.version.Version(version))

# Add readme as long description
with open("README.md") as f:
    long_description = f.read()

# Library dependencies
INSTALL_REQUIRES = [
    "numpy",
    "pycairo",
]

setup(
    name="algorist",
    version=version,
    license="MIT",
    description="Algorist is a simple yet powerful library for composing algorithmic and generative art in Python.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ahmedkhalf/Algorist/",
    packages=find_packages(),
    author="Ahmed Khalf",
    author_email="ahmedkhalf567@gmail.com",
    python_requires=">=3.6",
    install_requires=INSTALL_REQUIRES,
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Topic :: Artistic Software",
        "Topic :: Education",
        "Topic :: Multimedia :: Graphics",
        "Topic :: Software Development",
    ],
)
