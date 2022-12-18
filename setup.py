from setuptools import setup
from typing import List



PROJECT_NAME = "housing-predictor"
VERSION = "0.0.1"
AUTHOR = "Shubham Wasnik"
DESCRIPTION = "This is project based on linear regression"
PACKAGES = ["housing"]
REQUIREMENT_FILE_NAME = "requirements.txt"


def get_requirements_list()->List[str]:
    """
    Descriptions: This function is going to return list of requirements mentioned in requirements.txt

    return this function will return a list of requirements packages
    """
    with open(REQUIREMENT_FILE_NAME) as requirement_file:
        return requirement_file.readlines()


setup(
    name=PROJECT_NAME,
    version=VERSION,
    author=AUTHOR,
    description=DESCRIPTION,
    packages=PACKAGES,
    install_requires=get_requirements_list()
)

