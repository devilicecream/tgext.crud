from setuptools import setup, find_packages
import os

version = '0.6.0'

here = os.path.abspath(os.path.dirname(__file__))
try:
    README = open(os.path.join(here, 'README.txt')).read()
    CHANGES = open(os.path.join(here, 'docs/HISTORY.txt')).read()
except IOError:
    README = CHANGES = ''

setup(name='tgext.crud',
      version=version,
      description="Crud Controller Extension for TG2",
      long_description=README + "\n" +
                       CHANGES,
      # Get more strings from http://www.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='turbogears2.extension, TG2, REST, crud, sprox',
      author='Christopher Perkins',
      author_email='chris@percious.com',
      url='https://github.com/TurboGears/tgext.crud',
      license='MIT',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['tgext'],
      include_package_data=True,
      zip_safe=True,
      install_requires=[
          'sprox>=0.8.3',
          # -*- Extra requirements: -*-
      ],
      test_suite='nose.collector',
      tests_require=[
          'nose',
          'webtest',
          'TurboGears2',
          'jinja2',
          'sqlalchemy',
          'zope.sqlalchemy',
          'transaction',
          'tw2.core',
          'tw2.forms'
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
