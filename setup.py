import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="radarboxplot",
    version="0.1.3",
    author="Caio Hamamura",
    author_email="caio.hamamura@usp.br",
    description="Implements the radar-boxplot using matplotlib",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/caiohamamura/radarboxplot-python",
    install_requires=['matplotlib', 'numpy'],
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)