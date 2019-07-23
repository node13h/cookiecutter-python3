#!/usr/bin/env python3

from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

with open(path.join(here, 'VERSION')) as f:
    version = f.read().strip()

{%- set license_classifiers = {
    'MIT': 'License :: OSI Approved :: MIT License',
    'GPLv3': 'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
    'AGPLv3': 'License :: OSI Approved :: GNU Affero General Public License v3'
} %}

setup(
    name='{{ cookiecutter.project_name }}',

    version=version,

    description='{{ cookiecutter.project_description }}',
    long_description=long_description,
    long_description_content_type='text/markdown',

    url='{{ cookiecutter.project_url }}',

    author='{{ cookiecutter.project_author }}',
    author_email='{{ cookiecutter.project_author_email }}',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 3 - Alpha',
{%- if cookiecutter.open_source_license in license_classifiers %}
        '{{ license_classifiers[cookiecutter.open_source_license] }}',
{%- endif %}
        'Programming Language :: Python :: 3',
    ],

    packages=find_packages(exclude=['tests']),
    include_package_data=True,

    # See https://packaging.python.org/en/latest/requirements.html
    install_requires=[
    ],

    scripts=[
    ],

    zip_safe=False,
)
