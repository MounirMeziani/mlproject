from setuptools import find_packages, setup
from typing import List


hyphen_E_DOT = '-e .'

def get_requirements(file_path:str)->list[str]:

    '''
    
    this function will return a list of requirments

    '''
    
    requirements = []

    with open (file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements= [req.replace("\n","") for req in requirements]

        if hyphen_E_DOT in requirements:
            requirements.remove (hyphen_E_DOT)



setup (

name = 'mlproject',
version = '0.0.1',
author = 'Mounir',
packages = find_packages(),
install_requires =get_requirements('requirements.txt')
)