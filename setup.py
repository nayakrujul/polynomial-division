from setuptools import setup, find_packages

long_description = 'Divide polynomials - read the docs at https://www.github.com/nayakrujul/polynomial-division'

setup(
  name = 'polynomial-division',
  version = '1.0',
  license='Apache',
  description = 'Divide polynomials',
  author = 'Rujul Nayak',
  author_email = 'rujulnayak@outlook.com',
  url = 'https://github.com/nayakrujul/polynomial-division',
  download_url = 'https://github.com/nayakrujul/polynomial-division/archive/refs/tags/v_01.tar.gz',
  keywords = ['math', 'polynomial', 'division'],
  install_requires=[
      ],
  classifiers=[
    'Development Status :: 3 - Alpha', 
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
  ],
  long_description=long_description,
  long_description_content_type='text/x-rst',
  packages = find_packages(),
  entry_points = {
    'console_scripts': [
      'divide = polynomial_division.pd:cmdline'
    ]
  }
)
