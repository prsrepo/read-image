from setuptools import setup
from pip.req import parse_requirements

install_reqs = parse_requirements('requirements.txt')

reqs = [str(ir.req) for ir in install_reqs]

setup(
   name='read-image',
   version='0.0.1',
   description='OCR',
   author='pcbuddies',
   author_email='pcbuddies',
   packages=['read_image'], 
   install_requires=reqs
)