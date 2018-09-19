import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="neutompy",
    version="1.0.0",
    author="Davide Micieli",
    author_email="neutompy@gmail.com",
    description="Python package for tomographic data processing and reconstruction",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/dmici/NeuTomPy-toolbox",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Intended Audience :: Science/Research",
        "Intended Audience :: Education",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Operating System :: OS Independent",
    ],
)