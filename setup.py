'''
The setup.py file is essential part of packaging and distributing Python projects.
It is used by setuptools to define the configuration of your project,
such as metadata, dependencs and more
'''

from setuptools import find_packages,setup
from typing import List

def get_requirements()->list[str]:

    '''
    This function will return list of requirements

    '''

    requirement_lst:List[str]=[]

    try:
        with open('requirements.txt','r') as file:
            #Read lines from the file
            lines = file.readlines()
            #Process each line
            for line in lines:
                requirement = line.strip()
                ## ignore empty lines and -e.
                if requirement and requirement != '-e .':
                    requirement_lst.append(requirement)

    except FileNotFoundError:
        print('reqiurements.txt file not found')

    return requirement_lst


setup(
    name='Network Security',
    version='0.0.1',
    author='Uday Islam',
    author_email='udayislam@gamil.com',
    packages=find_packages(),
    install_requires=get_requirements()
)