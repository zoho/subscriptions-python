# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'subscriptions'))

requires = ['requests', 'jsons']
try:
    import jsons
except ImportError:
    try:
        import json
    except ImportError:
        requires.append('simplejson')  # For Python==2.5

setup(
    name='subscription',
    version='0.1.0',
    author='Subscription',
    author_email=' support@zohosubscriptions.com',
    url='https://www.zoho.com/subscriptions/api/v1/#introduction',
    description='Python wrapper for the Zoho Subscription Billing API',
    packages=find_packages(exclude=['tests']),
    install_requires=requires,
    test_suite='tests',
)
