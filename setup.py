from setuptools import setup
import re, uuid
from setuptools import setup, find_packages

def parse_requirements(filename):
    """ load requirements from a pip requirements file """
    lineiter = (line.strip() for line in open(filename))
    return [line for line in lineiter if line and not line.startswith("#")]

install_reqs = parse_requirements('requirements.txt')
reqs = install_reqs

setup(
   name='read-image',
   version='0.0.1',
   description='OCR',
   author='pcbuddies',
   author_email='pcbuddies',
   packages=['read_image'], 
   install_requires=reqs,
   keywords="Python image reader",
   classifiers=[
         'Development Status :: 4 - Beta',
         'Topic :: Software Development :: Libraries',
         'License :: OSI Approved :: MIT License',
         'Operating System :: OS Independent',
         'Programming Language :: Python',
         'Programming Language :: Python :: 3.6',
         'Programming Language :: Python :: 3.7',
   ],
   zip_safe=True
)