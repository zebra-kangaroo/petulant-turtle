from setuptools import setup, find_packages
import sys, os

version = '0.0.1'

setup(name='wepay',
      version=version,
      description="Python SDK for WePay API's",
      long_description=open('README.md', 'r').read(),
      classifiers=[
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'License :: OSI Approved :: Apache Software License'], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='Python SDK Payments WePay API',
      author='WePay Inc.',
      author_email='api@wepay.com',
      url='http://www.wepay.com/developer',
      license='Apache License 2.0',
      packages=['wepay'],  # find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'requests'
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
