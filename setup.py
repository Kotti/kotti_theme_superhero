import os
from setuptools import find_packages
from setuptools import setup


version = '0.1'
project = 'kotti_theme_superhero'

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.rst')).read()
CHANGES = open(os.path.join(here, 'CHANGES.txt')).read()

setup(name=project,
      version=version,
      description="Superhero bootstrap theme for Kotti",
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
      license='BSD',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
        'Kotti',
      ],
      entry_points="""
      [fanstatic.libraries]
      kotti_theme_superhero = kotti_theme_superhero.static:library
      """,
      )
