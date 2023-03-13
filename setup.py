from importlib.metadata import entry_points
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="quantula",
    version="2023.02",
    author="Gabe DuBose",
    author_email="gabe.dubose.sci@gmail.com",
    description="A package for qunatitative image analysis",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/gabe-dubose/quantula",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires = ['matplotlib', 'numpy', 'opencv-python', 'pandas', 'tk', 'pandastable'],
    entry_points = {'console_scripts' : ['quantula-gui = quantula.gui.gui:run_gui']}
)