from setuptools import find_packages, setup
from typing import List

def requirements(file_path:str)->List[str]:
  with open(file_path) as f:
    requirements = f.readlines()
    requirements = [req.replace('\n','') for req in requirements]
  
  return requirements

setup(
    name='mlproject',
    version='0.0.1',
    author='Sudarshan Trifaley',
    # author_email='getwebsud@gmail.com',
    packages=find_packages(),
    install_requires=requirements('requirements.txt'),
    maintainer='Sudarshan Trifaley',
    maintainer_email='trifaleysudarshan@gmail.com'
)