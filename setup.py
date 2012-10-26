import os
from setuptools import (
    setup,
    find_packages,
)

version = '0.1'
project = 'kotti_theme_superhero'

tests_require = [
    'WebTest',
    'mock',
    'pytest',
    'pytest-cov',
    'pytest-xdist',
    'wsgi_intercept',
    'zope.testbrowser',
    ]

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.rst')).read()
CHANGES = open(os.path.join(here, 'CHANGES.txt')).read()

setup(name=project,
      version=version,
      description="AddOn for Kotti",
      long_description=README + '\n\n' + CHANGES,
      classifiers=[
        "Programming Language :: Python",
        "Framework :: Pyramid",
        "License :: Repoze Public License",
        ],
      keywords='kotti theme',
      author='Andreas Kaiser',
      author_email='disko@binary-punks.com',
      url='https://github.com/disko/kotti_theme_superhero',
      license='bsd',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'Kotti',
      ],
      tests_require=tests_require,
      entry_points="""
      [fanstatic.libraries]
      kotti_theme_superhero = kotti_theme_superhero.static:library
      """,
      extras_require={
          'testing': tests_require,
          },
      message_extractors={'kotti_theme_superhero': [
            ('**.py', 'lingua_python', None),
            ('**.zcml', 'lingua_xml', None),
            ('**.pt', 'lingua_xml', None),
            ]},
      )
