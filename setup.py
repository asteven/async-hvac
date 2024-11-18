#!/usr/bin/env python
import os
import pathlib
import sys
from setuptools import setup, find_packages

version = '9.9.9'
for candidate in ('async_hvac/version', 'version'):
    path = pathlib.Path(candidate)
    with path.open('r') as f:
        version = f.read()
        break

setup(
    name='async-hvac',
    #version=open(vsn_path, 'r').read(),
    version=version,
    description='HashiCorp Vault API client',
    long_description='HashiCorp Vault API python 3.6+ client using asyncio.',
    author='Lionel Zerbib',
    author_email='lionel@alooma.io',
    url='https://github.com/Aloomaio/async-hvac',
    keywords=['hashicorp', 'vault', 'hvac'],
    classifiers=['License :: OSI Approved :: Apache Software License'],
    packages=find_packages(),
    install_requires=[
        'aiohttp==3.3.1',
    ],
    include_package_data=True,
    package_data={'async_hvac': ['version']},
    extras_require={
        'parser': ['pyhcl==0.3.10']
    }
)
