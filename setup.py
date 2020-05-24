from setuptools import setup, find_packages

setup(
  name='mymodule',
  use_scm_version=True,
  setup_requires=[
    'setuptools_scm',
  ],
  packages=find_packages(exclude=['Test']),
  install_requires=[
    'flask==1.0',
    'six==1.10.0',
  ],
)