from setuptools import setup,find_packages

from typing import List

def get_requirements()->List[str]:

    requirement_list:List[str]=[]
    try:
        with open("requirements.txt") as file:
            #Read lines from he file
            lines=file.readlines()
            ## process each line
            for line in lines:
                requirement=line.strip()
                ## ignore empty lines and -e.
                if requirement and requirement!="-e .":
                    requirement_list.append(requirement)

    except FileNotFoundError:
        print("requirements.txt not found")
    return requirement_list

setup(
    name="Network Security",
    version="0.0.1",
    author="Kushagra Gaur",
    author_email="kgaur7164@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements() 
)
        