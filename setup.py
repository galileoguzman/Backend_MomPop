#!/usr/bin/env python

from setuptools import setup

setup(
    # GETTING-STARTED: set your app name:
    name='MomAndPop',
    # GETTING-STARTED: set your app version:
    version='1.0',
    # GETTING-STARTED: set your app description:
    description='Mom and pop app instructs parents to take control and help their kids to develop habilities and a healthy lifestyle.',
    # GETTING-STARTED: set author name (your name):
    author='@galileoguzman',
    # GETTING-STARTED: set author email (your email):
    author_email='mompopapp@gmail.com',
    # GETTING-STARTED: set author url (your url):
    url='https://github.com/galileoguzman/Backend_MomPop',
    # GETTING-STARTED: define required django version:
    install_requires=[
        'Django==1.8.4'
    ],
    dependency_links=[
        'https://pypi.python.org/simple/django/'
    ],
)
