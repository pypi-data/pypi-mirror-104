from setuptools import find_packages, setup
from my_pip_pkg import __version__
import pathlib

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

setup(
    name='cs253_demo_pip_abhay',
    version="1.0.1",

    description="A demo peoject for CS253 presentation",
    url='https://demo_project.com/dummy.xml',
    long_description=README,
    long_description_content_type="text/markdown",
    author='Abhay',
    author_email='abhaymishra3420@gmail.com',
    install_requires=["numpy"],
    packages=find_packages(),
)
