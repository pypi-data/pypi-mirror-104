from setuptools import setup, find_packages

setup(
  name = 'uchu',
  packages = find_packages(),
  version = '0.0.12',
  description = 'Sane interface to cloud services.',
  long_description = '',
  author = '',
  license = '',
  package_data={},
  url = 'https://github.com/alvations/uchu',
  keywords = [],
  classifiers = [],
  install_requires = ['boto3', 'botocore'],

)
