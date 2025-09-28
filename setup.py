from setuptools import setup, find_packages
from typing import List

HYPENE_DOT = '-e .'
def get_requirements(file_path:str)->list[str]:
    '''
    This function will return the list of requirements
    '''
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]
        
        if '-e .' in requirements:
            requirements.remove(HYPENE_DOT)
    
    return requirements



setup(
    name='MLproject',
    version='0.1.0',
    author='sumeet',
    author_email="sumeetpatekarr@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)