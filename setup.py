from setuptools import setup, find_packages
from typing import List

def get_requirements(file_path: str) -> List[str]:
    with open(file_path, 'r') as file:
        return [line.strip() for line in file.read().splitlines() if line.strip()]

setup(
    name='DiamondPricePrediction',
    version='0.0.1',
    author='Md Moazzam Ali',
    author_email='mdmoazzamali984@gmail.com',
    install_requires=get_requirements('requirements.txt'),
    packages=find_packages(),
)
