from distutils.core import setup
from setuptools import setup, find_packages

setup(
  name              = 'hubarcode',
  packages          = find_packages(),
  version           = '1.0.0',
  description       = 'A library to generate DataMatrix barcodes',
  author            = 'Olivier Bodarwé',
  author_email      = 'olivier.bodarwe@labsolution.lu',
  url               = 'https://github.com/labsolutionlu/hubarcode',
  download_url      = 'https://github.com/labsolutionlu/hubarcode/archive/1.0.0.zip',
  keywords          = ['Datamatrix', 'hubarcode', 'barcode', 'lx'],
  classifiers       = [],
  install_requires  = ['pillow'],
  zip_safe          = True,
)
